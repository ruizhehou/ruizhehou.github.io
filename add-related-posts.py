#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在文章页面中添加相关文章推荐脚本
"""

import os
import re
from pathlib import Path

def add_related_posts_script(file_path):
    """在文件中添加相关文章推荐脚本"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否为文章页面（包含 post-block 类）
        if 'post-block' not in content:
            return False

        # 检查是否已经添加了脚本
        if 'related-posts.js' in content:
            return False

        # 在 reading-progress.js 之后添加脚本
        script_tag = '''  <script src="/js/related-posts.js"></script>
  <script src="/js/reading-progress.js"></script>

    </div><!-- hexo-inject:begin --><!-- hexo-inject:end -->
</body>'''

        # 替换 body 结束标签之前的部分
        old_pattern = '''  <script src="/js/reading-progress.js"></script>

    </div><!-- hexo-inject:begin --><!-- hexo-inject:end -->
</body>'''

        new_content = content.replace(old_pattern, script_tag)

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

    # 使用 os.walk 遍历所有目录，处理中文目录名
    updated_count = 0
    for root, dirs, files in os.walk(base_dir):
        # 跳过 lib 目录
        if 'lib' in root:
            continue

        for file in files:
            if file == 'index.html':
                file_path = Path(root) / file
                # 只处理日期目录下的文件（包含数字的目录）
                parent_dirs = file_path.relative_to(base_dir).parts
                # 检查是否在年份目录下（4位数字）
                if len(parent_dirs) >= 1 and parent_dirs[0].isdigit() and len(parent_dirs[0]) == 4:
                    if add_related_posts_script(file_path):
                        updated_count += 1

    print(f"\n✓ Related posts script added to {updated_count} article pages.")

if __name__ == '__main__':
    main()
