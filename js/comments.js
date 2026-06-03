(function () {
  function isDark() {
    return document.body.classList.contains('dark-mode') ||
      document.documentElement.classList.contains('dark-mode') ||
      document.documentElement.getAttribute('data-theme') === 'dark' ||
      localStorage.getItem('darkmode') === 'true';
  }

  function sendTheme(theme) {
    var iframe = document.querySelector('iframe.giscus-frame');
    if (iframe) {
      iframe.contentWindow.postMessage(
        { giscus: { setConfig: { theme: theme } } },
        'https://giscus.app'
      );
    }
  }

  function loadGiscus() {
    if (!window.CONFIG || !CONFIG.page || !CONFIG.page.isPost) return;

    var old = document.getElementById('giscus-container');
    if (old) old.remove();

    var container = document.createElement('div');
    container.id = 'giscus-container';
    container.style.cssText = 'margin: 40px 20px 0; padding-bottom: 20px;';

    var postBlock = document.querySelector('.post-block');
    if (!postBlock) return;

    var footer = postBlock.querySelector('.post-footer-container');
    if (footer) {
      footer.parentNode.insertBefore(container, footer.nextSibling);
    } else {
      postBlock.appendChild(container);
    }

    var s = document.createElement('script');
    s.src = 'https://giscus.app/client.js';
    s.setAttribute('data-repo', 'ruizhehou/ruizhehou.github.io');
    s.setAttribute('data-repo-id', 'R_kgDOPpGkhg');
    s.setAttribute('data-category', 'General');
    s.setAttribute('data-category-id', 'DIC_kwDOPpGkhs4C-Z3O');
    s.setAttribute('data-mapping', 'pathname');
    s.setAttribute('data-strict', '0');
    s.setAttribute('data-reactions-enabled', '1');
    s.setAttribute('data-emit-metadata', '0');
    s.setAttribute('data-input-position', 'bottom');
    s.setAttribute('data-theme', isDark() ? 'dark' : 'light');
    s.setAttribute('data-lang', 'zh-CN');
    s.setAttribute('crossorigin', 'anonymous');
    s.async = true;
    container.appendChild(s);
  }

  // 初始加载
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadGiscus);
  } else {
    loadGiscus();
  }

  // Pjax 导航后重新加载
  window.addEventListener('pjax:success', loadGiscus);

  // 暗色模式切换时同步 Giscus 主题
  var mo = new MutationObserver(function () {
    sendTheme(isDark() ? 'dark' : 'light');
  });
  mo.observe(document.documentElement, { attributes: true, attributeFilter: ['class', 'data-theme'] });
  mo.observe(document.body, { attributes: true, attributeFilter: ['class'] });
})();
