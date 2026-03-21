#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在所有页面中添加深色模式功能
"""

import os
from pathlib import Path

def add_dark_mode(file_path):
    """在文件中添加深色模式功能"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否已经添加了深色模式
        if 'dark-mode.css' in content:
            return False

        # 在 code-block.css 之后添加深色模式 CSS
        css_link = '''<link rel="stylesheet" href="/css/dark-mode.css">
<link rel="stylesheet" href="/css/code-block.css">'''

        # 替换 code-block.css 之前的部分
        old_css_pattern = '''<link rel="stylesheet" href="/css/code-block.css">'''

        new_content = content.replace(old_css_pattern, css_link)

        # 检查是否需要添加脚本
        if 'dark-mode-toggle.js' not in new_content:
            # 在 body 结束标签之前添加脚本
            script_tag = '''  <script src="/js/dark-mode-toggle.js"></script>
  <script src="/js/related-posts.js"></script>'''

            # 替换 related-posts.js 之前的部分
            old_script_pattern = '''  <script src="/js/related-posts.js"></script>'''

            new_content = new_content.replace(old_script_pattern, script_tag)

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

    # 使用 os.walk 遍历所有目录
    updated_count = 0
    for root, dirs, files in os.walk(base_dir):
        # 跳过 lib 目录
        if 'lib' in root:
            continue

        for file in files:
            if file == 'index.html':
                file_path = Path(root) / file
                if add_dark_mode(file_path):
                    updated_count += 1

    print(f"\n✓ Dark mode added to {updated_count} pages.")

if __name__ == '__main__':
    main()
