---
name: wenjing-protocol
description: Agent initialization and protocol-driven workflow for the 文境 (Wenjing) knowledge vault system. Covers entry protocol, mode selection, Development Runtime bootstrap, Current Context lifecycle, and protocol compliance rules.
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

1. **读取 Workflow Index**：`04 Agent入口/05 Workflow Index.md`。包含四个 Workflow 的触发条件：
   - **Capture**：收录、保存、记录、加入Inbox
   - **Organization**：整理、分类、重构
   - **Archive**：归档、收卷、完成项目
   - **Reflection**：反思、总结、Review、回顾

2. **进入 Conversation Runtime**（默认状态）。Agent 持续监听创作者任务，仅在 Trigger 出现时按需加载对应 Workflow。Workflow 完成后立即返回 Conversation Runtime。

3. **Lazy Loading 原则**：所有 Workflow 仅按需读取、按需执行。不主动加载任何未触发的 Workflow，不主动遍历 Vault。

初始化完成后进入 **Ready for Collaboration** 状态，等待创作者提出具体任务。

#### 藏阁（Inbox）交互规则

藏阁是文境的灵感收件箱，路径：`02 养境（知识）/01 藏阁/01 Inbox/`。

当用户要求「从藏阁开始共创」时：

1. **随机抽取 3 条灵感**（不列出全部条目）
2. **生成 3 个创作方向**——不是简单罗列标题和类型，而是基于每条灵感提炼出可讨论的创作方向（含方向名称和简要切入角度），确保方向差异足够大
3. 等待用户选择后，再读取具体内容展开

**严禁**：列出全部条目、逐条读取、只呈现标题+类型而不给方向、主动索引所有藏阁内容。藏阁的 AI 使用方式明确允许「随机抽取灵感进行讨论」，禁止「擅自决定灵感是否值得继续发展」。
**严禁**：列出全部条目、仅呈现标题而不生成方向、主动索引所有藏阁内容。藏阁的 AI 使用方式明确允许「随机抽取灵感进行讨论」，禁止「擅自决定灵感是否值得继续发展」。

#### Capture Workflow 细节

Capture Workflow 触发后按 Capture Convention 执行 Pipeline：

```
Trigger → Recognize Resource → Resource Registration → Creator Confirm Policy → Payload Acquisition → Knowledge Match → Metadata → Save → Return
```

**Capture 必读文档**（Workflow Index）：Capture Convention → Knowledge Map Convention → Knowledge Map → **Inbox Standard**。Inbox Standard 是 Capture Workflow 的**唯一输出契约**——文档命名、YAML frontmatter、章节结构均由其定义。**跳过 Inbox Standard 将导致输出格式不符合规范。**

**Policy 选项**：Index（仅索引）、Knowledge（索引+正文+摘要+AI洞察，默认）、Archive（索引+正文+摘要+AI洞察+图片+附件，完整离线存档）。Policy 名称以 `Resource Policy Standard` 为准。

**外部 URL**：curl 优先，遇到 CAPTCHA 或 JS 渲染页面（如微信公众号）尝试 browser。微信公众号等 JS 渲染页面的 curl 不可用，必须用 browser_navigate 获取 snapshot 中的正文。详见 `references/platform-capture-notes.md`。两者都失败时，按 Failure Rule 不阻塞 Capture——完成 Resource Registration 即视为成功，Payload 留空待后续补充。

**附件文件**：当用户通过 `@file:` 附加文件时，Payload Acquisition 直接使用附件内容，无需外部获取。附件路径通常为 `.hermes/desktop-attachments/`。

**KM 匹配**：当前 KM 节点有限（AI / Agent / 文境 / 主体性 / 创作 / Loop Engineering），非 AI/创作领域的文档通常无 Canonical 匹配。不匹配时不创建新节点，Tags 使用描述性标签，Related 留空或手动填写。新 Canonical 提案需创作者确认。

#### Inbox 输出格式（Inbox Standard）

Capture Workflow 的输出必须严格遵循 Inbox Standard。Agent 应按以下格式生成 Inbox 文档：

**文档命名**：`【类型】 标题.md`（如 `【摘】 一人运营20个AI账号，年收入317万.md`）

**YAML frontmatter**（全部扁平键值对，Obsidian Properties 可识别）：

