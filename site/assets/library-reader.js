// Only generated, prefixed document headings are used as anchor destinations.
(() => {
  function reveal() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return; }
    if (!id.startsWith('doc-')) return;
    const target = document.getElementById(id);
    if (!target) return;
    for (let p = target.parentElement; p; p = p.parentElement) {
      if (p.tagName === 'DETAILS') p.open = true;
    }
  }
  addEventListener('hashchange', reveal);
  reveal();
})();
