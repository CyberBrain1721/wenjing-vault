# Resource Policy Standard

---

## 1. Purpose

Resource Policy Standard 用于规范所有外部资源进入文境时的默认保存策略。

Resource Policy 决定 Agent 应如何保存资源，以及保存到什么深度。

Resource Policy 不负责 Resource Registration。

所有进入文境的资源，必须首先完成 Resource Registration。随后，由 Agent 根据资源类型推荐默认 Policy。创作者拥有最终选择权。

---

## 2. First Principle

文境保存资源的目的，不是建立收藏夹，而是保证知识能够长期保存、持续引用，并参与知识网络。

任何 Resource Policy 都必须遵循以下原则：

```
Resource Registration
↓
Payload Acquisition
↓
Knowledge Mapping
↓
Save
```

其中：Resource Registration 为所有 Policy 的必选步骤。Payload Acquisition 根据不同 Policy 决定保存深度。Knowledge Mapping 为所有 Policy 的必选步骤。

---

## 3. Resource Registration

所有进入文境的资源，都必须首先建立统一 Resource Index，至少包括：

- Resource ID
- Resource Type
- Source
- Original URL
- Capture Time
- Resource Policy
- Tags
- Related

无论采用任何 Resource Policy，均不得跳过 Resource Registration。

---

## 4. Policy 1：Index

### 4.1 Purpose

建立资源索引。

适用于：工具链接、GitHub Repository、软件官网、临时收藏、稍后阅读。

### 4.2 保存内容

保存：

- Resource Index
- Title
- Source
- URL
- Metadata
- Tags
- Related

不保存：

- Original Content
- Summary
- Insight
- Images
- Attachments

---

## 5. Policy 2：Knowledge（Default）

### 5.1 Purpose

保存完整知识。

适用于：微信公众号、博客、教程、技术文章、PDF、长期学习资料，以及所有具有知识价值的内容。

Knowledge 为文境默认 Resource Policy。

### 5.2 保存内容

保存：

- Resource Index
- Title
- Source
- URL
- Original Content
- Summary
- Insight
- Metadata
- Tags
- Related

说明：Original Content 为原文全文。Summary 用于忠实保留原文结构与主要内容。Insight 用于记录 AI 或 Creator 对知识的进一步理解。

Original Content 不得被 Summary 替代。Summary 不得被 Insight 替代。三者共同构成完整 Knowledge Payload。

---

## 6. Policy 3：Archive

### 6.1 Purpose

永久保存资源。

适用于：重要资料、长期研究资料、容易失效的网络资源、需要完整离线保存的内容。

### 6.2 保存内容

保存：

- Resource Index
- Title
- Source
- URL
- Original Content
- Summary
- Insight
- Images
- Attachments
- Metadata
- Tags
- Related

Archive 应尽可能完整保留资源全部内容。Summary 与 Insight 不得代替 Original Content。

---

## 7. Resource Recommendation

完成 Resource Recognition 后，Agent 应根据资源类型推荐默认 Resource Policy。

推荐对照：

| 资源类型 | 推荐 Policy |
|----------|-------------|
| GitHub | Index |
| 微信公众号 | Knowledge |
| PDF | Knowledge |
| 学术论文 | Archive |
| YouTube | Knowledge（字幕与正文） |
| 普通网页 | Knowledge |

推荐仅作为建议。最终选择权始终属于创作者。

---

## 8. Policy Confirmation Rule

完成 Resource Recognition 后，Agent 应根据资源类型推荐默认 Resource Policy。推荐仅作为建议，最终决定权始终属于创作者。

若创作者已经明确指定 Resource Policy（如"保存全文""只保存链接""Archive"），Agent 应直接执行对应 Policy。

若创作者未指定 Resource Policy，Agent 不得默认开始 Payload Acquisition，应等待创作者确认。例如：

> 检测到微信公众号文章。
> 推荐：Knowledge（保存全文）
> 其它可选：Index / Archive
> 请选择。

创作者确认后，Agent 方可继续执行：

```
Payload Acquisition
↓
Knowledge Mapping
↓
Save Inbox
```

Agent 不得跳过 Creator Confirmation。不得自动修改 Resource Policy。不得根据历史习惯自动推断 Creator 的最终选择。每一次 Capture Workflow 均应以当前创作者确认结果为准。

---

## 9. Failure Rule

正文解析失败、图片获取失败、附件下载失败，均不得导致 Capture Workflow 失败。

只要 Resource Registration 已完成，Capture 即视为成功。

Payload 可为空。Agent 应保留 Resource Index。允许后续重新解析。

---

## 10. Knowledge Payload Principle

Knowledge Payload 由三个层级组成：

```
Original Content
↓
Summary
↓
Insight
```

其中：Original Content 为知识本体。Summary 用于保留原文上下文与主要结构。Insight 用于沉淀 AI 或 Creator 的进一步理解。

Original Content 不得省略。Summary 不得替代 Original Content。Insight 不得替代 Summary。

任何长期知识资源，均应优先保证 Original Content 的完整保存。

---

## 11. Knowledge First Principle

文境是长期知识系统。正文属于知识本体。AI Summary 属于辅助信息。

任何具有长期知识价值的资源，默认应保存原文，不得仅保存 AI Summary。

AI Summary 可以重新生成。原文一旦丢失，将无法恢复。

因此：原文的长期保存优先级高于 AI Summary。

---

## 12. Workflow Relationship

Capture Workflow 不直接决定保存内容。

Capture Workflow 负责：

- Resource Recognition
- Resource Registration
- 调用 Resource Policy
- 调用 Knowledge Mapping
- 保存 Inbox

Resource Policy 负责：决定 Payload 保存深度。

Knowledge Map Convention 负责：建立 Canonical、生成 Tags、建立 Related。

三者职责互不重叠。

---

## 13. Future Extension

未来允许新增新的 Resource Policy。

新增 Policy 应遵循以下原则：

- 不影响已有 Policy
- 不影响 Resource Registration
- 保持统一 Metadata
- 保持统一 Knowledge Mapping
- 保持向后兼容

任何新增 Policy，都应经过架构评审（Architecture Review）后方可加入文境标准。