```yaml
---
status: 待发展 | 共创中 | 成卷 | 已归档
type: 念 | 摘 | 事 | 梦 | 感 | 随 | 文 | 对 | 白 | 图
resource_url: （原始地址，仅当有真实 URL 时保留，空值则删除整行）
resource_capture_time: （收录时间，YYYY-MM-DD）
resource_policy: Index | Knowledge | Archive
tags:
  - （Obsidian tags，禁止 # 前缀）
publish_date: （发布时间，YYYY-MM-DD）
confidence: high | medium | low
---
```

> **禁止**：`resource_type`、`language`、`resource_id`、`resource_source`、`canonical`、`related`、`author` 字段不得出现在 YAML 中。这些字段已被移出 Inbox Standard。
>
> **禁止**：使用嵌套 YAML（如 `resource:` 下缩进子字段）。Obsidian Properties 只识别扁平键值对，嵌套对象在属性面板中不可见、不可查询。
>
> **`resource_url` 规则**：有真实 URL 时保留，为空或仅含占位文本时删除整行。不得保留 `resource_url:` 空行或填入 `（原始链接未记录）` 等占位文本。

**正文章节**：`# 【类型】 标题` → `## Resource` → `## Original Content` → `## Summary` → `## Insight` → `## References`

### 阶段 3B：开发模式（Development Mode）

读取 `04 Agent入口/04 开发入口（Development Entry）.md`，按顺序执行：

| 步骤 | 文档 | 路径 |
|------|------|------|
| ① | 开发说明 | `06 文境开发（Development）/00 开发说明(Working Agreement)/开发说明.md` |
| ② | ChatGPT Working Agreement | `06 文境开发（Development）/01 开发协议(protocol)/ChatGPT Working Agreement v1.0.md` |
| ③ | Current Context Protocol | `06 文境开发（Development）/01 开发协议(protocol)/02 Current Context Protocol.md` |
| ④ | Current Context | `06 文境开发（Development）/08 当前上下文(Current Context)/00 Current Context.md.md` |
| ⑤ | Runtime State Check | 检查 Runtime State 字段：`Initial` → 首次 Session，`Active` → 恢复状态 |
| ⑥ | Ready | 等待开发任务 |

### Runtime State Check 规则

读取 Current Context 的 `Runtime State` 字段：
- **`Initial`**：首次 Development Session。**不主动读取** Journal、RFC、Bug、Architecture Review 恢复状态。
- **`Active`**：恢复开发状态，根据 Current Context 记录的进度继续。

### Ready 状态规则

初始化完成后，按需加载（Lazy Loading）：
- ✅ 可以读取：用户明确要求的文档
- 🚫 不主动读取：Development Journal、RFC、Bug、Architecture Review

## Development Session 生命周期

```
读取 Current Context → 恢复状态 → Development Session → 覆盖更新 Current Context → 结束
```

### 结束 Session 时

按 Current Context Protocol 生成新的 Current Context，覆盖旧版本。必须包含：
- `Runtime State`：`Active`
- 当前开发目标
- 当前开发阶段
- 当前完成进度
- 下一步工作
- 推荐继续阅读

**同步开发索引**：若 Session 中新增或修改了 Convention / Bug / 开发日志，必须同步更新 `00 开发索引.md`，避免开发文档成为孤岛。

## 核心原则

### ChatGPT Working Agreement 关键规则

1. **冻结原则（Rule 0）**：已确认通过的设计视为冻结规范，不重新设计
2. **协议优先**：每次进入新会话先按协议工作
3. **Design Review Mode**：结论在前，推导在后
4. **交付优先**：明确任务时直接提供可执行方案
5. **规范延续**：不重新命名、重新编号或重新设计已确认规范
6. **上下文校准**：不假设已理解整个系统，不依赖推测
7. **一致性优先**：不因回答当前问题破坏既有系统一致性

### 显式状态原则

从 Bug-001 学到的教训：
- **禁止隐式信号**：不用"空 = Initial"这类推导
- **要求显式字段**：状态必须写在文件里，Agent 读到的就是状态本身
- **种子文件**：预置初始状态，不让任何状态文件以空文件形式存在

## 文件路径速查

