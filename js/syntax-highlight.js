(function () {
  function isDark() {
    return document.body.classList.contains('dark-mode') ||
      document.documentElement.classList.contains('dark-mode') ||
      localStorage.getItem('darkmode') === 'true';
  }

  function loadTheme() {
    var existing = document.getElementById('prism-theme');
    var href = 'https://cdn.jsdelivr.net/npm/prismjs@1/themes/' +
      (isDark() ? 'prism-tomorrow' : 'prism') + '.min.css';
    if (existing) {
      existing.href = href;
    } else {
      var link = document.createElement('link');
      link.id = 'prism-theme';
      link.rel = 'stylesheet';
      link.href = href;
      document.head.appendChild(link);
    }
  }

  loadTheme();

  var script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/prismjs@1/prism.min.js';
  script.setAttribute('data-manual', 'true');
  script.onload = function () {
    var autoloader = document.createElement('script');
    autoloader.src = 'https://cdn.jsdelivr.net/npm/prismjs@1/plugins/autoloader/prism-autoloader.min.js';
    autoloader.onload = function () {
      Prism.plugins.autoloader.languages_path =
        'https://cdn.jsdelivr.net/npm/prismjs@1/components/';
      Prism.highlightAll();
    };
    document.head.appendChild(autoloader);
  };
  document.head.appendChild(script);

  // 暗色模式切换时同步主题
  var mo = new MutationObserver(loadTheme);
  mo.observe(document.documentElement, { attributes: true, attributeFilter: ['class', 'data-theme'] });
  mo.observe(document.body, { attributes: true, attributeFilter: ['class'] });

  // Pjax 切页后重新高亮
  window.addEventListener('pjax:success', function () {
    if (window.Prism) Prism.highlightAll();
  });
})();
