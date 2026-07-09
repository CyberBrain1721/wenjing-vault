# Inbox Standard

Version: 1.0
Status: Draft
Category: Development Convention

---

## 1. Purpose

Inbox Standard 定义 Capture Workflow 的统一输出格式。

任何资源经过 Capture Workflow 后，最终生成的 Inbox 文档必须符合本规范。

本规范旨在保证不同来源、不同类型、不同 Resource Policy 所生成的 Inbox 文档具有一致的结构，以确保长期维护、知识检索、AI 理解以及后续 Workflow 的稳定运行。

Inbox Standard 不负责定义 Capture 流程，不负责定义 Resource Policy，也不负责定义 Knowledge Mapping。

上述职责分别由《Capture Convention》、《Resource Policy Standard》以及《Knowledge Map Convention》负责。

---

## 2. Scope

本规范适用于所有通过 Capture Workflow 创建的 Inbox 文档。

包括但不限于：

- Web 页面
- 微信公众号
- GitHub Repository
- PDF
- YouTube
- 图片
- 文本
- Creator 输入内容
- AI 自动生成内容

所有资源均应遵循统一输出结构。

---

## 3. Design Principle

Inbox 保存的是 Knowledge Resource，而不是 Markdown 文件。

因此，每一个 Inbox Document 都应包含四个组成部分：

1. Resource
2. Payload
3. Knowledge
4. Metadata

四个组成部分共同构成完整的 Inbox Resource。

任何 Resource Policy 均不得改变 Inbox 的整体结构。

Resource Policy 仅决定 Payload 的保存深度。

---

## 4. Standard Structure

### 4.1 YAML Frontmatter

所有 Inbox 文档均采用如下 YAML 结构：

```yaml
---
status: 待发展 | 共创中 | 成卷 | 已归档
type:
resource_url:
resource_capture_time:
resource_policy:
tags:
publish_date:
confidence:
---
```

> `status` 取值由《知识生命周期协议》定义，不得自创状态名。

### 4.2 Body Sections

正文统一采用如下章节：

```markdown
# Title

---

## Resource

- Source:
- Original URL:
- Capture Time:
- Resource Policy:

---

## Original Content

---

## Summary

---

## Insight

---

## References
```

章节名称不得随意修改。

允许新增章节，但不得删除标准章节。

---

## 5. Document Naming Rule

Inbox Document Title 应遵循统一命名规则。

格式：

```
【类型】 标题
```

例如：

- 【摘】 闻道有先后，从知道到应用，还有很长路要走
- 【念】 无限答案时代的认知构建
- 【文】 AI 时代最后的庇护所
- 【事】 Karpathy 十条军规

标题应保持与 Resource Title 一致。

不得自动修改标题。不得删除前缀。不得根据 Resource Policy 修改命名格式。

Document Name 与 Markdown 一级标题应保持一致。

---

## 6. Resource Specification

Resource Section 用于建立 Resource Identity。

至少应包含以下字段：

| Field | Description |
|--------|-------------|
| resource_url | 原始地址（为空时省略此字段） |
| resource_capture_time | 收录时间 |
| resource_policy | 当前 Resource Policy |

任何 Inbox 文档均不得缺少 Resource Section。

---

## 7. Payload Specification

Payload 保存知识内容，分为三个层级。

### 7.1 Original Content

Original Content 为知识本体。

应尽可能完整保留原始内容。除格式调整外，不得修改内容。

对于长期知识资源，应优先保存 Original Content。

**Markdown 格式原文**：当原始资源本身为 Markdown 格式（如课程笔记、文档附件、已导出的文章），应全文直接收录于 Original Content 中，保留原始结构与格式。不得以摘要、大纲或要点提取替代全文。

### 7.2 Summary

Summary 用于忠实描述原文。

Summary 应保持原文逻辑。不得加入新的观点。不得进行知识延伸。

Summary 的职责是帮助快速理解原文。

### 7.3 Insight

Insight 用于保存 AI 或 Creator 对知识的新理解。

Insight 可以：

- 提炼观点
- 建立关联
- 提出问题
- 延伸思考

Insight 不得修改 Original Content。Insight 不得替代 Summary。

### 7.4 References

References 用于建立跨文档关联。

格式采用 Obsidian 双向链接（Wikilink）：

```markdown
- [[文档标题]]
```

References 应链接至文境中与此资源相关的其他内容，包括：

- 藏阁 Inbox 中方向相近的灵感或摘录
- 成卷中已完成的文章
- 归藏中已归档的知识
- 道的系统原则文档

References 为可选章节。无关联内容时留空，不得填入 Knowledge Map 节点作为替代。

不得使用纯文本替代 Wikilink。不得在 References 中重复已在 Tags 中表达的知识关联。

---

## 8. Knowledge Specification

Knowledge Section 用于建立 Knowledge Network。

Tags 用于 Obsidian 索引与知识检索。

Agent 应根据 Knowledge Map Convention 匹配 Canonical 并生成对应 Tags。

若未命中 Canonical，Agent 应提出新增 Canonical 建议，不得直接创建新的 Canonical。

---

## 9. Metadata Specification

Metadata 用于描述资源属性。

标准字段包括：

| Field | Description |
|--------|-------------|
| publish_date | 发布时间 |
| confidence | AI 识别置信度 |

未来允许新增 Metadata 字段。新增字段不得破坏已有结构。

---

## 10. Resource Policy Compatibility

所有 Resource Policy 使用统一 Inbox Structure。

不同 Policy 仅决定 Payload 内容。对应关系如下：

| Resource Policy | Original | Summary | Insight | Images | Attachments |
|-----------------|----------|----------|----------|---------|-------------|
| Index | Optional | Optional | Optional | No | No |
| Knowledge | Required | Required | Required | Optional | No |
| Archive | Required | Required | Required | Required | Required |

因此，Resource Policy 不影响 Inbox Structure，仅影响 Payload Completeness。

---

## 11. Output Rule

Capture Workflow 完成后，最终输出必须符合 Inbox Standard。

任何 Workflow 均不得自行定义 Markdown 结构。所有输出均应遵循本规范。

---

## 12. Future Extension

未来允许扩展：

- Metadata 字段
- Payload Section
- Resource 字段

不得删除已有字段。不得修改章节名称。不得改变标准结构。

所有扩展均应保持向后兼容。

新增内容应经过 Architecture Review 后方可纳入标准。

---

## 13. Output Contract

Inbox Standard 是 Capture Workflow 的唯一输出规范（Output Contract）。

Capture Workflow 负责完成资源识别、资源注册、Resource Policy 执行以及 Knowledge Mapping。

Capture Workflow 不负责定义最终 Markdown 文档结构。

所有 Inbox 文档必须按照 Inbox Standard 输出，包括但不限于：

- 文档命名
- YAML Metadata
- Resource Section
- Payload Structure
- Knowledge Section
- Metadata Section
- References

任何 Capture Workflow 均不得直接生成 Markdown。

任何新增字段、章节或命名规则，必须首先修改 Inbox Standard。

Capture Workflow 仅负责按照 Inbox Standard 生成最终文档。

因此：Inbox Standard 是 Capture Runtime 的唯一输出规范。Resource Policy 决定保存内容，Inbox Standard 决定保存格式。二者职责必须保持独立。
