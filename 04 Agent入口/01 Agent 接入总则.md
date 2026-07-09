# Agent 接入总则

## Purpose

本文件定义所有 Agent 接入文境时必须遵守的统一路径。

文境不依赖任何单一人工智能环境。

文境的本体是本地 Obsidian Vault。

Agent 只是进入 Vault 的协作者。

---

# Local-First Principle

文境必须优先作为本地系统存在。

任何创作者只要拥有本地 Vault 文件夹，就应能够在 Obsidian 中打开、阅读、维护和继续创作。

Agent 不得将文境解释为：

- 某个 AI 应用的项目
- 某个云端模型的工作区
- 某个自动化平台的流程
- 某个桌面 Agent 的专属插件

文境可以被不同 Agent 使用，但不属于任何 Agent。

---

# Unified Entry Principle

所有 Agent 的接入路径必须统一。

无论创作者使用：

- Codex 桌面版
- WorkBuddy 桌面版
- OpenClaw
- 其他本地或桌面 Agent

只要 Agent 接入文境 Vault，就必须首先读取：

```text
04 Agent入口/00 文境入口.md
```

随后按入口协议继续读取：

```text
04 Agent入口/02 共创入口（Creator Entry）.md
04 Agent入口/05 Workflow Index.md
```

未经协议触发，不得主动读取其他目录。

---

# Agent-Agnostic Rule

Agent 接入文境时，不得根据自身产品特性重写流程。

允许差异：

- 文件读写能力不同
- 上下文长度不同
- 是否能打开网页不同
- 是否能运行命令不同
- 是否能生成图片或视频不同

不允许差异：

- 改变入口顺序
- 跳过 Runtime 初始化
- 主动遍历整个 Vault
- 未经触发进入 Workflow
- 替创作者决定方向
- 把当前 Agent 的能力当作文境默认能力

---

# Collaboration Start

Agent 完成入口读取后，应只确认当前 Runtime 状态。

标准状态：

```text
Mode: Creator
Runtime: Conversation Runtime
Current Workflow: None
Status: Ready
```

此时 Agent 等待创作者提出任务。

如果创作者提出“收录 / 保存 / 整理 / 归档 / 复盘”等任务，再根据 `05 Workflow Index.md` 进入对应 Workflow。

---

# Boundary

文境的目标不是让 Agent 自动创作。

文境的目标是让不同 Agent 在同一个本地创作系统中，按照同一套协议协助创作者完成：

- 收集
- 理解
- 整理
- 共创
- 输出
- 复盘
- 归档

Agent 负责执行协议。

创作者负责决定意义。
