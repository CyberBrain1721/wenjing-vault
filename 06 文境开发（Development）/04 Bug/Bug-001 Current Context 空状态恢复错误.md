# Bug-001｜Current Context 空状态恢复错误

## 状态

Closed — 2026-06-30

---

# 发现时间

2026-06-30

---

# 发现方式

Experiment-001

Hermes 与 WorkBuddy Runtime 初始化测试

---

# 问题描述

当 Current Context 不包含任何开发状态时。

部分 Agent 会主动继续读取 Development Journal、Architecture Review、RFC 等历史文档，并尝试自行恢复当前开发状态。

该行为绕过了 Current Context 的职责。

导致 Current Context 无法成为 Development Runtime 唯一状态来源。

---

# 实际行为（Actual）

Current Context 为空。

↓

Agent 主动继续扫描 Development 文档。

↓

Agent 根据历史内容自行推导当前开发状态。

↓

进入 Ready。

---

# 预期行为（Expected）

Current Context 为空。

↓

Agent 判定：

首次 Development Session。

↓

停止继续读取 Development 文档。

↓

进入 Ready。

↓

等待创作者新的开发任务。

---

# 原因分析

Current Context Protocol 未明确规定：

当 Current Context 不包含开发状态时。

Agent 不得继续通过其他 Development 文档恢复当前开发状态。

导致不同 Agent 采用不同策略完成初始化。

---

# 修复方案

修订：

Current Context Protocol

新增：

首次 Development Session 规则。

明确规定：

Current Context 为唯一状态来源（Single Source of Truth）。

不得使用 Journal、RFC、Bug 或 Architecture Review 恢复当前状态。

---

# 验证方式

重新执行：

Experiment-001

验证不同 Agent 在 Current Context 为空时是否停止继续读取 Development 文档。

---

# 修复记录

## 修复日期

2026-06-30

## 修复内容

### 1. 协议层

Current Context Protocol 新增「首次 Development Session」规则：

> 如果 Current Context 不包含任何开发状态，应视为首次 Development Session。Agent 不得主动通过读取 Development Journal、Architecture Review、RFC、Bug 或其他 Development 文档恢复开发状态。

### 2. 状态文件层

Current Context 预置种子文件，不再为空：

```markdown
# Current Context

## Runtime State
Initial
```

- 首次读取从「空白推导」变为「显式状态」
- Runtime State 字段取值：`Initial` | `Active`
- 消除隐式信号，符合协议驱动原则

## 验证结果

Experiment-004 测试通过。Agent 读取 Current Context 后正确识别 `Runtime State: Initial`，未主动扫描其他 Development 文档。

---

# 当前状态

Closed — 2026-06-30

修复完成，等待正式集成。