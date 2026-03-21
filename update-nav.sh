#!/bin/bash

# 批量更新导航菜单，添加关于和项目链接

# 定义新的导航菜单 HTML
NEW_NAV='        <li class="menu-item menu-item-home">

    <a href="/" rel="section"><i class="fa fa-home fa-fw"></i>首页</a>

  </li>
        <li class="menu-item menu-item-about">

    <a href="/about/" rel="section"><i class="fa fa-user fa-fw"></i>关于</a>

  </li>
        <li class="menu-item menu-item-projects">

    <a href="/projects/" rel="section"><i class="fa fa-folder-open fa-fw"></i>项目</a>

  </li>
        <li class="menu-item menu-item-archives">

    <a href="/archives/" rel="section"><i class="fa fa-archive fa-fw"></i>归档</a>

  </li>
      <li class="menu-item menu-item-search">
        <a role="button" class="popup-trigger"><i class="fa fa-search fa-fw"></i>搜索
        </a>
      </li>
  </ul>
</nav>'

# 定义旧的导航菜单 HTML（需要替换的部分）
OLD_NAV='        <li class="menu-item menu-item-home">

    <a href="/" rel="section"><i class="fa fa-home fa-fw"></i>首页</a>

  </li>
        <li class="menu-item menu-item-archives">

    <a href="/archives/" rel="section"><i class="fa fa-archive fa-fw"></i>归档</a>

  </li>
      <li class="menu-item menu-item-search">
        <a role="button" class="popup-trigger"><i class="fa fa-search fa-fw"></i>搜索
        </a>
      </li>
  </ul>
</nav>'

# 查找所有需要更新的 index.html 文件
find /Users/houruizhe/IdeaSnapshots/ruizhehou.github.io -name "index.html" -type f | while read file; do
    # 检查文件是否包含旧的导航菜单
    if grep -q "menu-item-archives" "$file" && ! grep -q "menu-item-about" "$file"; then
        echo "Updating: $file"
        # 使用 sed 进行替换
        sed -i '' "/menu-item-archives/,/<\/nav>/c\\
$NEW_NAV
" "$file"
    fi
done

echo "Navigation menu update completed!"
