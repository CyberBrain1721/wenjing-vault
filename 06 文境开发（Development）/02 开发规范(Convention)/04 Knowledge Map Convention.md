# Knowledge Map Convention

---

## 1. 目的

Knowledge Map Convention 用于规范所有 Development Agent 与 Creator Agent 在文境中使用 Knowledge Map 的方式。

Knowledge Map 是文境 Knowledge Layer 的统一知识地图，也是整个知识网络唯一的规范索引（Canonical Knowledge Index）。

Knowledge Map Convention 不保存知识，不参与知识创作，也不承担知识归档职责。

它仅规定 Agent 如何查询、引用、维护 Knowledge Map，以及如何利用 Knowledge Map 建立统一的知识网络。

---

## 2. 设计原则

Knowledge Map 的核心目标不是保存知识，而是统一知识语言。

随着 Inbox、成卷、归藏不断增长，Knowledge Map 应始终保持较小规模，仅维护长期稳定存在的核心知识节点。

任何 Agent 在建立知识连接时，都应优先复用已有 Canonical Node，而不是创建新的概念。

Knowledge Map 的增长速度应远低于整个知识库的增长速度。

知识可以不断增长，但 Knowledge Map 应保持稳定。

---

## 3. Agent 查询规范

所有 Agent 在执行 Inbox Capture、成卷整理或知识整理时，应首先查询 Knowledge Map。

Agent 的查询对象始终为 Knowledge Map，而不是整个 Vault。

Knowledge Map 是 Agent 在 Knowledge Layer 唯一允许主动遍历的知识索引。

Agent 不得主动扫描 Inbox、成卷、归藏或其他知识目录建立知识连接。

Knowledge Map 应作为所有知识引用行为的唯一入口。

---

## 4. Capture Workflow

任何内容进入文境知识网络之前，应执行以下流程：

```
Extract Concepts
↓
Query Knowledge Map
↓
Canonical Match
↓
Generate Metadata
↓
Generate Related Links
↓
Save
```

Agent 必须首先完成概念提取。随后查询 Knowledge Map。

若成功匹配 Canonical Node，则统一生成 Metadata 与 Related Links。

不得重新创建同义概念。

---

## 5. Canonical Match

Agent 查询时，应同时匹配以下字段：

- Canonical
- Alias

Canonical 为文境唯一标准名称。Alias 用于识别不同表达方式。

例如：

- Canonical：AI
- Alias：人工智能 / Artificial Intelligence / LLM（特定语境）

当 Alias 命中时，应统一引用 Canonical。

---

## 6. Metadata Generation

成功匹配 Canonical 后，Agent 应自动生成符合 Obsidian 规范的 Metadata。

Metadata 中的 Tags 应统一采用 Canonical 对应的 Tag。

例如：

```yaml
tags:
  - AI
```

不得使用 Alias 作为 Tag。

---

## 7. Related Link Generation

完成 Metadata 后，Agent 应自动建立对应 Canonical Node 的 Wikilink。

例如：

```
[[AI]]
```

Tag 用于 Obsidian 索引。Wikilink 用于知识网络。

任何进入 Inbox 的知识，如果未建立 Related Link，应视为 Capture 未完成。

---

## 8. New Canonical Proposal

若 Agent 未匹配到已有 Canonical Node，不得直接修改 Knowledge Map。

Agent 应生成新增建议，至少包含：

- 建议 Canonical
- 建议 Tag
- 建议 Alias
- 新增理由
- 与现有 Knowledge Map 的关系

等待创作者确认后，方可更新 Knowledge Map。

---

## 9. Forbidden

Agent 不得执行以下行为：

- 不得主动遍历整个 Vault
- 不得自动新增 Canonical Node
- 不得创建重复 Canonical
- 不得建立同义 Canonical
- 不得修改已有 Canonical
- 不得绕过创作者确认直接修改 Knowledge Map

---

## 10. 生命周期

Knowledge Map 是文境长期维护的知识基础设施。

Inbox、成卷、归藏可以持续增长。Knowledge Map 应保持长期稳定。

随着知识增长，Knowledge Map 的职责始终保持不变。

它定义的是整个文境知识网络共同使用的语言，而不是全部知识本身。
