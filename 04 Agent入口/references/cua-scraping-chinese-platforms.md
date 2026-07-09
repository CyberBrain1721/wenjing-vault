# cua-driver 自动化抓取中文平台（知乎/简书/百家号）

## 适用场景

知乎（zhuanlan.zhihu.com）、百家号（baijiahao.baidu.com）等中文内容平台使用强反爬机制（知乎的 zse-ck JS challenge、百家号需登录），curl 和 Browserbase 均被拦截。cua-driver 通过操控用户本地浏览器（已登录、有 cookie）绕过反爬。

## 前置条件

1. **cua-driver 已安装并运行**：`hermes computer-use install`（需 VPN 访问 GitHub）
2. **用户本地浏览器已登录目标平台**（知乎/百家号）
3. **用户默认浏览器为 Chrome 或 Edge**

## 完整抓取流程

### 1. 启动 cua-driver

```bash
hermes computer-use install        # 首次安装
cua-driver autostart kick          # 启动服务
hermes computer-use doctor         # 验证状态
```

### 2. 打开文章链接

```bash
start "" "https://zhuanlan.zhihu.com/p/33897990"
start "" "https://zhuanlan.zhihu.com/p/33960743"
# ... 批量打开所有 URL
```

### 3. 找到浏览器窗口

```bash
# 找到 Edge/Chrome 进程
echo '{}' | cua-driver get_accessibility_tree | python3 -c "..." 

# 列出窗口
echo '{"pid":<PID>}' | cua-driver list_windows
```

### 4. 循环提取（Ctrl+W 切换标签）

```bash
# 提取当前标签页全文
echo '{"pid":<PID>, "window_id":<WID>, "action":"get_text"}' | cua-driver page

# 关闭当前标签（CDP 连接自动切换到下一标签）
echo '{"pid":<PID>, "window_id":<WID>, "keys":["ctrl","w"], "delivery_mode":"foreground"}' | cua-driver hotkey
sleep 2

# 重复提取 + 关闭，直到所有文章抓完
```

### 5. 识别文章边界

`page get_text` 返回完整页面文本（含导航、评论区、推荐阅读）。文章正文位于标题行和「发布于 YYYY-MM-DD」行之间。

## 关键坑

- **`hotkey` 对 Chromium 窗口需 `delivery_mode: "foreground"`**，否则报 `Background delivery is not available for target window class 'Chrome_WidgetWin_1'`
- **`type_text` 后台模式不可靠**，`effect: "unverifiable"`，建议用 `click` + `set_value` 导航或 `start "" "URL"` 开新标签
- **`page` 工具锁定一个 CDP target**，必须用 Ctrl+W 关闭当前标签才能连接下一标签
- **Edge 窗口标题显示当前标签页标题**，可用来验证是哪个文章

## 降级链

```
curl (1次) → browser_navigate (1次) → cua-driver page get_text → 用户粘贴 → 放弃该篇
```

同一 URL 不要在同一个阻塞层级反复重试。
