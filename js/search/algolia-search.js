/**
 * Algolia Search Integration
 * This file handles Algolia search functionality
 */

(function() {
  'use strict';

  if (typeof algoliasearch === 'undefined') {
    console.warn('Algolia search library not loaded');
    return;
  }

  var searchInput = document.querySelector('.search-input');
  var searchPopup = document.querySelector('.search-popup');
  var searchResult = document.getElementById('search-result');
  var noResult = document.getElementById('no-result');

  if (!searchInput || !searchPopup || !searchResult || !noResult) {
    return;
  }

  if (!searchInput || !searchPopup) {
    return;
  }

  // Initialize Algolia client
  var algoliaConfig = CONFIG.algolia || {};
  if (!algoliaConfig.appId || !algoliaConfig.apiKey || !algoliaConfig.indexName) {
    console.warn('Algolia configuration missing');
    return;
  }
  var client = algoliasearch(algoliaConfig.appId, algoliaConfig.apiKey);
  var index = client.initIndex(algoliaConfig.indexName);

  var search = function(query) {
    if (!query || query.trim() === '') {
      searchResult.innerHTML = '';
      noResult.style.display = 'block';
      return;
    }

    var hitsConfig = algoliaConfig.hits || {};
    index.search(query, {
      hitsPerPage: hitsConfig.per_page || 10
    }).then(function(content) {
      var hits = content.hits;
      var resultHTML = '';

      if (hits.length === 0) {
        searchResult.innerHTML = '';
        noResult.style.display = 'block';
        return;
      }

      noResult.style.display = 'none';

      hits.forEach(function(hit) {
        resultHTML += '<div class="search-result-item">';
        resultHTML += '<a href="' + hit.permalink + '">';
        resultHTML += '<h3>' + hit._highlightResult.title.value + '</h3>';
        if (hit._highlightResult.content) {
          resultHTML += '<p>' + hit._highlightResult.content.value + '</p>';
        }
        resultHTML += '</a>';
        resultHTML += '</div>';
      });

      searchResult.innerHTML = resultHTML;
    }).catch(function(error) {
      console.error('Algolia search error:', error);
    });
  };

  var debounce = function(func, wait) {
    var timeout;
    return function() {
      var context = this;
      var args = arguments;
      clearTimeout(timeout);
      timeout = setTimeout(function() {
        func.apply(context, args);
      }, wait);
    };
  };

  var debouncedSearch = debounce(search, 300);

  searchInput.addEventListener('input', function(e) {
    debouncedSearch(e.target.value);
  });

  // Handle search popup open/close
  var searchToggle = document.querySelector('.popup-trigger');
  var closeBtn = document.querySelector('.popup-btn-close');

  if (searchToggle) {
    searchToggle.addEventListener('click', function() {
      searchPopup.style.display = 'block';
      setTimeout(function() {
        searchInput.focus();
      }, 100);
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', function() {
      searchPopup.style.display = 'none';
    });
  }

  // Close on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && searchPopup.style.display === 'block') {
      searchPopup.style.display = 'none';
    }
  });

})();
