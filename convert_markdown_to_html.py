#!/usr/bin/env python3
"""
Convert Markdown article to HTML format using ElasticSearch article as template
"""
import markdown
import re
from datetime import datetime

def parse_front_matter(content):
    """Parse YAML front matter from markdown content"""
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            front_matter = content[3:end]
            body = content[end+3:]
            return front_matter, body
    return None, content

def parse_yaml_front_matter(front_matter):
    """Simple YAML parser for front matter"""
    data = {}
    for line in front_matter.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            if key == 'tags' or key == 'categories':
                data[key] = [item.strip('- ') for item in value.split('\n') if item.strip()]
            else:
                data[key] = value
    return data

def markdown_to_html(markdown_content):
    """Convert markdown to HTML with code highlighting"""
    md = markdown.Markdown(extensions=['fenced_code', 'tables', 'codehilite'])
    html = md.convert(markdown_content)
    return html

def convert_headings(html_content):
    """Convert markdown headings to HTML with id attributes"""
    # Replace ## with h2, ### with h3, etc.
    html_content = re.sub(r'<h2>([^<]+)</h2>', lambda m: f'<h2 id="{m.group(1).replace(" ", "-")}">{m.group(1)}</h2>', html_content)
    html_content = re.sub(r'<h3>([^<]+)</h3>', lambda m: f'<h3 id="{m.group(1).replace(" ", "-")}">{m.group(1)}</h3>', html_content)
    return html_content

def convert_code_blocks(html_content):
    """Convert code blocks to proper format"""
    # Replace ```language with pre code blocks
    html_content = re.sub(r'<pre><code class="language-(\w+)">', r'<pre><code class="language-\1">', html_content)
    html_content = re.sub(r'<pre><code>', r'<pre><code class="language-bash">', html_content)
    return html_content

def generate_toc(html_content):
    """Generate table of contents from headings"""
    toc_items = []
    h2_count = 0

    for match in re.finditer(r'<h([23]) id="([^"]+)">([^<]+)</h\1>', html_content):
        level = int(match.group(1))
        anchor = match.group(2)
        text = match.group(3)

        if level == 2:
            h2_count += 1
            h3_count = 0
            toc_items.append(f'<li class="nav-item nav-level-2"><a class="nav-link" href="#{anchor}"><span class="nav-number">{h2_count}.</span> <span class="nav-text">{text}</span></a>')
        elif level == 2:
            h3_count += 1
            toc_items.append(f'<li class="nav-item nav-level-3"><a class="nav-link" href="#{anchor}"><span class="nav-number">{h2_count}.{h3_count}</span> <span class="nav-text">{text}</span></a>')

    return ''.join(toc_items)

def read_template():
    """Read the ElasticSearch article as template"""
    with open('/Users/houruizhe/IdeaSnapshots/ruizhehou.github.io/2026/03/28/ElasticSearch深度解析/index.html', 'r', encoding='utf-8') as f:
        return f.read()

def generate_article_html(front_matter_data, body_html, template):
    """Generate complete HTML article"""
    title = front_matter_data.get('title', '')
    date = front_matter_data.get('date', '')
    tags = front_matter_data.get('tags', [])
    date_str = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%m-%d') if date else ''

    # Generate tags HTML
    tags_html = '\n'.join([f'              <a href="/tags/{tag}/" rel="tag"><i class="fa fa-tag"></i> {tag}</a>' for tag in tags])

    # Generate meta tags
    description = body_html[:150].replace('<', '').replace('>', '') if body_html else ''

    # Replace placeholders in template
    html = template

    # Replace title
    html = re.sub(r'<title>.*?</title>', f'<title>{title} | 侯瑞哲的博客</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{description}">', html)
    html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title}">', html)
    html = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{description}">', html)
    html = re.sub(r'<h1 class="post-title"[^>]*>.*?</h1>', f'<h1 class="post-title" itemprop="name headline">\n      {title}\n  </h1>', html, flags=re.DOTALL)

    # Replace date
    html = re.sub(r'<time[^>]*>.*?</time>', f'<time itemprop="dateCreated" datetime="{date}+08:00" content="{date}">\n      {date_str}\n    </time>', html, flags=re.DOTALL)

    # Replace post body content
    html = re.sub(r'<div class="post-body"[^>]*>.*?</div>', f'<div class="post-body" itemprop="articleBody">\n\n    {body_html}\n\n  </div>', html, flags=re.DOTALL)

    # Replace tags
    html = re.sub(r'<div class="post-tags">.*?</div>', f'<div class="post-tags">\n{tags_html}\n          </div>', html, flags=re.DOTALL)

    # Update canonical URL
    url_title = title.replace(' ', '')
    html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://ruizhehou.github.io/2026/03/28/{url_title}/">', html)

    return html

def convert_file(input_path, output_path):
    """Convert a markdown file to HTML"""
    print(f"Converting {input_path}...")

    # Read markdown content
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse front matter
    front_matter, body = parse_front_matter(content)
    front_matter_data = parse_yaml_front_matter(front_matter) if front_matter else {}

    # Convert markdown to HTML
    body_html = markdown_to_html(body)
    body_html = convert_headings(body_html)

    # Read template
    template = read_template()

    # Generate complete HTML
    html = generate_article_html(front_matter_data, body_html, template)

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Converted to {output_path}")

if __name__ == '__main__':
    files = [
        ('/Users/houruizhe/IdeaSnapshots/ruizhehou.github.io/2026/03/28/Zookeeper深度解析/index.html',
         '/Users/houruizhe/IdeaSnapshots/ruizhehou.github.io/2026/03/28/Zookeeper深度解析/index.html'),
        ('/Users/houruizhe/IdeaSnapshots/ruizhehou.github.io/2026/03/28/ClickHouse深度解析/index.html',
         '/Users/houruizhe/IdeaSnapshots/ruizhehou.github.io/2026/03/28/ClickHouse深度解析/index.html'),
        ('/Users/houruizhe/IdeaSnapshots/ruizhehou.github.io/2026/03/28/分布式一致性算法/index.html',
         '/Users/houruizhe/IdeaSnapshots/ruizhehou.github.io/2026/03/28/分布式一致性算法/index.html'),
    ]

    for input_path, output_path in files:
        convert_file(input_path, output_path)
