/**
 * Reading Progress Bar
 * Shows a progress bar at the top of the page indicating reading progress
 */

(function() {
  'use strict';

  // Create progress bar element
  var progressBar = document.createElement('div');
  progressBar.className = 'reading-progress-bar';
  progressBar.style.cssText = 'position: fixed; top: 0; left: 0; height: 3px; background: #fc6423; width: 0%; z-index: 9999; transition: width 0.1s ease;';
  document.body.appendChild(progressBar);

  // Update progress on scroll
  var updateProgress = function() {
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    var scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var progress = (scrollTop / scrollHeight) * 100;
    progressBar.style.width = progress + '%';
  };

  // Throttle scroll events
  var ticking = false;
  window.addEventListener('scroll', function() {
    if (!ticking) {
      window.requestAnimationFrame(function() {
        updateProgress();
        ticking = false;
      });
      ticking = true;
    }
  });

  // Initial update
  updateProgress();

})();
