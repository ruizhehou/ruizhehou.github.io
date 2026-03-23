/**
 * Gitalk Comments Integration
 * This file handles Gitalk comment functionality
 */

(function() {
  'use strict';

  if (typeof Gitalk === 'undefined') {
    console.warn('Gitalk library not loaded');
    return;
  }

  var commentsContainer = document.querySelector('.comments');
  if (!commentsContainer) {
    return;
  }

  // Get page information
  var gitalkContainer = document.getElementById('gitalk-container');
  if (!gitalkContainer) {
    gitalkContainer = document.createElement('div');
    gitalkContainer.id = 'gitalk-container';
    commentsContainer.appendChild(gitalkContainer);
  }

  // Initialize Gitalk
  var gitalkConfig = CONFIG.gitalk || {};
  var gitalk = new Gitalk({
    clientID: gitalkConfig.client_id || '',
    clientSecret: gitalkConfig.client_secret || '',
    repo: gitalkConfig.repo || '',
    owner: gitalkConfig.owner || '',
    admin: gitalkConfig.admin || [],
    id: CONFIG.page ? CONFIG.page.path : window.location.pathname,
    language: gitalkConfig.language || 'zh-CN',
    distractionFreeMode: gitalkConfig.distractionFreeMode || false,
    perPage: gitalkConfig.perPage || 10,
    pagerDirection: gitalkConfig.pagerDirection || 'last',
    createIssueManually: gitalkConfig.createIssueManually || false,
    proxy: gitalkConfig.proxy || ''
  });

  gitalk.render('gitalk-container');

})();
