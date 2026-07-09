---
status: 待消化
type: 摘
resource_url: https://mp.weixin.qq.com/s/r6CE2U3Y0-pU05wF3_PuTQ
resource_capture_time: 2026-06-30
resource_policy: Knowledge
tags:
  - AIHOT
  - AI资讯
  - 信息筛选
  - VibeCoding
  - 产品设计
publish_date: 2026-06-30
confidence: high
---

# 【摘】这个封装了我3年自媒体经验的AI热点网站，今天向所有人免费开放

> 来源：数字生命卡兹克｜公众号「数字生命卡兹克」
> 原文发布于 2026年5月7日

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2jjfQoZLoqW46nqOg5QnNmqiblXgeGaEBzvZ7d4GSz2vJsDlia6vTGnmib9Xtws2DggBkMqVF1nPN1ibDCF0TutibPtXDAqSoY9xDaM6I52Uia1Nk/0?wx_fmt=jpeg)

今天，我决定把我自己做的，帮助我自己监控AI热点、辅助找选题的网站，向所有人免费开放了。它几乎承载了我三年做AI自媒体获取信息的经验。我把它称为，**AIHOT**。

很多小伙伴可能在过去我很多篇文章中，都见过它的身影了。这个东西的作用其实巨简单，一段话就能描述清楚：

**帮助你以干净的时间线的形式，监控这个世界上跟AI相关的信息，然后用我自己对内容挑选的策略，将值得你关注的东西精选出来，对信息海进行降维，从而保护我们的为数不多的注意力。**

这玩意其实本身是给我们公司内部用的，创造它的目的，其实就是为了保护我自己的创作精力，我一开始真的没打算把它开放给所有人。因为对于一个自媒体来说，信息的获取的及时性，有的时候就是命根子。

但，可能是产品心理作祟吧，我工作这么多年，一直在设计产品，一直在做产品，做了好多好多年。我还是有产品梦的，我还是想为这个美好的互联网贡献一点我自己的东西的，而我很多时候最大的成就感的来源，其实就是大家喜欢看我的文章，喜欢用我做的产品。

我在每次文章的底部，都会写上一句话，叫做"谢谢你看我的文章。"这句话来源于我最喜欢的一部电影，《头号玩家》。这是绿洲游戏的创造者哈利迪在最后消逝的时候，对身为玩家的主角所说的一句话，也是我认为整部电影，最棒的落笔。

我也想我创造的东西，被人看见，被大家喜欢，仅此而已。

所以在4月初的某个夜晚，我甚至都没有说服自己的过程，就突然间起心动念，就觉得，不如给大家开放了吧，大家一起用吧。如果能帮助到大家，那我就真的很开心了。

**网址：** [https://aihot.virxact.com/](https://aihot.virxact.com/)

---

## AIHOT 的产品逻辑

我觉得在这个时代，很多的工作其实已经不是执行了，执行这块Agent已经可以干的很好了，现在更多的工作成了信息的处理，我自己一般分为三个流程：

> **获取信息 → 对信息进行分析 → 基于信息做决策**

对于我做内容创作来说，获取信息就是从信息海中找到值得我关注的，而进行分析，其实就是基于信息，看看有什么选题角度可以切入，最后的决策，其实就是这个选题到底值不值得写。

目前来说，AIHOT解决的就是获取信息的问题。

---

## 第一步：筛选信源

在如今，信源比信息重要。

作者目前监控的信源是 **168个**，手段有RSS订阅、HTML爬取、公开API接口、花钱买的三方数据接口等。

信源分3级：
- **T1**：官方一手信息（OpenAI博客、Anthropic工程博客、奥特曼Blog、CMU博客等）
- **T1.5**：官方X账号（信息更多更杂，权重调低）
- **T2**：大佬个人号、KOL、媒体、综合资讯站

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqXwxArxPyPGz0n4eFibgnicd44pwoib0B3JaELzNgD6b8TKQr0RhwsgRftsovUJapVlHV9wlu2XJVvicPWliaDXDq6dfc6732p5O3uc/640?wx_fmt=png&from=appmsg)

---

## 第二步：信息处理流程

每天抓取几百条信息，但有一半跟AI无关。

### 处理流水线

```
抓取 → DeepSeek V3.2 预筛（是否与AI有关）
       → 无关：直接落库
       → 有关：进入评分 + 翻译 + 摘要（并行）
              → 五维评分 → 代码权重公式计算 → 质量分
              → 是否过精选阈值（代码判断）
              → 事件聚类（embedding语义聚类）
```

### 精选评分机制的11版迭代

作者最核心的坑：**第一版以为写个Prompt让大模型打分就行。**

结果：硬核论文动不动90分，Sam Altman的鸡汤推文87分，同一事件被报道七遍全部进精选。

然后开始往prompt里加规则（涨到300多行），引入人类反馈标注+自动评估迭代。跑了一周后崩溃——规则越多，泛化越差。

最终结论：**能用代码处理的，一律不用模型处理。**

重构后：
- 大模型只做一件事：打 **5个维度分**（Prompt从600行缩减到200行）
- 权重计算、精选判断：全部由**代码公式**处理
- 模型：DeepSeek V4 Pro（世界知识强 + 成本低）

> "用代码管控的最好的结果，就是极度的可控、可调。"

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqVL4wNdFydNG73CtHqEKHiauTQtKLvFckfEwVicMlWlpJ3ra1iciaCgD8o6pSzsSoXUYGIzDI59H8ZnY2s8MCiblTziaP0eqj2FO6470/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2jjfQoZLoqXR4BKnUFwWVpdDOSU2Zmsk70UKDMJHjzHiaicH473OUxHbdgsv9vwSntaG6zxvMAicxDutTztd482vJfUJZv8oZkfMZTSyGxfiakU/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqUrRBOpeG3Sic5byJTLp1EsEgVXctSZB1iaUo82ng9tvGg39tNBOUMavRRnNL1R0uuJ37u7gOwZ92HicRVcbicFUOUic2XCuS20ZYbA/640?wx_fmt=png&from=appmsg)

---

## 第三步：事件聚类

用embedding把语义相近的条目聚到一个事件簇里，簇里选一条最权威的当主条，其他折叠进去。官方源永远优先当主条。

---

## AI日报功能

每天早上8点，系统自动把过去24小时的精选内容整理成日报。

版块分五块：模型发布/更新、产品发布/更新、行业动态、论文研究、技巧与观点。

日报不需要任何大模型生成——所有精选、分类、翻译在入库时已完成，只需1秒。

![](https://mmbiz.qpic.cn/mmbiz_png/2jjfQoZLoqX0ubHrb7JI8RjiccVZ8nNhRMA8Qe3ibAdqNSOXPzMnwhoKQIReniaUTwzHG7mugnEicOSNiahrX64jb2x8zywD1wgTO0F1wbaPXnrw/640?wx_fmt=png&from=appmsg)

---

## 未来计划

- 趋势预测（抓到加速曲线爆发初期）
- 每条信息拉取过去1个月的相关信息
- AIHOT热度指数

---

## 核心教训

> **「能用脚本就别用Agent」**
>
> 你绝不能把所有事情都交给模型。打分是他、权重计算是他、打标是它、判断是否精选还是它——结果就是灾难。
>
> 大模型只做自己擅长的事。剩下的，用代码。

**网址：** [https://aihot.virxact.com/](https://aihot.virxact.com/)

## References
