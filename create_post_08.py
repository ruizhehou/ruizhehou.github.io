#!/usr/bin/env python3
import os

content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <!-- hexo-inject:begin --><!-- hexo-inject:end --><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=2">
<meta name="theme-color" content="#222">
<meta name="generator" content="Hexo 5.0.0">
  <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon-next.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16x16.png">
  <link rel="mask-icon" href="/images/apple-touch-icon-next.png" color="#222">
  <meta name="baidu-site-verification" content="true">
<link rel="stylesheet" href="/css/mobile-optimization.css">
<link rel="stylesheet" href="/css/dark-mode.css">
<link rel="stylesheet" href="/css/code-block.css">
<link rel="stylesheet" href="/css/main.css">
<link rel="stylesheet" href="//fonts.googleapis.com/css?family=Noto Serif SC:300,300italic,400,400italic,700,700italic|FuraCode Nerd Font:300,300italic,700,700italic&display=swap&subset=latin,latin-ext">
<link rel="stylesheet" href="/lib/font-awesome/css/all.min.css">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/gh/fancyapps/fancybox@3/dist/jquery.fancybox.min.css">
  <link rel="stylesheet" href="/lib/pace/pace-theme-minimal.min.css">
  <script src="/lib/pace/pace.min.js"></script>
<script id="hexo-configurations">
    var NexT = window.NexT || {};
    var CONFIG = {"hostname":"ruizhehou.github.io","root":"/","scheme":"Gemini","version":"7.8.0","exturl":true,"sidebar":{"position":"left","display":"post","padding":18,"offset":12,"onmobile":false},"copycode":{"enable":false,"show_result":false,"style":null},"back2top":{"enable":true,"sidebar":false,"scrollpercent":false},"bookmark":{"enable":true,"color":"#222","save":"auto"},"fancybox":true,"mediumzoom":false,"lazyload":true,"pangu":true,"comments":{"style":"tabs","active":"gitalk","storage":true,"lazyload":false,"nav":{"gitalk":{"order":-2}}},"algolia":{"hits":{"per_page":10},"labels":{"input_placeholder":"搜索...","hits_empty":"We did not find any results for search: ${query}","hits_stats":"${hints} results found in ${time} ms"}},"localsearch":{"enable":true,"trigger":"auto","top_n_per_article":1,"unescape":true,"preload":true},"motion":{"enable":true,"async":true,"transition":{"post_block":"fadeIn","post_header":"slideDownIn","post_body":"slideDownIn","coll_header":"slideLeftIn","sidebar":"slideUpIn"}},"path":"search.xml"};
  </script>
  <meta name="description" content="ACM 学习篇第八课：理解堆的原理与二叉堆的实现，掌握优先队列的常用操作，学会用堆高效解决 Top-K、合并有序链表、数据流中位数等经典问题。">
<meta property="og:type" content="article">
<meta property="og:title" content="ACM 学习篇 08：堆与优先队列">
<meta property="og:url" content="https://ruizhehou.github.io/2026/06/20/ACM%E5%AD%A6%E4%B9%A0%E7%AF%8708-%E5%A0%86%E4%B8%8E%E4%BC%98%E5%85%88%E9%98%9F%E5%88%97/index.html">
<meta property="og:site_name" content="侯瑞哲的博客">
<meta property="og:locale" content="zh_CN">
<meta property="article:published_time" content="2026-06-20T04:00:00.000Z">
<meta property="article:modified_time" content="2026-06-20T04:00:00.000Z">
<meta property="article:author" content="侯瑞哲">
<meta property="article:tag" content="数据结构与算法">
<meta property="article:tag" content="算法题目">
<meta name="twitter:card" content="summary">
<link rel="canonical" href="https://ruizhehou.github.io/2026/06/20/ACM%E5%AD%A6%E4%B9%A0%E7%AF%8708-%E5%A0%86%E4%B8%8E%E4%BC%98%E5%85%88%E9%98%9F%E5%88%97/index.html">
<script id="page-configurations">
  CONFIG.page = {"sidebar":"",isHome:false,isPost:true,lang:'zh-CN'};