所有路径相对于 `E:\文境vault\文境Vault\`：

| 文件 | 路径 |
|------|------|
| 文境入口 | `04 Agent入口/00 文境入口.md` |
| 模式选择 | `04 Agent入口/01 工作模式确认（Mode Selection）.md` |
| 共创入口 | `04 Agent入口/02 共创入口（Creator Entry）.md` |
| Workflow Index | `04 Agent入口/05 Workflow Index.md` |
| 开发索引 | `06 文境开发（Development）/00 开发索引.md` |
| 开发入口 | `04 Agent入口/04 开发入口（Development Entry）.md` |
| 开发说明 | `06 文境开发（Development）/00 开发说明(Working Agreement)/开发说明.md` |
| Working Agreement | `06 文境开发（Development）/01 开发协议(protocol)/ChatGPT Working Agreement v1.0.md` |
| Current Context Protocol | `06 文境开发（Development）/01 开发协议(protocol)/02 Current Context Protocol.md` |
| Current Context | `06 文境开发（Development）/08 当前上下文(Current Context)/00 Current Context.md.md` |
| Bug 目录 | `06 文境开发（Development）/04 Bug/` |

## 常见陷阱

### 共创讨论规则

Creator Mode 下 Agent 提供选项而非结论。关键模式：

- **方向选择**：每次提供 **2-3 个方向选项**，编号呈现，方向差异足够大，交还选择权
- **不主动收束**：不主动总结、不定性结论、不替创作者决定方向
- **追问优先于回答**：多问「你想往哪个方向走」，少给「最佳方案是」

### 成卷（Article Generation）

当讨论深入、素材足够时，创作者可能说 **「成卷」**，表示进入文章生成阶段。

**流程**（遵循《成卷 Convention》与《知识生命周期协议》）：

1. **搭框架** — 根据讨论内容提炼标题方向（3 选 1）+ 章节结构
2. **确认** — 等待创作者确认标题和结构
3. **生成正文** — 确认后一次性生成完整文章
4. **建立卷结构** — 按《成卷 Convention》创建卷目录与标准文件
5. **更新来源状态** — 来源 Inbox `status` → `成卷`，建立双向链接，**保留未选方向**（共创中未被选择的思考方向追加到 Inbox 原文末尾）

**卷结构要求**（强制）：

- 目录：`03 成卷（项目）/卷NNN · 标题简写/`
- 必建文件：`创作过程：标题.md`（元数据+共创记录）、`正文：完整标题.md`
- **禁止**：将文章保存为成卷根目录下的扁平 `.md` 文件
- **禁止**：跳过卷目录创建或省略创作过程文件

**成卷 ≠ 用完**：共创讨论中可能有多个方向，选了一个成卷，其余有价值的思考方向应作为「待继续思考」保留在来源 Inbox 正文中。灵感不是一次性的。

**注意**：成卷不是 Workflow（不触发 Lazy Loading），而是 Creator Mode 内的一个操作阶段。生成完成后返回 Conversation Runtime。详细规范见 `08 成卷 Convention.md` 与 `09 知识生命周期协议.md`。

## 参考文件

- `references/dev-init-checklist.md` — Development Runtime 初始化检查清单
- `references/bug-001-implicit-signal-elimination.md` — 隐式信号消除模式（Bug-001 修复记录）
- `references/ai-mirror-discussion.md` — AI 作为认知镜子的讨论模式与案例
- `references/inbox-standard-compliance.md` — Inbox Standard 输出合规检查清单
- `templates/ai-collaboration-self-assessment.md` — AI 协作自评表模板（追问深度/推翻率/残留率/控制变量法）
- `references/08-rollup-convention-latest.md` — 成卷 Convention 最新版摘要

## 常见陷阱

1. **在模式选择前就开始索引文档** — 必须等待用户选择模式后再继续
2. **Current Context 为空时主动扫描 Development 文档** — Current Context Protocol 禁止此行为（Bug-001）
3. **跳过 Runtime State Check** — 必须显式检查 `Runtime State` 字段
4. **Session 结束时忘记覆盖 Current Context** — 每次结束必须重新生成
5. **修改正式文档未经 Architecture Review** — Development 模式下，未经评审不得修改正式系统原则
6. **「从藏阁开始共创」仅列标题而不生成方向** — 用户说「从藏阁开始共创」后，Agent 必须：随机抽取 3 条灵感→快速读取内容→提炼核心主题→生成 3 个**创作方向**（每个含引人思考的标题、灵感来源标注、可深入的角度）。**仅呈现标题+类型**等于让用户做 Agent 本应完成的提炼工作，违反共创模式「AI 提供选项，人选择方向」的原则。
7. **Reset 后引用前序对话** — 用户说「删除上下文记忆」「删除本轮上下文」「恢复到初始状态」后，必须视为全新会话。不得搜索前序对话中创建的文件、引用前序讨论的话题。即使记得也必须当作不知道。
8. **Capture 输出跳过 Inbox Standard** — Capture Workflow 必须读取 Inbox Standard 再生成输出。根因通常是 Workflow Index 未列入 Inbox Standard 或 Agent 未按列表加载。
9. **Inbox YAML 使用嵌套结构** — Obsidian Properties 只识别扁平键值对。所有字段必须展平为顶层键值对。
10. **References 填入 Knowledge Map 节点** — `## References` 应指向 vault 中实际存在的关联文档。无关联时留空，不得填入 KM 节点（如 `[[AI]]`）作为替代。
11. **在 Vault 根目录新增文件或目录** — 绝对禁止。必须先向创作者提出并等待确认位置。
12. **批量修改同类文件前先询问** — 修改涉及同目录下多个同类文件时，必须先确认是否同步修改。
13. **成卷后必须维护 Inbox ↔ 成卷双向链接** — 每次成卷后检查：来源 Inbox 的 `## References` 是否已添加指向该卷的 `[[双向链接]]`，以及 Inbox 间的衍生关系是否已录入。成卷完成后来源 Inbox 的 `status` 应更新为 `成卷`（依知识生命周期协议）。同时，在卷的 `创作过程` 文件中建立指向来源 Inbox 的反向链接。

