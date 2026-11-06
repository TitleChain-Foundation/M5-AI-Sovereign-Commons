/* Public navigation only. No account, credential, authorization or private-data API. */
(() => {
  'use strict';
  const CONTRACT = {"foundation":"TitleChain Foundation","menus":{"commons":[{"id":"pathways","label":"Pathways","matchHashes":["#/","#/programs/","#/projects/"],"path":"#/","site":"commons"},{"id":"toolkits","label":"Toolkits","matchHashes":["#/tools/"],"path":"#/tools/","site":"commons"},{"id":"standards","label":"Research & Standards","matchHashes":["#/standards/"],"path":"#/standards/","site":"commons"},{"id":"funding","label":"Funding","matchHashes":["#/funding/"],"path":"#/funding/","site":"commons"},{"id":"search","label":"Search","matchHashes":["#/search/"],"path":"#/search/","site":"commons"},{"id":"documentation","label":"Documentation","matchPaths":["library/"],"path":"library/index.html","site":"commons"}],"labs":[{"id":"calculators","label":"Calculators","matchHashes":["#calculators"],"matchPaths":["calculator-families/"],"path":"calculator-families/","site":"labs"},{"id":"projects","label":"Projects","matchHashes":["#projects"],"matchPaths":["research/"],"path":"research/","site":"labs"},{"id":"observatory","label":"Observatory","matchPaths":["observatory/"],"path":"observatory/","site":"labs"},{"id":"simulations","label":"Simulations","matchPaths":["simulations/"],"path":"simulations/","site":"labs"},{"id":"inversion","label":"The Inversion","matchPaths":["inversion/"],"path":"inversion/","site":"labs"},{"id":"marketplace-reference","label":"Marketplace","matchPaths":["marketplace/"],"path":"marketplace/","site":"labs"},{"id":"research","label":"Papers","matchHashes":["#papers"],"matchPaths":["whitepapers/"],"path":"whitepapers/","site":"labs"},{"id":"about","label":"About","matchHashes":["#about"],"matchPaths":["about/"],"path":"about/","site":"labs"}]},"pageSections":{"commons":{"iwbe.html":[{"label":"Free M5-IAM","path":"#simulate"},{"label":"iSWE","path":"#iswe"},{"label":"Commons access","path":"#commons"},{"label":"Plan","path":"#plan"},{"label":"Underwrite iWBE","path":"#underwrite"}],"labs.html":[{"label":"Sovereign AI & Science","path":"#/programs/ai-science/","site":"commons"},{"label":"Calculator families","path":"#families"}],"marketplace.html":[{"label":"Services","path":"#services"},{"label":"Calculator research","path":"#/labs/calculators/","site":"commons"},{"label":"Member sign-in","url":"https://m5bank.app/"}]},"labs":{}},"schema":"m5-public-navigation/v1","sharedTools":[{"id":"freedom-office","label":"Freedom Office","matchPaths":["freedom-office.html"],"path":"freedom-office.html","site":"commons"},{"id":"marketplace","label":"M5-OpenAPI Marketplace","matchPaths":["marketplace.html"],"path":"marketplace.html","site":"commons"}],"sites":{"commons":{"label":"M5 Sovereign Commons","source":"https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons","switchLabel":"Commons","url":"https://commons.titlechainfoundation.org/"},"labs":{"label":"M5Labs","source":"https://gitlab.com/titlechain-foundation/m5labs","switchLabel":"M5Labs","url":"https://m5labs-8770fb.gitlab.io/"}},"version":"1.2.1"};
  const script = document.currentScript;
  const site = script?.dataset.m5Site;
  if (!CONTRACT.sites[site]) return;
  const root = new URL('../../', script.src);
  const assetRoot = new URL('.', script.src);
  const assetVersion = new URL(script.src).searchParams.get('v') || CONTRACT.version;
  let scheduled = false, open = false, contextKey = '';
  const config = CONTRACT.sites[site];
  const localPath = () => decodeURI(location.pathname.slice(root.pathname.length));
  function target(item) {
    if (item.url) return item.url;
    if (!item.site) return new URL(item.path, location.href).href;
    return new URL(item.path, item.site === site ? root : CONTRACT.sites[item.site].url).href;
  }
  function anchor(item) {
    const a = document.createElement('a');
    a.textContent = item.label;
    a.href = target(item);
    a.dataset.m5NavId = item.id || '';
    if (item.id === 'documentation') a.dataset.commonsLibrary = 'true';
    return a;
  }
  function navigation(label, items, className) {
    const nav = document.createElement('nav');
    nav.setAttribute('aria-label', label);
    nav.className = className;
    for (const item of items) nav.append(anchor(item));
    return nav;
  }
  function contentTarget() {
    const main = document.querySelector('main');
    return main?.querySelector('h1') ? main : document.querySelector('h1') || main;
  }
  function setOpen(value) {
    open = value;
    const header = document.getElementById('m5-shared-header');
    if (!header) return;
    header.dataset.open = String(open);
    const button = header.querySelector('button');
    button.setAttribute('aria-expanded', String(open));
    button.textContent = open ? 'Close menu' : 'Menu';
  }
  function create() {
    const header = document.createElement('header');
    header.id = 'm5-shared-header';
    header.dataset.navigationVersion = CONTRACT.version;
    header.dataset.m5Site = site;
    header.dataset.open = 'false';
    const inner = document.createElement('div');
    inner.className = 'm5-nav-inner';
    const row = document.createElement('div'); row.className = 'm5-nav-masthead';
    const brand = document.createElement('a'); brand.className = 'm5-nav-brand'; brand.href = root.href;
    const logo = document.createElement('img'); logo.src = new URL('mark.png?v='+assetVersion, assetRoot).href; logo.alt = ''; logo.width = 34; logo.height = 34;
    const words = document.createElement('span'), foundation = document.createElement('span'), title = document.createElement('strong');
    foundation.textContent = CONTRACT.foundation; title.textContent = config.switchLabel; brand.setAttribute('aria-label',CONTRACT.foundation+' '+config.switchLabel+' home'); words.append(foundation,title); brand.append(logo,words);
    const button = document.createElement('button'); button.type = 'button'; button.textContent = 'Menu'; button.setAttribute('aria-expanded','false'); button.setAttribute('aria-controls','m5-shared-links'); button.addEventListener('click',()=>setOpen(!open));
    row.append(brand,button);
    const links = document.createElement('div'); links.id = 'm5-shared-links';
    const utilities = document.createElement('div'); utilities.className = 'm5-nav-utilities';
    utilities.append(navigation('TitleChain sites',Object.entries(CONTRACT.sites).map(([key,value])=>({id:'site-'+key,label:value.switchLabel,site:key,path:''})),'m5-nav-sites'),navigation('Shared tools',CONTRACT.sharedTools,'m5-nav-tools'));
    links.append(utilities,navigation('Primary',CONTRACT.menus[site],'m5-nav-primary'));

    inner.append(row,links); header.append(inner);
    const skip = document.createElement('a'); skip.className = 'm5-nav-skip'; skip.textContent = 'Skip to content'; skip.href = '#main'; skip.addEventListener('click',e=>{e.preventDefault();const target=contentTarget();if(target){target.setAttribute('tabindex','-1');target.focus();target.scrollIntoView({block:'start'});}}); header.prepend(skip);
    header.addEventListener('click',e=>{if(e.target.closest('a'))setOpen(false);});
    header.addEventListener('keydown',e=>{if(e.key==='Escape'&&open){setOpen(false);button.focus();}});
    document.body.prepend(header);
    if (window.ResizeObserver) new ResizeObserver(entries=>{const value=Math.ceil(entries[0].contentRect.height)+'px';if(document.documentElement.style.getPropertyValue('--m5-navigation-height')!==value)document.documentElement.style.setProperty('--m5-navigation-height',value);}).observe(header);
    return header;
  }
  function matches(item) {
    if (item.site !== site) return false;
    const path = localPath(), hash = location.hash || '#/';
    const isRoot = path === '' || path === 'index.html';
    return (item.matchPaths || []).some(x=>x.endsWith('/')?path.startsWith(x):path===x) || (isRoot && (item.matchHashes || []).some(x=>x==='#/'?hash===x:hash===x||(x.endsWith('/')&&hash.startsWith(x))));
  }
  function apply() {
    scheduled = false;
    if (!document.body) return;
    const header = document.getElementById('m5-shared-header') || create();
    document.documentElement.dataset.m5NavigationVersion = CONTRACT.version;
    const content=contentTarget(); if(content){ if(!content.id)content.id='m5-page-content'; header.querySelector('.m5-nav-skip').href='#'+content.id; }
    for (const old of document.querySelectorAll('header')) {
      if (old === header || old.closest('#m5-shared-header') || old.closest('main,article,section,aside')) continue;
      if (old.querySelector('h1')) { old.setAttribute('role','region'); old.setAttribute('aria-label','Page introduction'); continue; } // A page title/hero is content, not a toolbar.
      const researchMetadata = localPath().startsWith('whitepapers/') && !old.querySelector('nav');
      const documentMetadata = site === 'commons' && localPath().startsWith('library/');
      if (researchMetadata || documentMetadata) { old.classList.add('m5-navigation-context-header'); old.setAttribute('role','region'); old.setAttribute('aria-label','Document context'); if(researchMetadata)for(const a of old.querySelectorAll('a'))a.classList.add('m5-navigation-replaced'); }
      else old.classList.add('m5-navigation-replaced');
      let frame = old.parentElement;
      while (frame && frame !== document.body) { if (frame.style.minHeight === '100vh') { frame.classList.add('m5-navigation-frame'); break; } frame = frame.parentElement; }
    }
    // Retire only the old skip hook and adapter-added header entry; the shared equivalents stay.
    for (const a of document.querySelectorAll('a[href="#main"]')) if (!header.contains(a) && a.textContent.trim()==='Skip to content') a.classList.add('m5-navigation-replaced');
    for (const a of document.querySelectorAll('a[data-commons-library]')) if (!header.contains(a) && a.closest('header.m5-navigation-replaced')) a.remove();
    for (const [key] of Object.entries(CONTRACT.sites)) {
      const a = header.querySelector('[data-m5-nav-id="site-'+key+'"]');
      if (key === site) a.setAttribute('aria-current','true'); else a.removeAttribute('aria-current');
    }
    for (const item of [...CONTRACT.sharedTools,...CONTRACT.menus[site]]) {
      const a = header.querySelector('[data-m5-nav-id="'+item.id+'"]');
      if (matches(item)) a.setAttribute('aria-current','page'); else a.removeAttribute('aria-current');
    }
    const sections = CONTRACT.pageSections[site][localPath()] || [];
    const key = JSON.stringify(sections);
    if (key !== contextKey) {
      contextKey = key;
      let context = document.getElementById('m5-page-navigation');
      if(!context){context=navigation('Page sections',[],'m5-nav-context');context.id='m5-page-navigation';header.after(context);}
      context.replaceChildren();
      if (sections.length) {const label=document.createElement('span');label.textContent='On this page';context.append(label);for(const item of sections)context.append(anchor(item));}
      context.hidden = !sections.length;
    }
  }
  function schedule() {if(!scheduled){scheduled=true;requestAnimationFrame(apply);}}
  new MutationObserver(schedule).observe(document.documentElement,{childList:true,subtree:true});
  addEventListener('hashchange',()=>{setOpen(false);schedule();});
  addEventListener('DOMContentLoaded',schedule);
  schedule();
})();
