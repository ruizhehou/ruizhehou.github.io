# 侯瑞哲的博客

这个仓库托管 [ruizhehou.github.io](https://ruizhehou.github.io/) 的静态站点文件。

当前 checkout 更接近发布后的站点产物，而不是完整的 Hexo 源码工程。大多数内容已经是生成后的 HTML，所以在这个仓库里改文章时，本质上是在直接维护线上静态文件。

## 目录结构

| 路径 | 说明 |
| --- | --- |
| `index.html` | 首页和近期文章入口。 |
| `catalog/index.html` | 手动整理的文章目录页。 |
| `search.xml` | 站内本地搜索索引。 |
| `2019/`, `2020/`, `2026/` | 按日期组织的文章目录，单篇文章通常有自己的 `index.html`。 |
| `archives/`, `page/`, `tags/`, `categories/` | 归档、分页、标签和分类等生成页。 |
| `css/`, `js/`, `images/`, `lib/` | 样式、脚本、图片和第三方前端资源。 |
| `add-*.py`, `update-nav.py`, `convert_markdown_to_html.py` | 用于维护站点 HTML 的辅助脚本。 |

## 编辑文章

新增或修改文章时，重点确认读者会经过的入口是否同步更新：

1. 修改文章目录下的页面，例如 `2026/06/16/<slug>/index.html`。
2. 如果文章需要出现在首页，同步更新 `index.html`。
3. 如果文章需要出现在目录页，同步更新 `catalog/index.html`。
4. 同步更新 `search.xml`，确保站内搜索能搜到最新内容。
5. 不要提交本地工具状态，`.DS_Store`、`.idea/`、`.claude/` 已在 `.gitignore` 中忽略。

如果只是修正一篇已存在文章的小段内容，通常只需要更新文章页和对应的 `search.xml` 条目。

## 校验

提交前至少跑：

```bash
git diff --check
xmllint --noout search.xml
git status --short
```

需要人工看页面效果时，可以在仓库根目录启动静态服务：

```bash
python3 -m http.server 4000
```

然后打开 `http://localhost:4000/` 或具体文章路径。

## 发布

站点从 `main` 分支发布。确认 diff 后提交并推送：

```bash
git add <changed-files>
git commit -m "<message>"
git push origin main
```

推送后 GitHub Pages 会使用最新的静态文件。
