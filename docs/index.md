# Templates

一个使用 Python 3.12 的项目模板，包含 Ruff、pre-commit 和 GitHub Actions 配置。

## Python 版本

项目使用 Python 3.12，版本约束在 `pyproject.toml` 中定义，
`.python-version` 用于选择本地解释器，Ruff 以 Python 3.12 为目标版本。

## 文档预览

文档使用基于 Vite 的 VitePress 构建，npm 配置、锁文件和依赖均位于 `docs/`。
在仓库根目录使用 Node.js 22 或更高版本执行：

```bash
cd docs
npm ci
npm run docs:dev
```

在浏览器中打开终端提示的本地地址即可预览。

## 文档构建与发布

在 `docs/` 目录执行：

```bash
npm run docs:build
npm run docs:preview
```

静态站点输出到 `docs/.vitepress/dist/`，该目录已被 Git 忽略。

在仓库的 **Settings → Pages → Build and deployment → Source** 中选择
**GitHub Actions**。更新 `main` 分支的文档、npm 依赖或文档 workflow 时，
GitHub Actions 会自动构建并发布文档。也可以在 Actions 页面手动运行“发布文档”。

Pull Request 只验证文档构建；发布仅在 `main` 分支运行。

发布 workflow 会根据仓库名称配置站点路径，适配 GitHub Pages 的项目站点。
本地构建默认使用 `/`；如需指定路径，可设置 `DOCS_BASE` 环境变量。
