import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Templates',
  description: 'Python 3.12 项目模板',
  lang: 'zh-CN',
  base: process.env.DOCS_BASE || '/',
  themeConfig: {
    nav: [{ text: '首页', link: '/' }],
    outline: {
      label: '页面导航'
    },
    search: {
      provider: 'local'
    }
  }
})
