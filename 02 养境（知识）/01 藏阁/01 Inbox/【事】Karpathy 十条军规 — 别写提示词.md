---
status: 待学习
type: 事
resource_capture_time: 2026-06-30
resource_policy: Knowledge
tags:
  - AI
  - Karpathy
  - Claude
  - 提示词
  - 工程实践
  - LoopEngineering
publish_date: 2026-06-30
confidence: high
---

# 【事】Karpathy 内部十条军规：别写提示词

> **CLAUDE.md: Field Notes on Getting a Language Model to Write Code You Will Not Rewrite**
> 
> 副标题：A Short List of Rules, Earned by Watching the Same Mistakes Twice

Karpathy 入职 Anthropic 五周，内部实战版 10 条 Claude.md 军规流出。比 GitHub 上 18 万星的 4 条社区版多了六条新章节。

核心信条：**模型擅长生成看起来合理的代码，但不擅长发现「看起来合理」跟「真的对」之间的差距——这份纪律，得从过程中来。**

---

## 十条军规

### 1. 先读再写（Read Before You Code）
模型写出烂代码最大的原因，是它根本没读你的代码库就开始动手。先看要改的文件，把已有模式照搬过来，搞明白项目实际依赖什么。

### 2. 先想再敲（Think Before You Code）
搞清楚你要做什么再动手。例：「添加认证」其实是五件不同的事，列出来说明取舍。搞不懂就停下来问，别用一段看着像那么回事、一跑就崩的代码糊弄。

### 3. 极简主义（Simplicity）
写能解决眼前问题的最少代码，不是能解决所有未来版本的最少代码。如果某样东西被抽象出来的唯一理由是「以防万一」，那你就过度构建了。

### 4. 精准手术（Surgical Changes）
diff 应该和任务一样小。没让碰的别碰，匹配已有代码风格，不要顺手重排格式。你能为每一行改动找到和用户需求的直接关联吗？找不到，就撤回。

---

以下 6 条是内部新增：

### 5. 验证（Verification）
修 bug 的时候，先把这个 bug「录」下来——写一个能稳定复现的测试用例。修完跑一遍，测试通过了才算真修好。测那些真会在用户面前炸掉的场景，跳过测试等于承认代码设计有问题。

### 6. 目标驱动执行（Goal-Driven Execution）⭐ 灵魂条款
动手写代码之前，先把「做完了」长什么样说清楚——而且得是能验证的。比如「加个验证」太模糊，要翻译成：「用户邮箱没填或填错了，要弹出明确的报错提示，两种情况都得测过。」

### 7. 调试（Debugging）
东西坏了，去查，别猜。读完整报错和堆栈跟踪，先复现问题再动手改，一次只改一个地方。

### 8. 依赖管理（Dependencies）
每一个依赖都是你无法控制的永久代码。先问标准库能不能搞定？加了就说清楚为什么。

### 9. 沟通（Communication）
说你做了什么、为什么，不只是丢一块代码。「我不确定这个库是否支持流式传输」叫好的沟通；「我觉得这应该能用」不叫。

### 10. 常见翻车模式（Common Failure Modes）
- **Kitchen Sink** — 让你修水龙头，它把整个厨房拆了重装
- **Wrong Abstraction** — 该合并的没合并，不该抽象的瞎抽象
- **Optimistic Path** — 只考虑顺利路径，不考虑用户输错、网络断、服务器挂
- **Runaway Refactor** — 本来只改一个文件，多米诺骨牌倒了十几个

发现自己正在犯这些错时，立刻停手，不是硬着头皮冲到底。

---

## 更大的变化：循环工程（Loop Engineering）

Claude Code 创始人 Boris Cherny 说：**「我不再给 Claude 写提示词了。循环替我写。我的工作，就是写循环。」**

核心思路：搭一个小系统，替 AI 反复派活、验收、纠错，直到做完。做完一件记下来，下次接着干。你睡着了，它还在跑。

Claude Code 已内置 `/goal`（干到完成为止）和 `/loop`（按节奏定期检查）两条命令。

**Karpathy 的十条军规 = Loop 的自检标准。** 没有纪律文件，Loop 在高速生产 bug；有了它，Loop 才知道怎么在翻车前刹车。

三次范式跃迁：提示词工程 → 上下文工程 → 循环工程。人类从「操作员」变成「设计者」。

## References
