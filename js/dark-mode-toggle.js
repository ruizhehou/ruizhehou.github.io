/**
 * 深色模式切换功能
 */
(function() {
  'use strict';

  // 创建深色模式切换按钮
  const toggleButton = document.createElement('button');
  toggleButton.className = 'dark-mode-toggle';
  toggleButton.setAttribute('aria-label', '切换深色模式');
  toggleButton.innerHTML = '<i class="fas fa-moon"></i>';
  document.body.appendChild(toggleButton);

  // 从 localStorage 获取保存的主题偏好
  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

  // 设置初始主题
  function setTheme(isDark) {
    if (isDark) {
      document.body.classList.add('dark-mode');
      toggleButton.innerHTML = '<i class="fas fa-sun"></i>';
      localStorage.setItem('theme', 'dark');
    } else {
      document.body.classList.remove('dark-mode');
      toggleButton.innerHTML = '<i class="fas fa-moon"></i>';
      localStorage.setItem('theme', 'light');
    }
  }

  // 初始化主题
  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    setTheme(true);
  } else {
    setTheme(false);
  }

  // 切换主题
  toggleButton.addEventListener('click', function() {
    const isDark = document.body.classList.contains('dark-mode');
    setTheme(!isDark);

    // 添加切换动画
    toggleButton.style.transform = 'rotate(360deg)';
    setTimeout(() => {
      toggleButton.style.transform = '';
    }, 300);
  });

  // 监听系统主题变化
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
    if (!localStorage.getItem('theme')) {
      setTheme(e.matches);
    }
  });

  // 平滑过渡
  document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';

})();
