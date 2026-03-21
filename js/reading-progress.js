/**
 * 文章阅读进度条
 * 显示当前文章的阅读进度
 */
(function() {
  'use strict';

  // 检查是否为文章页面
  if (!document.body.classList.contains('post-body')) {
    return;
  }

  // 创建进度条元素
  const progressBar = document.createElement('div');
  progressBar.className = 'reading-progress-bar';
  progressBar.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: linear-gradient(90deg, #fc6423, #ff8c61);
    width: 0%;
    z-index: 9999;
    transition: width 0.1s ease;
    box-shadow: 0 1px 3px rgba(252, 100, 35, 0.3);
  `;
  document.body.appendChild(progressBar);

  // 计算阅读进度
  function updateProgress() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const progress = (scrollTop / docHeight) * 100;

    progressBar.style.width = progress + '%';

    // 根据进度改变颜色
    if (progress > 90) {
      progressBar.style.background = 'linear-gradient(90deg, #52c41a, #73d13d)';
    } else if (progress > 50) {
      progressBar.style.background = 'linear-gradient(90deg, #1890ff, #40a9ff)';
    }
  }

  // 监听滚动事件
  let ticking = false;
  window.addEventListener('scroll', function() {
    if (!ticking) {
      window.requestAnimationFrame(function() {
        updateProgress();
        ticking = false;
      });
      ticking = true;
    }
  });

  // 初始化
  updateProgress();

})();