</script>
  <title>ACM 学习篇 08：堆与优先队列 | 侯瑞哲的博客</title>
  <noscript><style>.use-motion .brand,.use-motion .menu-item,.sidebar-inner,.use-motion .post-block,.use-motion .pagination,.use-motion .comments,.use-motion .post-header,.use-motion .post-body,.use-motion .collection-header{opacity:initial;}.use-motion .site-title,.use-motion .site-subtitle{opacity:initial;top:initial;}.use-motion .logo-line-before i{left:initial;}.use-motion .logo-line-after i{right:initial;}</style></noscript>
</head>
<body itemscope itemtype="http://schema.org/WebPage">
  <div class="container use-motion">
    <div class="headband"></div>
    <header class="header" itemscope itemtype="http://schema.org/WPHeader">
      <div class="header-inner"><div class="site-brand-container">
  <div class="site-nav-toggle"><div class="toggle" aria-label="切换导航栏"><span class="toggle-line toggle-line-first"></span><span class="toggle-line toggle-line-middle"></span><span class="toggle-line toggle-line-last"></span></div></div>
  <div class="site-meta"><a href="/" class="brand" rel="start"><span class="logo-line-before"><i></i></span><span class="site-title">侯瑞哲的博客</span><span class="logo-line-after"><i></i></span></a></div>
  <div class="site-nav-right"><div class="toggle popup-trigger"><i class="fa fa-search fa-fw"></i></div></div>
</div>
<nav class="site-nav"><ul class="main-menu menu">
  <li class="menu-item menu-item-home"><a href="/" rel="section"><i class="fa fa-home fa-fw"></i>首页</a></li>
  <li class="menu-item menu-item-about"><a href="/about/" rel="section"><i class="fa fa-user fa-fw"></i>关于</a></li>
  <li class="menu-item menu-item-catalog"><a href="/catalog/" rel="section"><i class="fa fa-list fa-fw"></i>目录</a></li>
  <li class="menu-item menu-item-projects"><a href="/projects/" rel="section"><i class="fa fa-folder-open fa-fw"></i>项目</a></li>
  <li class="menu-item menu-item-search"><a href="javascript:;" class="popup-trigger"><i class="fa fa-search fa-fw"></i>搜索</a></li>
</ul></nav>
<div class="search-pop-overlay"><div class="popup search-popup"><div class="search-header"><span class="search-icon"><i class="fa fa-search"></i></span><div class="search-input-container"><input autocomplete="off" autocorrect="off" autocapitalize="off" placeholder="搜索..." spellcheck="false" type="search" class="search-input"></div><span class="popup-btn-close"><i class="fa fa-times-circle"></i></span></div><div id="search-result"><div id="no-result"><i class="fa fa-spinner fa-pulse fa-5x fa-fw"></i></div></div></div></div>
</div>
    </header>
    <main class="main">
      <div class="main-inner">
        <div class="content-wrap">
          <div class="content page posts-expand">
  <article itemscope itemtype="http://schema.org/Article" class="post-block" lang="zh-CN">
  <div class="post-header">
    <div class="post-meta-container"><div class="post-meta">
      <time itemprop="dateCreated" datetime="2026-06-20T12:00:00+08:00" content="2026-06-20">06-20</time>
    </div></div>
    <h1 class="post-title" itemprop="name headline">ACM 学习篇 08：堆与优先队列</h1>
  </div>

  <div class="post-body" itemprop="articleBody">

<p>上一篇讲了并查集，它擅长处理连通性和集合合并。今天来看另一个非常实用的数据结构：堆（Heap），它是实现优先队列最常见的方式。</p>

<h2 id="为什么需要堆">为什么需要堆</h2>

<p>想象一个场景：不断有新任务进来，每个任务有不同的优先级，你每次要挑出当前优先级最高的任务来做。</p>

<p>如果用普通数组或链表，每次取最大值都要遍历一遍，时间复杂度是 O(n)。如果用排序后的数组，每次插入要移动元素，也很慢。</p>

<p>堆就是为了解决这类"动态维护最值"的问题而生的：它能在 O(log n) 的时间内插入元素和取出最值。</p>

<h2 id="什么是二叉堆">什么是二叉堆</h2>

<p>二叉堆本质上是一棵<strong>完全二叉树</strong>，它用数组来存储，并且满足堆性质：</p>

