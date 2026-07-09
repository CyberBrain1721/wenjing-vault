# AR-004｜Inbox → 成卷 链路闭合评审

## 状态

Accepted · 2026-07-01

---

## 背景

文境的知识流转路径两端已有协议覆盖（Capture → Inbox、成卷 → 卷结构），但 Inbox → 成卷 这一段缺少协议。流转依赖人的判断和 Agent 的临场执行。

---

## 问题

Inbox 到成卷的过渡是否需要一个正式协议？如果需要，它应该定义什么？

---

## 选项

**A**：不需要。成卷 Convention 内补步骤即可。
**B**：需要。轻量"发展协议"（Inbox 状态流转）。
**C**：需要。统一"知识生命周期协议"，覆盖全链路。

---

## 决策

**选 C**。

理由：Inbox → 成卷 的问题本质不是一段缺失的链路，而是整条知识流转链缺少统一的状态模型。Capture、共创、成卷、归档各自由不同 Convention 管，但知识条目在流转中没有一个贯穿始终的状态定义。与其补一段，不如建一个生命周期协议，使各 Convention 的流程部分有统一的参照系。

---

## 实施

1. 新建 `09 知识生命周期协议`，定义全链路状态机
2. 更新 Capture Convention §7：Payload 完成后状态标记引用本协议
3. 更新 成卷 Convention §3：Step 4.5 更新来源状态，引用本协议
4. 更新 Inbox Standard §4：YAML 中 `status` 字段值域引用本协议
5. 更新 wenjing-protocol skill 的共创/成卷流程引用本协议

---

## 影响范围

- 新建：`09 知识生命周期协议`
- 修改：Capture Convention、成卷 Convention、Inbox Standard
- 不修改：Resource Policy Standard、Knowledge Map Convention 等
