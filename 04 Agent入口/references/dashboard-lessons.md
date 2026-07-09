# 看板链接问题：完整排查与最终方案

## 问题

文境看板 HTML 需要在 Obsidian 中渲染深色卡片布局，且链接可点击跳转到 Vault 内文件。

## 尝试记录（7 次，全部失败 → 最终切换全局方案）

### 1. onclick + obsidian:// → HTML Viewer
- `onclick="window.open('obsidian://open?...')"`
- ❌ 所有 onclick 被剥离，window.open 被阻断

### 2. 纯 `<a href="obsidian://...">` → HTML Viewer
- `<a href="obsidian://open?vault=VAULT&file=PATH">`
- ❌ 沙箱阻断自定义协议

### 3. obsidian://open?path=绝对路径 → HTML View Plus
- `<a href="obsidian://open?path=E:\文境vault\...">`
- ❌ 双重 URL 编码导致路径错乱；修正后仍被沙箱阻断

### 4. obsidian://open?file=PATH（无 vault 参数）
- ❌ "vault not found"

### 5. Custom Frames 插件
- 调研后放弃——所有 iframe 类插件沙箱限制相同

### 6. CSS Snippet + Markdown 看板
- 用 `.obsidian/snippets/` 美化 MD 页面
- ❌ 字体/间距与 Obsidian 默认样式冲突严重，颜值不可接受

### 7. HTML 看板（颜值） + Markdown 导航（跳转）
- `文境看板.html` 看数据 + `文境导航.md` wiki 跳转
- ⚠️ 能用但不优雅——需开两个文件

## 最终方案

**浏览器打开 HTML 看板。**

核心发现：`obsidian://` 是操作系统级协议处理器。浏览器不受 Obsidian 插件沙箱限制，能正常触发跳转。但测试后发现 Vault 名称匹配、路径编码等问题仍不稳定——最终放弃了 HTML 链接跳转，看板专注可视化，导航回归 Obsidian 原生方式。

| 组件 | 工具 | 状态 |
|------|------|------|
| 文境看板.html | 浏览器 | ✅ 深色主题完美渲染 |
| 文境速览.html | 浏览器 | ✅ 三大数字 + 最新三卷 |
| 日常导航 | Obsidian 原生 | ✅ 文件树 / Ctrl+O / wiki 链接 |
| 数据刷新 | refresh_dashboard.py + Cron | ✅ 自动扫描 Vault |

## 经验教训

1. **Obsidian HTML 插件沙箱是硬限制**——不要试图绕过
2. **同一问题失败 3 次立即切换全局方案**——不反复修补同一思路
3. **看板的核心价值是「一眼看全局数据」，不是导航**
4. 双重编码是常见 URL 陷阱——`urllib.parse.quote()` 只调用一次
5. 新设备 Bootstrap 时 `setup_obsidian.py` 自动装 HTML View Plus + Startpage 等 7 个插件

## 后续演进：文境速览

在完整看板之外，新增了 `文境速览.html`——精简版仪表盘：

- 三张卡片：藏阁 Inbox / 典阁 Library / 成卷
- 每张卡片含子统计（摘/念/其他；创作体系/技术知识/法律客观）
- 底部「最新三卷」区域，动态显示最近 3 个卷的正文标题
- 同一刷新脚本 `refresh_dashboard.py` 统一更新两个看板
- 布局与完整看板一致的深色卡片风格

速览适合日常快速扫一眼，完整看板用于深入了解各层状态。

## 自动化 Obsidian 配置

Bootstrap 流程第 4 步新增 `scripts/setup_obsidian.py`：
- 自动写入推荐核心插件配置（18 项开启）
- 从 GitHub 下载 7 个社区插件（Startpage / HTML Viewer+ / Select Folder / Editing Toolbar / Full Calendar / Style Settings / PDF+）
- 自动启用社区插件模式
- 安装完成后提示用户重启 Obsidian
