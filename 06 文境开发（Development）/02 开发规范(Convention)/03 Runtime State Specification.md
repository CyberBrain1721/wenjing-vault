# Runtime State Specification

---

## 1. 目的

本规范定义 Development Runtime 使用的统一状态（Runtime State）。

所有 Development Agent 在读取或写入 Current Context 时，应使用本规范定义的状态名称。

Runtime State 用于描述当前 Development Runtime 所处阶段。不用于描述开发任务，不用于描述开发结果。

---

## 2. 状态原则

Runtime State 应满足以下原则：

一、任何时刻只能存在一个 Runtime State。

二、Runtime State 仅描述当前运行状态。

三、Runtime State 由 Development Runtime 自动维护。

四、所有 Agent 使用统一状态名称，不得自行创建新的 Runtime State。

---

## 3. Runtime State

### 3.1 Initial

表示当前不存在可恢复的 Development 状态。

通常发生于：

- 第一次进入 Development Runtime
- Current Context 尚未建立有效状态

进入 Initial 后，Development Runtime 应进入 Ready，等待新的 Development Session。

---

### 3.2 Resume

表示 Current Context 包含有效开发状态。

Development Runtime 已成功恢复，应继续执行未完成的 Development 工作。

---

### 3.3 Review

表示当前 Runtime 正处于设计评审阶段。

当前工作重点为：

- Design Review
- Architecture Review
- RFC

不进入正式开发。

---

### 3.4 Blocked

表示当前 Development 暂时无法继续。

通常原因包括：

- 缺少创作者决策
- 缺少必要信息
- 等待测试结果
- 等待协议确认

Blocked 状态下，Development Runtime 保持等待。

---

### 3.5 Completed

表示当前 Development Session 已完成。

Current Context 已更新。Development Runtime 可以正常退出。

---

## 4. Runtime Lifecycle

Runtime State 与 Runtime Lifecycle 相互独立。

Runtime State 描述当前 Development 状态。Runtime Lifecycle 描述当前 Runtime 生命周期。

例如：

- Runtime State：Resume
- Runtime Lifecycle：Ready

表示：当前已恢复开发状态，并可以接受新的开发任务。

---

## 5. Current Context

Current Context 第一项应固定记录 Runtime State。

例如：

```
Runtime State：Initial
```

或：

```
Runtime State：Resume
```

Development Agent 不得使用其他名称替代。

---

## 6. 扩展原则

新增 Runtime State 前，必须经过 Architecture Review，并更新本规范。

未经 Runtime State Specification 定义的状态，Development Agent 不得使用。
