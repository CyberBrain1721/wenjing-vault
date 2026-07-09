# Current Context Protocol

---

## 1. 目的

Current Context 是 Development Runtime 的唯一状态文件（State File）。

本协议规定 Current Context 的读取、写入、覆盖更新及维护规则。

所有进入 Development Mode 的 Agent 必须遵循本协议。

---

## 2. 唯一性

Development 中始终只允许存在一份 Current Context。

文件名称固定：`Current Context.md`。

不得创建多个 Current Context。不得保留历史版本。不得建立 Current Context 副本。

---

## 3. 读取规则

每次进入 Development Mode，Agent 完成 Development Entry 初始化后，必须立即读取 Current Context。

读取完成后，应恢复当前开发状态，再开始新的 Development Session。

不得跳过 Current Context。

---

## 4. 首次 Development Session

如果 Current Context 不包含任何开发状态，应视为首次 Development Session。

Agent 不得主动通过读取 Development Journal、Architecture Review、RFC、Bug 或其他 Development 文档恢复开发状态。

Current Context 为 Development Runtime 唯一状态来源。

首次 Development Session 完成后，由 Development Agent 生成第一份 Current Context。后续 Development Session 均基于 Current Context 恢复开发状态。

---

## 5. 写入与覆盖规则

每次结束 Development Session，Agent 必须重新生成 Current Context，覆盖旧版本。

不得追加。不得保留旧状态。

Current Context 始终代表最近一次 Development Session 的最终状态。Development 历史由 Development Journal 保存。

---

## 6. 修改权限

Current Context 默认维护者为 Development Mode Agent。Creator Mode 不得修改。

创作者原则上不直接编辑 Current Context。如需修正 Current Context，应开启新的 Development Session 并重新生成。

---

## 7. 内容规范

Current Context 必须使用统一模板。不得新增、删除或修改字段名称。

允许记录：

- 当前开发目标
- 当前开发阶段
- 当前完成进度
- 下一步工作
- 推荐继续阅读

不得记录：长篇讨论、架构分析、思考过程、Bug 内容、RFC 内容、Journal 内容。

---

## 8. 生命周期

```
Development Entry
↓
读取 Current Context
↓
恢复当前开发状态
↓
Development Session
↓
覆盖更新 Current Context
↓
更新开发索引（如有新增 Convention / Bug / 日志）
↓
结束 Development Session
```

---

## 9. 与其他模块的关系

- Current Context：保存当前开发状态
- Development Journal：保存开发历史
- Architecture Review：保存正式设计决议
- RFC：保存开放研究议题
- Bug：保存系统问题
- 开发索引：统一文档入口，避免孤岛

各模块职责互不重叠。

---

## 10. Agent 执行要求

Development Mode 初始化时，Agent 必须执行：

1. 阅读 Current Context
2. 根据 Current Context 恢复开发状态
3. 开始 Development Session

Development Session 结束时，Agent 必须执行：

1. 根据当前开发结果重新生成 Current Context
2. 覆盖原 Current Context
3. **更新开发索引**：若 Session 中新增或修改了 Convention / Bug / 开发日志，同步更新 `00 开发索引.md`
4. 结束本次 Development Session

未完成 Current Context 更新与索引同步，不应结束 Development Session。

---

## 11. 长期原则

Current Context 是 Development Runtime 唯一允许持续覆盖更新的状态文件。

它保存的是当前状态，而不是历史。

任何 Development Session，均应从 Current Context 开始，并以 Current Context 结束。