<ul>
  <li><strong>大顶堆</strong>：每个节点的值都大于等于它的左右子节点的值；</li>
  <li><strong>小顶堆</strong>：每个节点的值都小于等于它的左右子节点的值。</li>
</ul>

<p>因为堆是完全二叉树，所以可以用数组紧凑地表示。如果根节点在下标 1 的位置，那么：</p>

<ul>
  <li>节点 i 的左子节点在 <code>2 * i</code>；</li>
  <li>节点 i 的右子节点在 <code>2 * i + 1</code>；</li>
  <li>节点 i 的父节点在 <code>i / 2</code>。</li>
</ul>

<h2 id="C++中的优先队列">C++ 中的优先队列</h2>

<p>C++ STL 提供了 <code>priority_queue</code>，默认是一个大顶堆：</p>

<pre><code class="language-cpp">priority_queue&lt;int&gt; maxHeap;  // 大顶堆
priority_queue&lt;int, vector&lt;int&gt;, greater&lt;int&gt;&gt; minHeap;  // 小顶堆
</code></pre>

<p>常用操作：</p>

<pre><code class="language-cpp">maxHeap.push(10);   // 插入元素，O(log n)
maxHeap.top();      // 取堆顶元素（最大值），O(1)
maxHeap.pop();      // 删除堆顶元素，O(log n)
maxHeap.size();     // 元素个数
maxHeap.empty();    // 是否为空
</code></pre>

<h2 id="手写一个最小堆">手写一个最小堆</h2>

<p>虽然 STL 已经提供了优先队列，但理解堆的内部实现对你很有帮助。下面手写一个小顶堆：</p>

<pre><code class="language-cpp">class MinHeap {
private:
    vector&lt;int&gt; heap;

    void swim(int k) {  // 上浮操作
        while (k &gt; 1 &amp;&amp; heap[k] &lt; heap[k / 2]) {
            swap(heap[k], heap[k / 2]);
            k /= 2;
        }
    }

    void sink(int k) {  // 下沉操作
        int n = heap.size() - 1;
        while (2 * k &lt;= n) {
            int j = 2 * k;
            if (j &lt; n &amp;&amp; heap[j + 1] &lt; heap[j]) j++;  // 选较小的子节点
            if (heap[k] &lt;= heap[j]) break;
            swap(heap[k], heap[j]);
            k = j;
        }
    }

public:
    MinHeap() { heap.push_back(0); }  // 从下标1开始使用

    void push(int x) {
        heap.push_back(x);
        swim(heap.size() - 1);
    }

    int top() {
        return heap[1];
    }

    void pop() {
        int n = heap.size() - 1;
        swap(heap[1], heap[n]);
        heap.pop_back();
        sink(1);
    }

    bool empty() {
        return heap.size() == 1;
    }
};
</code></pre>

<p>核心思路只有两个：</p>

<ul>
  <li><strong>上浮 swim</strong>：新元素放到末尾，然后一路向上与父节点比较，如果违反堆性质就交换；</li>
  <li><strong>下沉 sink</strong>：堆顶元素与末尾交换后弹出，然后从顶部一路向下，与较小的子节点比较交换。</li>
</ul>

<h2 id="典型题数组中第K大的元素">典型题：数组中第 K 大的元素</h2>

<p>给一个未排序的数组，找出其中第 K 大的元素。用小顶堆非常优雅：</p>

<pre><code class="language-cpp">int findKthLargest(vector&lt;int&gt;&amp; nums, int k) {
    priority_queue&lt;int, vector&lt;int&gt;, greater&lt;int&gt;&gt; minHeap;

    for (int x : nums) {
        minHeap.push(x);
        if (minHeap.size() &gt; k) {
            minHeap.pop();  // 只保留最大的 k 个元素
        }
    }
    return minHeap.top();
}
</code></pre>

<p>思路：维护一个大小为 k 的小顶堆。堆顶就是当前已遍历元素中第 k 大的那个。遍历完后，堆顶就是答案。时间复杂度 O(n log k)。</p>

<h2 id="典型题合并K个有序链表">典型题：合并 K 个有序链表</h2>

<p>给 k 个有序链表，把它们合并成一条有序链表。这是堆的经典应用：</p>

