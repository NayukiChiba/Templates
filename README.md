# Templates

我的 Python 3.12 项目简单模板。

项目限定使用 Python 3.12，`.python-version`、Ruff 和 pre-commit 配置与之保持一致。

## 文档

文档源码位于 `docs/`，使用基于 Vite 的 VitePress 构建。
文档的 npm 配置、锁文件和依赖均位于 `docs/`。
安装 Node.js 22 或更高版本后，在仓库根目录执行：

```bash
cd docs
npm ci
npm run docs:dev
```

在 `docs/` 目录构建检查：`npm run docs:build`，构建后预览：`npm run docs:preview`。

首次发布前，在仓库 **Settings → Pages → Build and deployment → Source** 中选择
**GitHub Actions**。之后更新 `main` 分支的文档或相关配置会自动发布到 GitHub Pages；
Pull Request 会检查文档构建，也可以在 Actions 页面手动运行“发布文档” workflow。
