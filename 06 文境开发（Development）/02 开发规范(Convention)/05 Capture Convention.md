# Capture Convention

---

## 1. Purpose

Capture Workflow 用于规范所有外部资源进入文境时的统一处理流程。

Capture 的目标不是保存内容。Capture 的目标是建立可引用的 Knowledge Resource。

任何进入文境的资源，都必须首先完成 Resource Registration。之后根据 Resource Policy 决定 Payload 的保存策略。

Payload 包括：

- Original Content（原文）
- Summary（摘要）
- Insight（AI 提炼）

不同 Resource Policy 决定是否保存上述内容。

Capture Convention 不负责定义具体 Policy。具体规则由《Resource Policy Standard》维护。

---

## 2. First Principle

```
Capture = Resource Registration + Payload Acquisition
```

Resource Registration 为必选步骤。Payload Acquisition 为可选步骤。

任何 Capture Workflow 均不得跳过 Resource Registration。

---

## 3. Capture Pipeline

```
Trigger
↓
Recognize Resource
↓
Resource Registration
↓
Creator Confirm Resource Policy
↓
Payload Acquisition
↓
Knowledge Match
↓
Metadata Generation
↓
Save Inbox
↓
Set Initial Status（`待发展`，依知识生命周期协议）
↓
Return Conversation Runtime
```

---

## 4. Resource Registration

所有 Capture Workflow 必须首先建立 Resource Index。

Resource Index 至少包括：

- Resource ID
- Resource Type
- Source
- URL（如存在）
- Date
- Tags
- Related

即使 Payload 获取失败，Resource Registration 仍应成功。Capture Workflow 不得因此失败。

---

## 5. Resource Policy

Capture Workflow 不负责定义 Resource Policy。

完成 Resource Registration 后，Agent 应读取 Resource Policy Standard。根据创作者确认的 Resource Policy 执行对应 Payload Acquisition。

Capture Convention 不维护任何具体 Resource Policy。

---

## 6. Knowledge Matching

完成 Resource Registration 后，Agent 应查询 Knowledge Map，匹配 Canonical，生成 Tags 与 Related。

不得跳过 Knowledge Matching。

---

## 7. Failure Rule

正文解析失败、图片获取失败、外部资源无法访问，均不得导致 Capture Workflow 失败。

只要 Resource Registration 已完成，Capture 即视为成功。

Payload 可留空，后续允许重新解析。
