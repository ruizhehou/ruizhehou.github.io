/**
 * Pjax - loads pages with AJAX and updates the URL
 * This file wraps the pjax library from /lib/pjax/pjax.js
 */

(function() {
  'use strict';

  // Load pjax from lib folder
  var script = document.createElement('script');
  script.src = '/lib/pjax/pjax.js';
  script.onload = function() {
    // Initialize pjax if available
    if (typeof $ !== 'undefined' && $.pjax) {
      $(document).pjax('a[target!=_blank]', '.content-wrap', {
        fragment: '.content-wrap',
        timeout: 5000
      });
    }
  };
  document.head.appendChild(script);

})();
