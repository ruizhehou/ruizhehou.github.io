#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在所有页面中添加代码块样式 CSS
"""

import os
from pathlib import Path

def add_code_block_css(file_path):
    """在文件中添加代码块样式 CSS"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否已经添加了样式
        if 'code-block.css' in content:
            return False

        # 在 main.css 之后添加代码块样式
        css_link = '''<link rel="stylesheet" href="/css/code-block.css">

<link rel="stylesheet" href="/css/main.css">'''

        # 替换 main.css 之前的部分
        old_pattern = '''<link rel="stylesheet" href="/css/main.css">'''

        new_content = content.replace(old_pattern, css_link)

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
                if add_code_block_css(file_path):
                    updated_count += 1

    print(f"\n✓ Code block CSS added to {updated_count} pages.")

if __name__ == '__main__':
    main()