<pre><code class="language-cpp">struct Compare {
    bool operator()(ListNode* a, ListNode* b) {
        return a-&gt;val &gt; b-&gt;val;  // 小顶堆
    }
};

ListNode* mergeKLists(vector&lt;ListNode*&gt;&amp; lists) {
    priority_queue&lt;ListNode*, vector&lt;ListNode*&gt;, Compare&gt; minHeap;

    for (auto head : lists) {
        if (head) minHeap.push(head);
    }

    ListNode dummy(0);
    ListNode* tail = &amp;dummy;

    while (!minHeap.empty()) {
        ListNode* cur = minHeap.top();
        minHeap.pop();
        tail-&gt;next = cur;
        tail = cur;
        if (cur-&gt;next) minHeap.push(cur-&gt;next);
    }

    return dummy.next;
}
</code></pre>

<p>思路：每个链表先取一个头节点放入小顶堆，每次取出最小的接到结果里，然后把该节点的下一个节点重新入堆。总时间复杂度 O(N log k)，N 是所有节点总数。</p>

<h2 id="典型题数据流的中位数">典型题：数据流的中位数</h2>

<p>不断有数据流入，每次要快速返回当前所有数据的中位数。用两个堆来做：</p>

<pre><code class="language-cpp">class MedianFinder {
private:
    priority_queue&lt;int&gt; maxHeap;           // 存较小的一半，堆顶是这一半的最大值
    priority_queue&lt;int, vector&lt;int&gt;, greater&lt;int&gt;&gt; minHeap;  // 存较大的一半，堆顶是这一半的最小值

public:
    void addNum(int num) {
        maxHeap.push(num);
        minHeap.push(maxHeap.top());
        maxHeap.pop();

        if (maxHeap.size() &lt; minHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }

    double findMedian() {
        if (maxHeap.size() &gt; minHeap.size()) {
            return maxHeap.top();
        }
        return (maxHeap.top() + minHeap.top()) / 2.0;
    }
};
</code></pre>

<p>思路：大顶堆存较小的一半，小顶堆存较大的一半。保持大顶堆的元素个数等于或比小顶堆多一个，中位数就在两个堆顶之间。插入 O(log n)，查询 O(1)。</p>

<h2 id="堆的其他应用">堆的其他应用</h2>

<ul>
  <li><strong>Top-K 问题</strong>：从海量数据中找最大的 K 个或最小的 K 个；</li>
  <li><strong>堆排序</strong>：先建堆，然后不断弹出堆顶，时间复杂度 O(n log n)；</li>
  <li><strong>Dijkstra 最短路径</strong>：用小顶堆选下一个距离最小的节点；</li>
  <li><strong>Prim 最小生成树</strong>：用小顶堆选下一条权值最小的边；</li>
  <li><strong>任务调度</strong>：按优先级取出任务执行。</li>
</ul>

<h2 id="堆的易错点">堆的易错点</h2>

<ul>
  <li><strong>大顶堆还是小顶堆</strong>：不要搞反了，找 Top-K 大用小顶堆，找 Top-K 小用大顶堆；</li>
  <li><strong>自定义比较器</strong>：<code>priority_queue</code> 的比较器写法容易记反；</li>
  <li><strong>下标从 0 还是从 1 开始</strong>：手写堆时注意父节点和子节点的下标计算；</li>
  <li><strong>重复元素</strong>：堆允许重复元素，取出时要注意是否需要去重；</li>
  <li><strong>空间换时间</strong>：堆虽然速度快，但需要额外的数组空间。</li>
</ul>

<h2 id="什么时候用堆">什么时候用堆</h2>

<p>看到这些关键词，就可以考虑堆：</p>

<ul>
  <li>动态维护最大值或最小值；</li>
  <li>第 K 大、第 K 小、Top-K；</li>
  <li>合并多个有序序列；</li>
  <li>最短路径、最小生成树等图算法；</li>
  <li>需要按优先级处理任务。</li>
</ul>

<h2 id="这一篇先记住什么">这一篇先记住什么</h2>

<ul>
  <li>堆是一棵完全二叉树，用数组存储，满足堆性质；</li>
  <li>两个核心操作：上浮 swim 和下沉 sink；</li>
  <li>C++ 中 <code>priority_queue</code> 默认大顶堆，要小顶堆需指定 <code>greater&lt;T&gt;</code>；</li>
  <li>堆的插入和删除都是 O(log n)，取堆顶是 O(1)；</li>
  <li>经典应用：Top-K、合并 K 个有序链表、数据流中位数、Dijkstra。</li>
</ul>

<p>下一篇继续数据结构：二叉搜索树（BST）。它能在 O(log n) 的平均时间内完成查找、插入和删除，同时保持元素有序，是很多更高级数据结构的基础。</p>
  </div>

  <div class="post-footer-container">
    <div class="post-footer">
      <div class="post-tags">
          <a href="/tags/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/" rel="tag"><i class="fa fa-tag"></i> 数据结构与算法</a>
          <a href="/tags/%E7%AE%97%E6%B3%95%E9%A2%98%E7%9B%AE/" rel="tag"><i class="fa fa-tag"></i> 算法题目</a>
      </div>
      <nav class="post-nav">
        <div class="post-nav-next post-nav-item"></div>
        <span class="post-nav-divider"></span>
        <div class="post-nav-prev post-nav-item">
          <a href="/2026/06/19/ACM%E5%AD%A6%E4%B9%A0%E7%AF%8707-%E5%B9%B6%E6%9F%A5%E9%9B%86/" rel="prev" title="ACM 学习篇 07：并查集">
            ACM 学习篇 07：并查集 <i class="fa fa-chevron-right"></i>
          </a>
        </div>
      </nav>
    </div>
  </div>
  </article>
  </div>
  </div>

  <div class="toggle sidebar-toggle" role="button">
    <span class="toggle-line"></span><span class="toggle-line"></span><span class="toggle-line"></span>
  </div>
  <aside class="sidebar">
    <div class="sidebar-inner">
      <ul class="sidebar-nav motion-element">
        <li class="sidebar-nav-toc sidebar-nav-active" data-target="post-toc">文章目录</li>
        <li class="sidebar-nav-overview" data-target="site-overview">站点概览</li>
      </ul>
      <!--noindex-->
      <div class="post-toc-wrap sidebar-panel sidebar-panel-active">
        <div class="post-toc motion-element"><ol class="nav">
<li class="nav-item nav-level-2"><a class="nav-link" href="#为什么需要堆"><span class="nav-number">1.</span> <span class="nav-text">为什么需要堆</span></a></li>
<li class="nav-item nav-level-2"><a class="nav-link" href="#什么是二叉堆"><span class="nav-number">2.</span> <span class="nav-text">什么是二叉堆</span></a></li>
<li class="nav-item nav-level-2"><a class="nav-link" href="#C++中的优先队列"><span class="nav-number">3.</span> <span class="nav-text">C++ 中的优先队列</span></a></li>
<li class="nav-item nav-level-2"><a class="nav-link" href="#手写一个最小堆"><span class="nav-number">4.</span> <span class="nav-text">手写一个最小堆</span></a></li>
<li class="nav-item nav-level-2"><a class="nav-link" href="#典型题数组中第K大的元素"><span class="nav-number">5.</span> <span class="nav-text">典型题：数组中第 K 大的元素</span></a></li>
<li class="nav-item nav-level-2"><a class="nav-link" href="#典型题合并K个有序链表"><span class="nav-number">6.</span> <span class="nav-text">典型题：合并 K 个有序链表</span></a></li>
<li class="nav-item nav-level-2"><a class="nav-link" href="#典型题数据流的中位数"><span class="nav-number">7.</span> <span class="nav-text">典型题：数据流的中位数</span></a></li>
<li class="nav-item nav-level-2"><a class="nav-link" href="#堆的其他应用"><span class="nav-number">8.</span> <span class="nav-text">堆的其他应用</span></a></li>
<li class="nav-item nav-level-2"><a class="nav-link" href="#堆的易错点"><span class="nav-number">9.</span> <span class="nav-text">堆的易错点</span></a></li>
<li class="nav-item nav-level-2"><a class="nav-link" href="#什么时候用堆"><span class="nav-number">10.</span> <span class="nav-text">什么时候用堆</span></a></li>
<li class="nav-item nav-level-2"><a class="nav-link" href="#这一篇先记住什么"><span class="nav-number">11.</span> <span class="nav-text">这一篇先记住什么</span></a></li>
</ol></div>
      </div>
      <!--/noindex-->
      <div class="site-overview-wrap sidebar-panel">
        <div class="site-overview">
          <div class="site-author motion-element" itemprop="author" itemscope itemtype="http://schema.org/Person">
              <p class="site-author-name" itemprop="name">侯瑞哲</p>
              <div class="site-description motion-element" itemprop="description"></div>
          </div>
          <nav class="site-state motion-element">
            <div class="site-state-item site-state-posts">
              <a href="/archives/"><span class="site-state-item-count">263</span><span class="site-state-item-name">日志</span></a>
            </div>
            <div class="site-state-item site-state-categories">
              <a href="/categories/"><span class="site-state-item-count">0</span><span class="site-state-item-name">分类</span></a>
            </div>
            <div class="site-state-item site-state-tags">
              <a href="/tags/"><span class="site-state-item-count">39</span><span class="site-state-item-name">标签</span></a>
            </div>
          </nav>
        </div>
      </div>
    </div>
  </aside>
  <div id="sidebar-dimmer"></div>
      </div>
    </main>
    <footer class="footer">
      <div class="footer-inner">
        <div class="copyright">&copy; <span itemprop="copyrightYear">2026</span> <span class="with-love"><i class="fa fa-heart"></i></span> <span class="author" itemprop="copyrightHolder">侯瑞哲</span></div>
        <div class="powered-by">由 <a href="https://hexo.io/" class="theme-link" rel="noopener" target="_blank">Hexo</a> &amp; <a href="https://theme-next.org/" class="theme-link" rel="noopener" target="_blank">NexT.Gemini</a> 强力驱动</div>
      </div>
    </footer>
  </div>
  <script src="/lib/anime.min.js"></script>
  <script src="/lib/velocity/velocity.min.js"></script>
  <script src="/lib/velocity/velocity.ui.min.js"></script>
  <script src="//cdn.jsdelivr.net/npm/jquery@3/dist/jquery.min.js"></script>
  <script src="//cdn.jsdelivr.net/gh/fancyapps/fancybox@3/dist/jquery.fancybox.min.js"></script>
  <script src="//cdn.jsdelivr.net/npm/lozad@1/dist/lozad.min.js"></script>
  <script src="//cdn.jsdelivr.net/npm/pangu@4/dist/browser/pangu.min.js"></script>
  <script src="/lib/reading-progress/reading-progress.js"></script>
  <script src="/js/utils.js"></script>
  <script src="/js/motion.js"></script>
  <script src="/js/schemes/pisces.js"></script>
  <script src="/js/next-boot.js"></script>
  <script src="/js/bookmark.js"></script>
  <script src="/lib/pjax/pjax.min.js"></script>
  <script src="/js/search/algolia-search.js"></script>
  <script src="/js/reading-progress/reading-progress.js"></script>
  <script src="/js/related-posts.js"></script>
  <script src="/js/dark-mode-toggle.js"></script>
  <script src="/js/local-search.js"></script>
  <script>
var pjax = new Pjax({selectors:['head title','#page-configurations','.content-wrap','.post-toc-wrap','.languages','#pjax'],switches:{'.post-toc-wrap':Pjax.switches.innerHTML},analytics:false,cacheBust:false,scrollTo:!CONFIG.bookmark.enable});
window.addEventListener('pjax:success',()=>{document.querySelectorAll('script[data-pjax],script#page-configurations,#pjax script').forEach(element=>{var code=element.text||element.textContent||element.innerHTML||'';var script=document.createElement('script');script.type='text/javascript';script.text=code;document.body.appendChild(script);});});
  </script>
<script src="/js/syntax-highlight.js"></script>
<script src="/js/comments.js"></script>
</body>
</html>
"""

os.makedirs('/Users/bytedance/IdeaProjects/ruizhehou.github.io/2026/06/20/ACM学习篇08-堆与优先队列', exist_ok=True)
with open('/Users/bytedance/IdeaProjects/ruizhehou.github.io/2026/06/20/ACM学习篇08-堆与优先队列/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('File created successfully!')
