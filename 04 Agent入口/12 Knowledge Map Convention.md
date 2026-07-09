# Knowledge Map Convention

## Purpose

Knowledge Map Convention 定义 Agent 在 Capture、Organization、Output 等流程中如何使用 Knowledge Map。

Knowledge Map 不是目录，也不是全部知识库。

它是文境中长期稳定概念的 Registry。

---

# Canonical Principle

Agent 建立标签、Related、Canonical 引用前，应优先读取：

```text
02 养境（知识）/00 知识目录/00 知识地图Knowledge Map.md
```

Agent 只能引用 Knowledge Map 中已有的 Canonical。

Agent 不得因为一次对话、一次收录或一个临时项目，自行新增 Canonical。

---

# Matching Order

匹配顺序：

1. 精确匹配 Canonical
2. 匹配 Alias
3. 匹配 Notes 中的解释范围
4. 无匹配则留空

如果多个 Canonical 都可能匹配，只保留最确定的 1-3 个。

不确定时，宁可留空。

---

# Tag Rule

YAML `canonical` 使用 Canonical 名称。

YAML `tags` 使用内容标签。

示例：

```yaml
canonical:
  - 文境
  - Agent
tags:
  - Obsidian
  - 协议
```

Tag 不替代 Canonical。

Canonical 不替代内容标签。

---

# New Canonical Rule

Agent 发现可能需要新增 Canonical 时，只能提出建议：

```text
可能需要新增 Canonical：
名称：
理由：
可替代的已有 Canonical：
是否需要加入 Knowledge Map：等待创作者确认
```

未经确认，不写入 Knowledge Map。

---

# Related Rule

Agent 不主动建立 `related`。

只有当创作者确认两个内容之间存在明确关系时，才可写入 `related`。

Related 应优先使用 Obsidian wikilink：

```yaml
related:
  - "[[文境]]"
```

如果目标笔记尚不存在，暂不建立链接。

---

# Exit

Knowledge Map Check 完成后，Agent 返回当前 Workflow。

不得因为读取 Knowledge Map 而进入 Organization Workflow。