14. **禁止 `sed -i` 修改 Python 写入的文件** — Windows/MSYS 环境下，`sed -i` 对 Python 写入的 UTF-8 文件进行原地修改可能导致内容截断（仅残留 `## References` 段）。替代方案：使用 `patch` 工具进行精确替换，或使用 Python `open(path, 'w', encoding='utf-8')` 直接写入。

15. **`execute_code` 内 `read_file` 返回行号前缀** — `read_file(path).get('content')` 返回 `LINE|CONTENT` 格式文本，直接写回文件会将行号嵌入正文。在 execute_code 内读写文件时，用 Python 原生 `open(path, 'r', encoding='utf-8')` 代替。

16. **卷文件重命名导致 [[wikilink]] 断裂** — 成卷 Convention 将文件从数字前缀（`00 项目首页.md`）改为语义前缀（`创作过程：标题.md`）后，Vault 中指向旧名的 wikilink 会断裂。解决方案：在创作过程文件 YAML 中声明 `aliases`（如 `aliases: [主题简称, 卷NNN]`），Obsidian 自动匹配。

14. **Windows 文件操作陷阱** — MSYS `sed -i` 修改 Python 写入的 UTF-8 文件会导致内容截断。`execute_code` 内 `read_file().get('content')` 返回带行号前缀的内容，直接写回会污染文件。**正确做法**：内容修改用 `patch` 工具或 Python `open()`；批量重命名用 `mv`；状态字段修改用 `patch` 的 `replace` 模式。

15. **卷文件重命名后旧 wikilink 断裂** — 卷目录下文件名变更后，所有指向旧文件名的 `[[wikilink]]` 全部失效。**解决方案**：在卷的 `创作过程` 文件 frontmatter 中声明 `aliases`（含主题简称和卷编号），使旧链接通过别名自动解析。
14. **禁止 `sed -i` 修改 Python 写入的 .md 文件** — Windows MSYS/git-bash 的 `sed -i` 对 Python `write_file` 写入的 UTF-8 文件处理异常，会导致内容被截断。修改文件内容统一使用 `patch` 工具或 Python `open(path, 'w', encoding='utf-8')`。
15. **execute_code 内 read_file 返回带行号的内容** — Python 沙箱内的 `read_file().get('content')` 返回 `LINE|CONTENT` 格式，直接写回会将行号嵌入正文，导致文件污染。execute_code 内读取文件内容应使用 Python `open()` 直接读取，而非通过 hermes_tools 的 `read_file`。对含特殊字符的路径，`read_file` 还可能返回空，写入前必须验证内容非空。
16. **成卷后 Inbox 内容不可删除** — `status` 改为 `成卷` 仅更新状态，不删除、不清空、不截断 Inbox 原文。成卷 ≠ 用完。共创讨论中被放弃的方向应以「待继续思考」形式追加到原文末尾。