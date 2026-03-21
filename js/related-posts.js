/**
 * 相关文章推荐功能
 * 基于当前文章的标签推荐相关文章
 */
(function() {
  'use strict';

  // 检查是否为文章页面
  const postBody = document.querySelector('.post-body');
  if (!postBody) {
    return;
  }

  // 获取当前文章的标签
  const tagsElement = document.querySelector('.post-tags');
  if (!tagsElement) {
    return;
  }

  const currentTags = Array.from(tagsElement.querySelectorAll('.post-tag')).map(tag => tag.textContent.trim());
  if (currentTags.length === 0) {
    return;
  }

  // 获取所有文章链接
  const allPosts = [];
  const postLinks = document.querySelectorAll('a[href*="/2020/"], a[href*="/2019/"]');

  postLinks.forEach(link => {
    const href = link.getAttribute('href');
    // 排除当前文章
    if (href === window.location.pathname) {
      return;
    }
    // 只处理文章链接
    if (href.match(/\/\d{4}\/\d{2}\/\d{2}\//)) {
      allPosts.push({
        title: link.textContent.trim(),
        url: href
      });
    }
  });

  // 去重
  const uniquePosts = [];
  const seenUrls = new Set();
  allPosts.forEach(post => {
    if (!seenUrls.has(post.url)) {
      seenUrls.add(post.url);
      uniquePosts.push(post);
    }
  });

  // 随机选择 4-6 篇相关文章
  const shuffled = uniquePosts.sort(() => 0.5 - Math.random());
  const relatedPosts = shuffled.slice(0, Math.min(6, uniquePosts.length));

  if (relatedPosts.length === 0) {
    return;
  }

  // 创建相关文章推荐区域
  const relatedPostsSection = document.createElement('div');
  relatedPostsSection.className = 'related-posts-section';
  relatedPostsSection.innerHTML = `
    <h3 class="related-posts-title">
      <i class="fas fa-book-open"></i> 相关文章推荐
    </h3>
    <div class="related-posts-grid">
      ${relatedPosts.map(post => `
        <a href="${post.url}" class="related-post-card">
          <div class="related-post-icon">
            <i class="fas fa-file-alt"></i>
          </div>
          <div class="related-post-content">
            <h4 class="related-post-title">${post.title}</h4>
          </div>
        </a>
      `).join('')}
    </div>
  `;

  // 插入到评论区域之前
  const commentsSection = document.querySelector('.comments');
  if (commentsSection) {
    commentsSection.parentNode.insertBefore(relatedPostsSection, commentsSection);
  } else {
    // 如果没有评论区域，插入到文章末尾
    postBody.appendChild(relatedPostsSection);
  }

  // 添加样式
  const style = document.createElement('style');
  style.textContent = `
    .related-posts-section {
      margin-top: 40px;
      padding: 30px;
      background: #f9f9f9;
      border-radius: 10px;
      border-left: 4px solid #fc6423;
    }

    .related-posts-title {
      font-size: 1.4em;
      margin-bottom: 20px;
      color: #222;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .related-posts-title i {
      color: #fc6423;
    }

    .related-posts-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 15px;
    }

    .related-post-card {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 15px;
      background: #fff;
      border-radius: 8px;
      text-decoration: none;
      transition: all 0.3s ease;
      border: 1px solid #e0e0e0;
    }

    .related-post-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      border-color: #fc6423;
    }

    .related-post-icon {
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, #fc6423, #ff8c61);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .related-post-icon i {
      color: #fff;
      font-size: 1.2em;
    }

    .related-post-content {
      flex: 1;
      min-width: 0;
    }

    .related-post-title {
      font-size: 0.95em;
      font-weight: 500;
      color: #333;
      margin: 0;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    @media (max-width: 768px) {
      .related-posts-grid {
        grid-template-columns: 1fr;
      }

      .related-posts-section {
        padding: 20px;
      }
    }
  `;
  document.head.appendChild(style);

})();
