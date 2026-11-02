/* Route only explicitly selected Commons documents; external and historical links stay intact. */
(() => {
  'use strict';
  const base = new URL('.', document.currentScript.src);
  const repository = '/TitleChain-Foundation/M5-AI-Sovereign-Commons/';
  let catalog, queued = false;
  function localTarget(value) {
    let url;
    try { url = new URL(value, location.href); } catch (_) { return null; }
    if (url.protocol !== 'https:' || url.hostname !== 'github.com' || !url.pathname.startsWith(repository)) return null;
    const match = url.pathname.slice(repository.length).match(/^(?:blob|tree)\/([^/]+)\/(.+)$/);
    if (!match || !['main', catalog.source_commit].includes(match[1]) || url.search) return null;
    let path, fragment;
    try { path = decodeURIComponent(match[2]); fragment = decodeURIComponent(url.hash.slice(1)); } catch (_) { return null; }
    path = catalog.aliases[path] || path;
    const item = catalog.entries.find(x => x.source_path === path && x.route);
    if (!item || (fragment && !item.anchors.includes(fragment))) return null;
    const target = new URL(item.route, base);
    if (fragment) target.hash = 'doc-' + fragment;
    return target.href;
  }
  function apply() {
    queued = false;
    if (!catalog) return;
    for (const link of document.querySelectorAll('a[href]')) {
      const target = localTarget(link.href);
      if (target) { link.href = target; link.removeAttribute('target'); }
    }
    const header = document.querySelector('header');
    let nav = document.querySelector('nav[aria-label="Primary"]') || document.querySelector('nav[aria-label="Commons"]') || document.querySelector('nav') || header?.querySelector('a')?.parentElement;
    if (!nav && header) {
      nav = document.createElement('nav');
      nav.setAttribute('aria-label', 'Documentation');
      nav.style.cssText = 'display:flex;flex-wrap:wrap;gap:16px;font-size:14px';
      header.append(nav);
    }
    if (nav && !nav.querySelector('[data-commons-library]')) {
      const first = nav.querySelector('a:last-of-type');
      const link = document.createElement('a');
      if (first) {
        link.className = first.className.split(/\s+/).filter(x => !['on', 'active', 'selected'].includes(x)).join(' ');
        link.style.cssText = first.style.cssText;
      }
      link.href = new URL('library/index.html', base).href;
      link.textContent = 'Documentation';
      link.dataset.commonsLibrary = 'true';
      nav.append(link);
    }
  }
  function schedule() { if (!queued) { queued = true; requestAnimationFrame(apply); } }
  fetch(new URL('library/source-map.json', base), {credentials: 'omit'})
    .then(r => { if (!r.ok) throw new Error('Documentation map unavailable'); return r.json(); })
    .then(data => {
      if (data.schema_version !== 1 || !Array.isArray(data.entries) || typeof data.aliases !== 'object') throw new Error('Invalid documentation map');
      // Routes are generated locally; refuse an injected external destination.
      for (const item of data.entries) {
        if (item.route && (!item.route.startsWith('library/') || item.route.includes('..') || new URL(item.route, base).origin !== base.origin)) throw new Error('Unsafe documentation route');
      }
      catalog = data;
      new MutationObserver(schedule).observe(document.documentElement, {childList: true, subtree: true});
      addEventListener('hashchange', schedule);
      schedule();
    }).catch(() => { /* Existing GitHub destinations remain usable if the map cannot load. */ });
})();
