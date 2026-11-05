# AutumnPants · 个人网站

> [qijunhao.com](https://qijunhao.com) — 戚俊皓的个人主页

## 简介

个人网站的唯一仓库，首页用 CardSwap 卡片交互进入各板块，板块以子目录形式挂在同一站点下。

## 目录

| 路径 | 板块 | 状态 |
|---|---|---|
| `/` | 首页（CardSwap 卡片总览） | 完成 |
| `/music/` | 音乐（听 / 赏 / 演 / 创） | 完成 |
| `/resume/` | 履历 | 完成 |
| `/contact/` | 联系 | 完成 |
| `/travel/` | 旅行 | 建设中 |
| `/photography/` | 摄影 | 建设中 |
| `/sports/` | 运动 | 建设中 |

## 共用资源

`style.css`、`common.js`、`gooey-nav.js`、`fonts/` 放在仓库根目录，所有板块的页面引用 `../` 指向根目录这一份，不再各自保留副本。

导航栏里未完工的板块（旅行 / 摄影 / 运动）会置灰并在下方标注「正在建设中」，规则写在 `gooey-nav.js` 的 `BUILDING_HREF`：

```js
var BUILDING_HREF = /^\/(travel|photography|sports)(\/|$)/i;
```

板块做完后，把对应的路径从这条正则里删掉即可恢复可点击。

## 构建

纯静态 HTML + CSS + JavaScript，通过 GitHub Pages 部署（分支 `main`，域名 `qijunhao.com`）。
