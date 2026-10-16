/* Brief / Full reading mode. Local, dependency-free.
   Without JavaScript the full text is shown and the brief boxes stay hidden (see style.css). */
(function () {
  var KEY = 'wikiReadingMode';
  var root = document.documentElement;

  function stored() {
    try { var v = localStorage.getItem(KEY); return v === 'brief' || v === 'full' ? v : 'full'; }
    catch (e) { return 'full'; }
  }
  function apply(mode) {
    root.classList.toggle('mode-brief', mode === 'brief');
    root.classList.toggle('mode-full', mode === 'full');
  }

  apply(stored());  // runs in <head>, before first paint

  document.addEventListener('DOMContentLoaded', function () {
    var bar = document.getElementById('reading-bar');
    var bBrief = document.getElementById('mBrief');
    var bFull = document.getElementById('mFull');
    if (!bar || !bBrief || !bFull) return;
    bar.hidden = false;

    var sections = Array.prototype.slice.call(document.querySelectorAll('details.acc'));

    function setMode(mode, save) {
      apply(mode);
      bBrief.setAttribute('aria-pressed', mode === 'brief');
      bFull.setAttribute('aria-pressed', mode === 'full');
      if (save) { try { localStorage.setItem(KEY, mode); } catch (e) { /* storage blocked */ } }
    }
    setMode(stored(), false);
    bBrief.addEventListener('click', function () { setMode('brief', true); });
    bFull.addEventListener('click', function () { setMode('full', true); });

    document.getElementById('expandAll').addEventListener('click', function () {
      sections.forEach(function (d) { d.open = true; });
    });
    document.getElementById('collapseAll').addEventListener('click', function () {
      sections.forEach(function (d) { d.open = false; });
    });

    // Open the section that contains a link target. A target hidden by Brief mode
    // switches the page to Full so that the anchor lands on visible text.
    function reveal(hash) {
      var id = decodeURIComponent(hash.slice(1));
      var target = id && document.getElementById(id);
      if (!target) return false;
      var d = target.closest('details');
      while (d) { d.open = true; d = d.parentElement && d.parentElement.closest('details'); }
      if (root.classList.contains('mode-brief') && target.getClientRects().length === 0) {
        setMode('full', false);  // temporary: the stored preference is unchanged
      }
      target.scrollIntoView();
      return true;
    }
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a[href^="#"]');
      if (a && a.getAttribute('href').length > 1 && reveal(a.getAttribute('href'))) {
        history.replaceState(null, '', a.getAttribute('href'));
        e.preventDefault();
      }
    });
    if (location.hash) { setTimeout(function () { reveal(location.hash); }, 0); }

    window.addEventListener('beforeprint', function () {
      sections.forEach(function (d) { d.open = true; });
    });
  });
})();
