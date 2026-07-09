---
name: wenjing-protocol
description: Agent initialization and protocol-driven workflow for the 文境 (Wenjing) knowledge vault system. Covers entry protocol, mode selection, Development Runtime bootstrap, Current Context lifecycle, and protocol compliance rules.
---

> **⚠️ 本 Skill 已合并进独立仓库**：[CyberBrain1721/obsidiancreatorskill](https://github.com/CyberBrain1721/obsidiancreatorskill)。所有协议逻辑已自包含在 `SKILL.md` 中，Bootstrap 脚本（`bootstrap.py`）、看板刷新（`refresh_dashboard.py`）、Canvas 速览生成（`generate_canvas.py`）、7 个插件文件全部捆绑。安装：`hermes skills install https://github.com/CyberBrain1721/obsidiancreatorskill`。本文件保留作为本地参考。

---

# 文境协议（Wenjing Protocol）

Agent 进入文境知识库后的协议驱动工作流程。协议决定流程，Agent 负责执行协议——不主动决定、不自行推断、不扫描全库。

## 触发条件

当用户说以下任一内容时加载本 skill：
- "文境入口" / "进入文境" / "文境"
- "Development Mode" / "开发模式"
- 在 `E:\文境vault` 目录下工作并需要遵循文境协议
- 用户提到 "Experiment-XXX" 与文境系统测试相关

## 完整初始化流程

### 阶段 1：入口

读取 `04 Agent入口/00 文境入口.md`。核心原则：
- 不主动索引整个 Vault
- 不根据已有知识推断当前任务
- 不自行决定下一步工作流程
- 协议驱动（Protocol-Driven）：Agent 执行协议

### 阶段 2：模式选择

读取 `04 Agent入口/01 工作模式确认（Mode Selection）.md`，呈现两个选项：
- ① 共创模式：作品创作、灵感讨论、知识整理、项目推进
- ② 开发模式：系统开发、协议修改、架构评审、Bug修复

**等待用户选择，不继续读取。**

### 阶段 3A：共创模式（Creator Mode）

#### 基础协议阅读

读取 `04 Agent入口/02 共创入口（Creator Entry）.md`，按顺序加载协议文档：

| 步骤 | 文档 | 路径 |
|------|------|------|
| ① | AI阅读原则 | `04 Agent入口/03 AI阅读原则.md` |
| ② | 道说明 | `01 悟道（系统）/00 道说明.md` |
| ③ | 文境总纲 | `01 悟道（系统）/01 山门/1.2 文境总纲.md` |
| ④ | 文境系统约束 | `01 悟道（系统）/03 文境系统约束.md` |

#### Runtime 建立

基础协议阅读完成后，建立 Creator Runtime：

1. **读取 Workflow Index**：`04 Agent入口/05 Workflow Index.md`。包含五个 Workflow 的触发条件：
   - **Capture**：收录、保存、记录、加入Inbox
   - **Organization**：整理、分类、重构
   - **Archive**：归档、收卷、完成项目
   - **Canonize**：入典、沉淀、提炼可复用知识
   - **Reflection**：反思、总结、Review、回顾

2. **进入 Conversation Runtime**（默认状态）。Agent 持续监听创作者任务，仅在 Trigger 出现时按需加载对应 Workflow。Workflow 完成后立即返回 Conversation Runtime。

3. **Lazy Loading 原则**：所有 Workflow 仅按需读取、按需执行。不主动加载任何未触发的 Workflow，不主动遍历 Vault。

初始化完成后进入 **Ready for Collaboration** 状态，等待创作者提出具体任务。

#### 藏阁（Inbox）交互规则

藏阁是文境的灵感收件箱，路径：`02 养境（知识）/01 藏阁/01 Inbox/`。

当用户要求「从藏阁开始共创」时：

**核心原则：第一个念头，永远是人的。** AI 展示灵感原文，先问"你看到了什么"——连接由创作者建立，AI 只从创作者的直觉展开。不允许 AI 先于创作者完成第一次模式识别。

1. **随机抽取 3 条灵感**（不列出全部条目）
2. **展示每条灵感的原文摘要**（标题 + 关键段落，不提炼、不生成方向、不总结主题）
3. **问「你看到了什么？它们之间你感觉到了什么联系？」**——等待创作者表达直觉
4. 基于创作者的回应，展开、补充、连接、挑战——真正的共创从这里开始

**严禁**：列出全部条目、AI 先于创作者提炼方向/生成主题、替创作者解释"你为什么会对它感兴趣"、在创作者表达直觉之前输出结构化创作方向。

**示例（正确——AI 展示原文，等创作者先开口）**：
```
从藏阁随机抽取三条：

①【摘】闻道有先后，从知道到应用，还有很长路要走
   > "信息本身并不能改变行为。知道和做到之间的鸿沟，往往比我们以为的更宽……"

②【念】无限答案时代的认知构建
   > "当 AI 可以瞬间生成任何答案，真正稀缺的不再是获取答案的能力，而是提出问题的能力……"

③【摘】暗处生长
   > "所有真正重要的变化，都不是在聚光灯下完成的……"

你看到了什么？它们之间有什么联系？
```

**示例（错误——AI 替创作者提炼了方向，属于越界）**：
```
三个方向：
① 知识的应用鸿沟 —— 为什么"知道"离"做到"那么远
② 认知构建 vs 消费 —— 无限答案时代的核心矛盾
③ 暗处生长的力量 —— 真正的改变发生在不被看见的地方
```

#### Capture Workflow 细节

Capture Workflow 触发后按 Capture Convention 执行 Pipeline。必读文档（Workflow Index）：Capture Convention → Knowledge Map Convention → Knowledge Map → **Inbox Standard**。

Inbox Standard 是 Capture Workflow 的**唯一输出契约**——文档命名、YAML frontmatter、章节结构均由其定义。**跳过 Inbox Standard 将导致输出格式不符合规范。**

Policy 选项：Index（仅索引）、Knowledge（默认）、Archive（完整离线存档）。Policy 名称以 `Resource Policy Standard` 为准。

外部 URL：curl 优先，遇到 CAPTCHA 或 JS 渲染页面（如微信公众号）尝试 browser。两者都失败时按 Failure Rule 不阻塞 Capture。\n\n**中文平台特殊处理**：知乎（zhuanlan.zhihu.com）使用 `zh-zse-ck` 反爬机制，curl 和 Browserbase 均被拦截；百家号（baijiahao.baidu.com）需登录。这些平台 curl 和 browser_navigate 各试一次即可——连续失败时不要反复重试同一思路，立即走降级路径：用 `start \"\" \"URL\"` 在用户本地 Chrome 打开 → 请用户粘贴正文。不要在没有 cua-driver 的环境中尝试通过 `start` 打开后自动抓取（Agent 无法读取用户本地浏览器内容）。

附件文件：当用户通过 `@file:` 附加文件时，Payload Acquisition 直接使用附件内容。

KM 匹配：当前 KM 节点有限（AI / Agent / 文境 / 主体性 / 创作 / Loop Engineering），不匹配时不创建新节点。新 Canonical 提案需创作者确认。

#### Inbox 输出格式

Capture Workflow 输出严格遵循 Inbox Standard。

文档命名：`【类型】 标题.md`

YAML frontmatter（全部扁平键值对，Obsidian Properties 可识别）：
```yaml
---
status: 待发展 | 共创中 | 成卷 | 已归档
type: 念 | 摘 | 事 | 梦 | 感 | 随 | 文 | 对 | 白 | 图
resource_url: （仅当有真实 URL 时保留，空值则删除整行）
resource_capture_time:
resource_policy:
tags:
publish_date:
confidence:
---
```

禁止：`resource_type`、`language`、`resource_id`、`resource_source`、`canonical`、`related`、`author` 字段。禁止嵌套 YAML。`resource_url` 为空时删除整行。

正文章节：`# 【类型】 标题` → `## Resource` → `## Original Content` → `## Summary` → `## Insight` → `## References`

#### 入典（Canonize）

当创作者发现某项知识已超越单一作品、可跨场景长期复用时，说「入典」。典阁路径：`02 养境（知识）/02 典阁/`。

**入典的核心判断**（只问一个问题）：**一年后，我还需要引用它吗？**

如果答案是"是"→ 入典。不确定 → 留在藏阁。

四条入典路径：

| 路径 | 来源 | 触发 |
|------|------|------|
| 从卷提炼 | 卷完成后，从中提取可复用方法/框架 | `入典 从 [卷名] 提炼 [X]` |
| 直接沉淀 | 客观规则/法律条文/技术规范，不需走卷流程 | `入典 [内容描述]` |
| 主动入库 | 创作中自己总结的方法论 | `入典 [方法论描述]` |
| 风格提取 | 从 5-10 份已完成卷/外部文章中提取写作风格画像 | `风格提取` / `风格复盘` |

**风格提取（路径四）**：批量文章 → 四维风格画像（语言特征/结构模式/语气倾向/书写习惯）→ 创作者逐维度审核校准 → 入典至 `创作体系/风格指南/`。支持自我分析（自己的卷）和外部作者分析两条子路径。风格画像是镜像，不是评分——Agent 只呈现事实，不评价好坏。复盘周期建议每月一次（日更频率）。详见 Convention `11 风格提取 Convention.md`。

典阁四个子分类（与实际目录结构对齐）：
- **创作体系** — Scene模板、世界观模板、人物模板、写作方法、风格指南
- **技术知识** — 代码模式、工具手册、技术参考
- **法律与规则** — 法律条文、合规要求、行业标准
- **客观知识** — 数据事实、方法论框架、概念定义

典阁文件命名规范：
- 单个条目使用类型前缀：`【人】`（人物模板）、`【学】`（学习资料）、`【组】`（关联组/关系模板）、`【法】`（方法/框架）等
- 关联组模板（如三人关系组）在 YAML frontmatter 中用 `group` 字段指向组文件，组文件用 `related` 字段列出成员
- 文件名不含路径，Wikilink 直接用完整文件名

Agent 执行入典时：
1. 确认内容类型（创作/技术/法律/客观）
2. 确定存放子目录
3. 生成典阁条目（命名、YAML frontmatter、正文结构化）
4. 如从卷提炼，在卷的 References 中建立双向链接

**典阁 vs 藏阁的边界**：藏阁存灵感（待处理），典阁存沉淀（已验证）。宁可不入典，也不要把典阁变成第二个藏阁。

#### 文境看板

系统仪表盘位于 Vault 根目录：`文境看板.html`。深色主题，纯创作者层六卡布局：

```
入境 | 道 | 藏阁
典阁 | 卷 | 归藏
   共创指令（全宽）
```

顶部显示完整生命循环：`道 → 境 → 卷 → 归藏 ⇢ 典阁 ↻ 卷`。

看板数据通过 Hermes Cron Job 按可配置频率自动刷新（脚本扫描 Vault 统计 Inbox/成卷/归藏/典阁条目数并更新 HTML）。默认每天一次，用户可调整。手动触发：对 Agent 说"刷新看板"。
**重要**：看板需用浏览器打开（非 Obsidian HTML 插件），`obsidian://open?path=绝对路径` 链接在浏览器中完美工作。详见 `references/dashboard-lessons.md`。

#### 成卷（Article Generation）

1. **搭框架** — 标题方向（3选1）+ 章节结构
2. **确认** — 等待创作者确认标题和结构
3. **生成正文** — 确认后一次性生成完整文章
4. **建立卷结构** — 先 `ls` 列出 `03 成卷（项目）/` 下所有目录，取实际最大编号 +1（禁止靠速览或记忆推断——速览只显示 3 条，历史存在重复编号）。然后创建卷目录与标准文件（`创作过程：标题.md` + `正文：标题.md`）。完成后自动更新文境速览（`.canvas`），无需等待用户确认。
5. **更新来源状态** — 来源 Inbox `status` → `成卷`，建立双向链接，保留未选方向（依知识生命周期协议）

卷结构强制：
- 目录：`03 成卷（项目）/卷NNN · 标题简写/`
- 创作过程文件无需 `aliases`——Wikilink 直接用目标文件的完整文件名（含类型前缀，如 `[[正文：标题]]`）
- 禁止保存为成卷根目录下的扁平文件

#### 境·回溯 与 境·发布日志

卷目录下有两个子目录，用于写作风格的持续沉淀和迭代：

- **`境·回溯`**：放入过往文章（早期博客、旧作、外部发表等）。Agent 提取原生风格基因，作为个人写作的基准画像。
- **`境·发布日志`**：放入修改后发布版本的成卷文章。Agent 比照成卷初稿与发布版，学习微调偏好（段落格式、语调、结尾方式等），持续缩小生成与发布之间的差距。

**初始化检查**：共创模式下，进入 Conversation Runtime 前，Agent 必须检查 `03 成卷（项目）/境·回溯/`：

| 状态 | Agent 行为 |
|------|-----------|
| 有 `.md` 文件 | 逐篇阅读 → 提取关键字 → 创建 `[[wikilink]]` 双向链接 → 被引用笔记同步更新 `## References` |
| 目录为空 | 提示创作者放入过往独立文章，说明路径和作用，不阻塞流程 |

风格指南存放位置：`典阁/Library/创作体系/风格指南/`。

### 阶段 3B：开发模式（Development Mode）

读取 `04 Agent入口/04 开发入口（Development Entry）.md`，按顺序执行：

| 步骤 | 文档 |
|------|------|
| ① | 开发说明 |
| ② | ChatGPT Working Agreement v1.0 |
| ③ | Current Context Protocol |
| ④ | Current Context |
| ⑤ | Runtime State Check |
| ⑥ | Ready |

Runtime State：`Initial` → 首次 Session，不主动读取 Journal/RFC/Bug。`Active` → 恢复状态。

Session 结束时：更新 Current Context + 同步开发索引（如有新增 Convention/Bug/日志）。

## 核心原则

1. **第一个念头，永远是人的**：AI 不替创作者走出第一步。收录 = 创作者的第一判断，共创 = 创作者先看见连接，成卷 = 创作者确认标题。AI 帮你走得更远，但不替你产生第一个念头。
2. **协议驱动**：Agent 执行协议，不主动决定流程
3. **Design Review Mode**：结论在前，推导在后
4. **交付优先**：明确任务时直接提供可执行方案
5. **规范延续**：不重新设计已确认规范
6. **上下文校准**：不依赖推测
7. **一致性优先**：不因回答当前问题破坏既有系统一致性
8. **自主执行**：Agent 执行验证、编号校验、wikilink 扫描、速览更新等步骤时无需逐次等待用户确认。只交付最终结果，中间过程自动完成。

## 文件路径速查

| 文件 | 路径 |
|------|------|
| 文境入口 | `04 Agent入口/00 文境入口.md` |
| 模式选择 | `04 Agent入口/01 工作模式确认（Mode Selection）.md` |
| 共创入口 | `04 Agent入口/02 共创入口（Creator Entry）.md` |
| Workflow Index | `04 Agent入口/05 Workflow Index.md` |
| 开发入口 | `04 Agent入口/04 开发入口（Development Entry）.md` |
| Current Context | `06 文境开发/08 当前上下文/00 Current Context.md.md` |
| 开发索引 | `06 文境开发/00 开发索引.md` |
| 境层知识索引 | `02 养境（知识）/境层知识索引.md` |
| 典阁使用方式 | `02 养境（知识）/02 典阁/00 典阁使用方式.md` |
| 文境看板 | `文境看板.html`（浏览器打开）+ `文境速览.canvas`（Obsidian 原生） |
| 风格提取 Convention | `06 文境开发（Development）/02 开发规范(Convention)/11 风格提取 Convention.md` |
| 格式化标准 | `references/formatting-standard.md` — 成卷正文格式强制规范 |
| Bootstrap | `scripts/bootstrap.py` — 一键创建目录+文档+插件+配置 |
| Canvas 生成 | `E:\hermes\skills\productivity\wenjing\scripts\generate_canvas.py` — 生成 Obsidian Canvas 速览（不在本 skill 目录下，`skill_view` 无法访问，需用 `terminal` 直接运行。如脚本扫描路径不对，手动 `write_file` 重写整个 `.canvas`） |
| 看板刷新 | `E:\hermes\skills\productivity\wenjing\scripts\refresh_dashboard.py` — 更新 HTML 看板+Canvas 速览（同上，需 `terminal` 直接运行） |
| cua-driver 抓取中文平台 | `references/cua-scraping-chinese-platforms.md` — 知乎/简书/百家号自动化抓取方案 |

## 常见陷阱

1. **在模式选择前就开始索引文档** — 必须等待用户选择模式后再继续
2. **Current Context 为空时主动扫描 Development 文档** — Current Context Protocol 禁止此行为
3. **跳过 Runtime State Check** — 必须显式检查 `Runtime State` 字段
4. **Session 结束时忘记覆盖 Current Context** — 每次结束必须重新生成
5. **修改正式文档未经 Architecture Review** — 未经评审不得修改正式系统原则
6. **「从藏阁开始共创」AI 替创作者提炼方向** — 必须展示原文摘要，先问「你看到了什么」；AI 不先于创作者完成第一次模式识别。原"提炼 3 个方向"的做法已废弃——那等于 AI 替创作者走了第一步
7. **Reset 后引用前序对话** — 必须视为全新会话，不得搜索或引用前序内容
8. **Capture 输出跳过 Inbox Standard** — 必须先读取 Inbox Standard 再生成输出
9. **Inbox YAML 使用嵌套结构** — Obsidian Properties 只识别扁平键值对
10. **References 填入 Knowledge Map 节点** — 无关联时留空，不得填入 `[[AI]]` 等 KM 节点
11. **在 Vault 根目录新增文件或目录** — 绝对禁止，必须先向创作者确认位置
12. **批量修改同类文件前先询问** — 修改涉及同目录下多个同类文件时，必须先确认
13. **成卷后未维护 Inbox ↔ 成卷双向链接** — 来源 Inbox status → `成卷` + References 双向链接
14. **`sed -i` 在 Windows/MSYS 环境损坏文件** — 禁止对 Python 写入的 UTF-8 文件使用 sed；用 patch 或 Python open()
15. **`execute_code` 内 `read_file` 返回行号前缀** — 直接用 Python 原生 open() 代替
16. **Wikilink 未用完整文件名** — 必须用磁盘上的完整文件名（含类型前缀如 `[[正文：标题]]`），不用 aliases
17. **典阁变成第二个藏阁** — 入典前问「一年后还需要引用吗？」
18. **成卷编号未 ls 目录** — 创建新卷前必须先 `ls` 列目录取实际最大号+1，禁止靠速览或记忆推断
19. **文境速览各区域未遵守「最多 3 条」** — 最新成卷/藏阁标签/典阁入典各最多 3 条
20. **多次 patch 同一 Canvas JSON 导致损坏** — 改多个节点时用 `write_file` 重写整个文件
16. **Wikilink 未用完整文件名** — 引用任何 Vault 文件时，wikilink 必须用磁盘上的完整文件名（含类型前缀）。最常见错误：引用成卷正文时漏掉 `正文：` 前缀（`[[不要只是看穿]]` ❌ → `[[正文：不要只是看穿]]` ✅）。引用 Inbox 条目时漏掉类型标记（`[[自信是掌控感]]` ❌ → `[[【念】 自信是掌控感，焦虑是偷懒]]` ✅）。不要依赖 aliases——完整文件名可直接命中，不依赖 YAML 声明。创建链接前先确认目标文件的实际文件名。
17. **典阁变成第二个藏阁** — 典阁只收已验证、可长期复用的知识；灵感碎片、未经验证的观点留在藏阁。入典前问「一年后还需要引用吗？」
18. **试图在 Obsidian HTML 插件中让看板链接可点击** — 所有 Obsidian HTML 渲染插件（HTML Viewer / View Plus 等）都运行在沙箱 iframe 中，`obsidian://` 协议链接被阻断。这是插件安全设计，无法绕过。正确方案：用浏览器打开看板 + Obsidian 内用 `文境导航.md` 做 wiki 跳转。见 `references/dashboard-lessons.md`
19. **试图用 CSS Snippet 复刻看板布局** — Obsidian 默认样式与自定义 CSS 冲突严重，字体/间距失控。不要走这条路
20. **同一任务失败 3 次必须换方案** — 不反复修补同一个思路。调整 URI 格式/换插件/调 CSS 各尝试 1-2 次无效后，立即切换全局方案（如从"修复插件链接"切换到"浏览器打开看板"）。
21. **收录不确认收录策略** — 收录时必须先问收录策略（① 全文收入 ② AI摘要 ③ 仅索引），用数字选项让用户选择。不可跳过此步直接写入。
22. **SKILL.md 指令对单步写入描述模糊** — "将内容写入路径"会触发 Agent 走 execute_code 编脚本。必须写死工具名："直接用 `write_file`，不需要脚本"。
23. **用 HTML 做 Obsidian 内看板** — 已放弃。改用 Canvas（`.canvas` 文件），Obsidian 原生渲染，`[[wiki 链接]]` 直接可点，按状态分组展示全部 Inbox 条目。见 `scripts/generate_canvas.py`。
24. **用 `browser_navigate` 打开用户要看的本地文件** — `browser_navigate` 打开的是 Hermes 内置浏览器（Browserbase 远程渲染），用户看不到也无法直接交互。当用户要求"打开 PDF / 图片 / 文档"或"下载查看"时，必须用 `start "" "<绝对路径>"`（Windows）打开系统默认应用，让文件出现在用户的桌面上。`browser_navigate` 仅用于 Agent 需要抓取/解析的网页内容。
25. **Inbox 条目间未维护双向链接** — 当新收录的 Inbox 条目在 References 中链接了其他 Inbox 条目或成卷文件时，必须同步更新所有被引用条目的 References，添加反向链接。双向链接不是"成卷后"才做的事——任何新文档引用已有文档的瞬间，就应建立双向关系。
26. **典阁区域展示成卷或其他目录的文件** — 文境速览中「典阁 Library」区域的「最新入典」只能链接典阁目录（`02 养境（知识）/02 典阁/01 Library/`）中实际存在的文件，不得混入成卷、Inbox 或其他目录的内容。典阁展示的是已沉淀的知识资产，不是所有文章。先确认典阁目录下有什么文件，再决定展示什么。典阁条目不够时如实展示实际数量，不要用其他目录的内容填充。
27. **多次 patch 同一 Canvas JSON 文件导致损坏** — Canvas（`.canvas`）文件的 JSON 经过多次 `patch` 操作后容易出现转义符错乱（`\\n` 变成 `\\\n`）、花括号丢失等问题。需要修改多个节点时，直接用 `write_file` 重写整个文件内容，而不是逐个节点 patch。
28. **文境速览各区域未遵守「最多 3 条」规则** — 文境速览（`.canvas`）中三个展示区域均只保留最新 3 条：最新成卷（3 卷）、藏阁各状态标签（每标签 3 条 Inbox）、典阁最新入典（3 条）。标签格式为 `(3/X)` 显示当前/总数。新增条目时自动替换最旧的，保持清爽。
29. **成卷编号未实际检查目录** — 创建新卷前必须先 `ls` 列出 `03 成卷（项目）/` 下所有目录，取实际最大编号 +1。禁止靠速览或记忆推断——速览只显示 3 条、历史存在重复编号（卷006×2、卷010×2），仅凭记忆必出错。
30. **对中文反爬平台反复重试同一思路** — 知乎（zh-zse-ck）和百家号（需登录）的 curl + browser_navigate 各试一次即可。连续失败后按以下优先级降级：\n\n**三层降级链**：\n  ① **cua-driver `page get_text`**（首选自动化路径）：用 `start "" "URL"` 在用户本地浏览器打开文章 → 用 cua-driver 的 `page` 工具 `action=get_text` 提取全文 → 用 `ctrl+w` 关闭当前标签使 CDP 连接切换到下一个标签 → 循环提取。已验证对知乎、简书、百家号均有效。cua-driver 通过 `hermes computer-use install` 安装（需 VPN 访问 GitHub）。\n  ② **用户粘贴**（降级路径）：`start "" "URL"` 打开用户本地 Chrome → 请用户粘贴正文。\n  ③ **放弃该篇**（最终降级）：以上都不行时，不阻塞整体流程，用已有样本继续。\n\n**禁止**：换 header、换 API 端点、换 browser 参数反复撞墙
31. **成卷未用发布日志格式** — 禁用 `#` `##`，用 `> **粗体**` 分区，正文 4 空格缩进，子标题 8 空格缩进，长段落，全宽中文标点，结尾软着陆。详见 `references/formatting-standard.md`。——知乎的 zse-ck 是 JS challenge，不是 header 问题。各试一次 curl + browser_navigate 后立即切换到降级链。
32. **用 `skill_view` 加载 Canvas/看板脚本** — `generate_canvas.py` 和 `refresh_dashboard.py` 不在本 skill 的 `scripts/` 目录下，`skill_view(file_path='scripts/...')` 会返回 not found。正确做法：`terminal` 直接跑 `python "E:\hermes\skills\productivity\wenjing\scripts\generate_canvas.py"`。如脚本扫描了错误的 Vault 路径导致输出为空，不要反复调试脚本——直接 `write_file` 重写整个 `.canvas` 文件（见陷阱#20/#27）。