---
status: 待发展
type: 摘
resource_url: https://mp.weixin.qq.com/s/omwt7d9BSFX7kotW9vo9bQ
resource_capture_time: 2026-06-15
resource_policy: Knowledge
tags:
  - AI
  - Agent
  - LoopEngineering
publish_date: 2026-06-15
confidence: high
---

# 【摘】 Prompt该退环境了，未来属于Loop Engineering。

---

## Resource

- Source: 数字生命卡兹克
- Original URL: https://mp.weixin.qq.com/s/omwt7d9BSFX7kotW9vo9bQ
- Capture Time: 2026-06-15
- Resource Policy: Knowledge

---

## Original Content

最近，AI行业又出现了一个有趣的新词。Loop Engineering。

6月7号，OpenClaw的创始人Peter发了一条推：你不再需要为编码智能体编写提示词了，你应该设计循环来提示你的Agent。而在这之前几天，Claude Code的创始人Boris在一个开发者大会上也说了差不多的话——我不再手动给Claude写提示词了，我运行着能让Claude自动编排任务的循环，我的工作，就是编写这些循环机制。Google的Addy Osmani紧接着发了一篇长文，把Loop Engineering这个概念正式梳理了出来。于是，继Prompt Engineering、Context Engineering、Harness Engineering之后，AI行业的第四个逐渐形成共识的Engineering，就这么诞生了。

Loop Engineering，其实就是在Harness之上，又往上走了一层。把一个套马的缰绳，变成了全自动工业流水线。

以前你用Claude Code写代码，是坐在设备前一轮一轮的，你说一句它回一句，你就是驱动整个循环的发动机。而现在，Boris的工作方式是写一个loop，比如`/loop babysit all my PRs`，自动修CI问题，有新评论就派子Agent去处理。Claude Code开始自己跑，自动看GitHub上所有PR，哪些CI挂了就自己修，哪些review有新评论就自动派独立工作树Agent去改代码。他把一些loop挂到定时任务上，每天晚上自动启动。他自己说，2026年，他就再也没有手写过一行代码了。

你定义目标，定义验证条件，定义失败了怎么处理，然后就可以放手了，这一切交给系统。

Addy Osmani把完整的loop拆成五个组件：①定时任务（loop的心跳）②工作树隔离（Worktree，每个Agent独立空间）③项目知识体系（CLAUDE.md+记忆+docs，比单一skill更完整）④连接器（MCP，接入GitHub/飞书/数据库）⑤子Agent（做事和检查分开，不同模型互相验证）。五个东西加在一起，就是一个完整loop的骨架。

但作者认为这些都只是"术"。Loop Engineering真正的核心能力是**定义目标的能力**。

他用`/goal`命令举例：目标A「把这个应用优化一下」——Claude会陷入尴尬，不知道什么叫"优化好了"，可能改一点就停，也可能一直改到面目全非。目标B「test/auth目录下所有测试通过，tsc --noEmit零报错，npm run lint零违规」——每改一轮跑三个命令，全过就停，没过继续，清清楚楚。

定义目标的能力，本质上是**管人的逻辑**。你跟员工说"把这个功能做好"，做出来的大概率不是你想要的。你说"这个接口响应时间降到200毫秒以下，错误率控制在0.1%以内，下周三前上线"，偏差就小很多。目标清晰、资源充足、反馈及时——好的loop的三个要素，和好的管理三要素一模一样。

但还有一个陷阱：**古德哈特定律**——当一个衡量指标变成了目标本身，它就不再是好的衡量指标。Agent比人类更擅长钻规则空子：如果loop条件是测试全部通过，Agent可能不去修Bug，直接把失败的测试删了。所以好的目标定义，不能只有完成标准，还必须有"不能怎么做"的边界。Harness（约束）和Loop（驱动力）加在一起才是完整系统。

作者给出自己的目标定义框架：①完成标准要可被机器验证 ②边界条件跟完成标准一起定义 ③要有失败的降级方案 ④目标要分层。

最后串联四条演化线：Prompt Engineering（语言表达）→ Context Engineering（信息筛选）→ Harness Engineering（系统设计）→ Loop Engineering（目标定义与管理）。语言学、信息科学、控制论、管理学——四个Engineering，四门古老学科。

---

## Summary

卡兹克解读了AI行业新概念"Loop Engineering"：从手动写Prompt驱动Agent，进化到设计自动循环系统（loop）让Agent自主运行。核心观点是Loop Engineering的真正竞争力不在工程而在管理——定义清晰、可验证、有边界的目标的能力，与管人的逻辑完全同构。文章拆解了Loop的五个组件（定时任务/工作树隔离/知识体系/MCP/子Agent），并警告古德哈特定律陷阱（Agent会钻验证规则的空子）。最终将Prompt→Context→Harness→Loop四次跃迁对应到四门古老学科，主张AI时代管理学不但没死反而更重要。

---

## Insight

这篇文章对文境有直接的相关性。Loop Engineering的五个组件——定时任务、工作树隔离、知识体系、连接器、子Agent——恰好映射了文境已经在实践的许多机制：Cron调度、Agent隔离运行、Skill体系、MCP工具接入、多Agent验证。但文章真正的洞见不在工程层，而在"定义目标的能力"这一点上。

这恰好击中了文境当前设计中的一个核心张力：**文境的协议驱动（Protocol-Driven）本质上就是一种Loop Engineering——协议就是预先定义好的目标和约束，Agent在loop中按协议执行。** 但问题在于：协议的粒度应该多细？过于模糊（"优化一下"）Agent会迷失，过于精确（"全部测试通过+零lint"）可能触发古德哈特效应——Agent为满足协议而满足协议，而非服务真实创作意图。

这对文境的设计意味着：协议不能只是"怎么做"的清单，还必须包含边界条件（"不能怎么做"）和异常降级路径（"做不成时怎么办"）。这也解释了为什么文境的约束体系（道/系统约束）与工作流体系（Workflow Index）必须协同设计——它们分别对应Loop Engineering中的Harness（约束）和Loop（驱动力），缺一不可。

---

## References

