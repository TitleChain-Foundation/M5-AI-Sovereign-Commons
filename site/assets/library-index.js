// Offline, deterministic discovery. No models, trackers, credentials or remote APIs.
(() => {
  const list = document.getElementById('library-results');
  if (!list) return;
  const cards = [...list.querySelectorAll('.library-card')];
  const query = document.getElementById('library-query');
  const format = document.getElementById('library-format');
  const sort = document.getElementById('library-sort');
  const topics = [...document.querySelectorAll('[data-library-topic]')];
  const count = document.getElementById('library-count');
  const more = document.getElementById('library-more');
  const empty = document.getElementById('library-empty');
  let topic = 'all', limit = 12;
  const normalize = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  const synonyms = {iam:['iam','m5iam','identity','onboarding'],pod:['pod','m5pod','workspace'],consent:['consent','refusal'],code:['code','implementation'],privacy:['privacy','sovereignty','consent'],spring:['spring','312'],farm:['farm','farmland','ranch'],regulation:['regulatory','sec']};
  const starting = ['README.md','GLOSSARY.md','standards/README.md','reference-implementation/README.md','pilots/README.md','RELEASE-STATUS.md','THREAT-MODEL.md','LICENSE.md'];
  const info = cards.map((card, index) => ({card, index, text:normalize(card.dataset.search), title:card.querySelector('h3').textContent, source:card.querySelector('code').textContent}));
  function render() {
    const words = normalize(query.value).split(' ').filter(Boolean);
    const matches = info.filter(x => (topic === 'all' || x.card.dataset.topic === topic) && (format.value === 'all' || x.card.dataset.format === format.value) && words.every(word => (synonyms[word] || [word]).some(term => x.text.includes(term))));
    matches.sort((a,b) => {
      if (sort.value === 'az') return a.title.localeCompare(b.title, 'en') || a.index-b.index;
      const rank = x => starting.includes(x.source) ? starting.indexOf(x.source) : 1000+x.index;
      return rank(a)-rank(b);
    });
    cards.forEach(card => {card.hidden = true;});
    for (const [i, item] of matches.entries()) { list.append(item.card); item.card.hidden = i >= limit; }
    const shown = Math.min(limit, matches.length);
    count.textContent = matches.length ? `${shown} of ${matches.length} documents` : '0 documents';
    more.hidden = shown >= matches.length;
    more.textContent = `Show ${Math.min(12, matches.length-shown)} more documents`;
    empty.hidden = matches.length !== 0;
    topics.forEach(link => {const active=link.dataset.libraryTopic===topic;link.classList.toggle('is-active',active);if(active)link.setAttribute('aria-current','true');else link.removeAttribute('aria-current');});
    document.getElementById('library-topic-heading').textContent = topic === 'all' ? 'All documents' : topics.find(x=>x.dataset.libraryTopic===topic).firstElementChild.textContent;
  }
  function reset() {topic='all';query.value='';format.value='all';sort.value='recommended';limit=12;render();}
  topics.forEach(link => link.addEventListener('click', () => {topic=link.dataset.libraryTopic;limit=12;render();}));
  query.addEventListener('input', () => {limit=12;render();});
  format.addEventListener('change', () => {limit=12;render();});
  sort.addEventListener('change', () => {limit=12;render();});
  document.getElementById('library-clear').addEventListener('click',reset);
  document.querySelectorAll('[data-library-reset]').forEach(button=>button.addEventListener('click',reset));
  more.addEventListener('click',()=>{limit+=12;render();});
  document.querySelectorAll('[data-library-controls]').forEach(element=>{element.hidden=false;});
  render();
})();
