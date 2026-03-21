#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新导航菜单，添加关于和项目链接
"""

import os
import re
from pathlib import Path

# 定义新的导航菜单 HTML
NEW_NAV = '''        <li class="menu-item menu-item-home">

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
</nav>'''

# 定义旧的导航菜单 HTML（需要替换的部分）
OLD_NAV = '''        <li class="menu-item menu-item-home">

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
</nav>'''

def update_navigation(file_path):
    """更新单个文件的导航菜单"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否需要更新（有旧的导航菜单，没有新的）
        if 'menu-item-archives' in content and 'menu-item-about' not in content:
            # 替换导航菜单
            new_content = content.replace(OLD_NAV, NEW_NAV)

            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✓ Updated: {file_path}")
                return True
        return False
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False

def main():
    """主函数"""
    base_dir = Path('/Users/houruizhe/IdeaSnapshots/ruizhehou.github.io')

    # 查找所有需要更新的 index.html 文件
    updated_count = 0
    for file_path in base_dir.rglob('index.html'):
        # 跳过 lib 目录
        if 'lib' in str(file_path):
            continue

        if update_navigation(file_path):
            updated_count += 1

    print(f"\n✓ Navigation menu update completed! Updated {updated_count} files.")

if __name__ == '__main__':
    main()
