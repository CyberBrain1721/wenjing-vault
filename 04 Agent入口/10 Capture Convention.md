# Capture Convention

## Purpose

Capture Convention 定义 Agent 在文境中执行“收录 / 保存 / 记录下来 / 加入 Inbox / Capture / 保存到藏阁”时必须遵守的最小流程。

Capture 的目标不是立刻整理知识，也不是立刻生成作品。

Capture 的目标是：

> 将外部输入登记为文境中可再次引用、可追踪、可回到来源的 Resource。

---

# Runtime Boundary

进入 Capture Workflow 后，Agent 仅允许处理本次创作者明确提供或指定的内容。

Agent 不得：

- 主动遍历整个 Vault
- 主动读取全部 Inbox
- 主动判断该内容是否值得成卷
- 主动把内容改写成成品
- 主动建立双向链接
- 主动移动、删除或覆盖已有文件

Agent 可以：

- 为本次输入建立 Resource Registration
- 建议文件标题
- 建议类型、状态和内容标签
- 根据 Knowledge Map 建议 Canonical Related
- 按创作者选择的 Resource Policy 保存 Payload

---

# Capture Pipeline

每次 Capture 必须按以下顺序执行。

## 1. Input Identification

先判断输入类型：

| 类型 | 判断标准 | 示例 |
| --- | --- | --- |
| Thought | 创作者自己的念头 | 一个突然出现的想法 |
| Quote | 摘录、引用、句子 | 文章中的一段话 |
| Link | 外部网页或仓库链接 | GitHub、文章、视频链接 |
| Image | 图片或视觉素材 | 截图、封面、参考图 |
| File | 本地文件或附件 | PDF、Markdown、视频 |
| Conversation | 当前对话中的共创内容 | 一段讨论、一个判断 |

如果输入类型不确定，先按 `Thought` 保存，不追问。

---

## 2. Resource Registration

任何 Capture 都必须先完成 Resource Registration。

Resource Registration 是最小登记，不等于全文保存。

建议 YAML：

```yaml
---
status: 待讨论
type: 念
resource_policy: Bookmark
source_type: Thought
source: ""
captured_at: 2026-07-09
canonical:
  - 文境
tags:
  - 创作
related: []
---
```

字段说明：

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| status | 是 | 默认 `待讨论` |
| type | 是 | 使用 Inbox Standard 的类型前缀 |
| resource_policy | 是 | Bookmark / Snapshot / Full Content / Archive |
| source_type | 是 | Thought / Quote / Link / Image / File / Conversation |
| source | 否 | URL、文件路径、来源说明 |
| captured_at | 是 | 收录日期 |
| canonical | 否 | 来自 Knowledge Map 的标准概念 |
| tags | 否 | 内容标签，不表达状态 |
| related | 否 | 仅保存已确认关联 |

---

## 3. Resource Policy

Agent 应根据创作者输入或默认规则选择 Resource Policy。

如果创作者没有指定，默认使用 `Snapshot`。

| Policy | 保存范围 | 适用场景 |
| --- | --- | --- |
| Bookmark | 仅保存来源、标题、简短说明 | 链接、仓库、稍后再读 |
| Snapshot | 保存摘要、关键点、为什么值得留下 | 默认策略 |
| Full Content | 保存正文或完整可读文本 | 创作者明确要求保存全文 |
| Archive | 保存正文、图片、附件或本地副本 | 创作者明确要求归档 |

Resource Policy 只决定 Payload 的保存范围，不改变 Resource Registration。

---

## 4. Knowledge Map Check

保存前，Agent 应读取 Knowledge Map，并尝试匹配已有 Canonical Node。

原则：

- 优先复用已有 Canonical。
- 只建议，不新增。
- 新增 Canonical 必须由创作者确认。
- 不因为一次收录新增长期概念。

如果没有匹配项，`canonical` 可以留空。

---

## 5. Inbox Save

所有 Capture 默认保存到：

```text
02 养境（知识）/01 藏阁/01 Inbox/
```

文件命名遵守 `11 Inbox Standard.md`。

---

# Output Format

Capture 完成后，Agent 只返回：

```text
已收录：
文件：
Policy：
Canonical：
下一状态：
```

不得在 Capture 结束时继续扩写、整理或进入正文阶段。

---

# Exit

完成保存后，立即退出 Capture Workflow。

恢复：

```text
Runtime: Conversation Runtime
Current Workflow: None
```
