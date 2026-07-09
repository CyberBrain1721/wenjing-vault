# Inbox Standard

## Purpose

Inbox Standard 定义藏阁 Inbox 的文件位置、命名、YAML 字段和最小正文结构。

它服务于一个原则：

> 记录优先于整理，结构服务于再次发现。

---

# Inbox Path

所有收录内容默认进入：

```text
02 养境（知识）/01 藏阁/01 Inbox/
```

Inbox 不建立二级文件夹。

Agent 不得为了分类移动文件。

---

# File Naming

每条内容一个独立 Markdown 文件。

命名格式：

```text
【类型】标题.md
```

标题要求：

- 8-24 个中文字符优先
- 不使用日期作为主标题
- 不使用“未命名”“新建笔记”
- 避免冒号、斜杠、问号等路径敏感符号

重名时追加短编号：

```text
【念】知识库不是仓库-02.md
```

---

# Type Prefix

| 前缀 | type | 用途 |
| --- | --- | --- |
| 【念】 | 念 | 灵感、设定、创意、想法 |
| 【梦】 | 梦 | 梦境 |
| 【白】 | 白 | 对白、台词、原话 |
| 【摘】 | 摘 | 摘录、引用 |
| 【图】 | 图 | 图片、视觉灵感 |
| 【感】 | 感 | 情绪、氛围 |
| 【事】 | 事 | 新闻、现实事件 |
| 【随】 | 随 | 随笔、自由记录 |
| 【链】 | 链 | 外部链接、网页、仓库 |
| 【档】 | 档 | 本地文件、附件、资料包 |
| 【话】 | 话 | 对话片段、共创记录 |

如果不确定，使用 `【念】`。

---

# YAML Standard

所有 Inbox 笔记必须包含 YAML。

最小结构：

```yaml
---
status: 待讨论
type: 念
resource_policy: Snapshot
source_type: Thought
source: ""
captured_at: 2026-07-09
canonical: []
tags: []
related: []
---
```

字段约束：

| 字段 | 允许值/说明 |
| --- | --- |
| status | 待讨论 / 待发展 / 成卷 / 已归档 |
| type | 念 / 梦 / 白 / 摘 / 图 / 感 / 事 / 随 / 链 / 档 / 话 |
| resource_policy | Bookmark / Snapshot / Full Content / Archive |
| source_type | Thought / Quote / Link / Image / File / Conversation |
| source | URL、文件路径、来源说明，可空 |
| captured_at | YYYY-MM-DD |
| canonical | Knowledge Map 中的 Canonical 数组，可空 |
| tags | 内容标签数组，不表达状态 |
| related | 已确认相关笔记数组，可空 |

---

# Body Standard

正文建议结构：

```markdown
## 原始记录

保留创作者输入或资源原始描述。

## 摘要

仅在 Snapshot / Full Content / Archive 时填写。

## 为什么留下

记录触动点、问题、潜在用途。

## 后续可能

只列可能性，不做决定。
```

`Bookmark` 可只保留 `## 原始记录` 和 `## 为什么留下`。

---

# Status Rule

状态必须写在 YAML `status` 字段中。

不要用正文标签表达状态。

示例：

```yaml
status: 待讨论
```

内容标签可以放在 `tags` 字段。

示例：

```yaml
tags:
  - Obsidian
  - Agent
```

---

# Agent Boundary

Agent 可以：

- 创建新的 Inbox 笔记
- 建议标题
- 建议 YAML 字段
- 建议内容标签
- 建议可能关联

Agent 不得：

- 删除 Inbox 笔记
- 擅自移动 Inbox 笔记
- 擅自覆盖创作者原文
- 擅自把 `status` 改为 `成卷` 或 `已归档`
- 擅自建立 `related` 链接

所有状态推进都由创作者确认。
