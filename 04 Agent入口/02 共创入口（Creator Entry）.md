# Runtime Initialization

完成基础协议阅读后。

Agent 应正式建立 Creator Runtime。

Creator Runtime 是整个共创过程的默认运行环境。

进入 Runtime 后。

Agent 应立即读取：

> 04 Agent入口 / 05 Workflow Index

Workflow Index 用于定义 Creator Runtime 中所有可用 Workflow 的触发条件。

Workflow 不属于初始化流程。

Workflow 不属于工作模式。

Workflow 仅在创作者提出对应任务时，由 Runtime 自动触发。

---

# 境·回溯检查

完成 Workflow Index 加载后，进入 Conversation Runtime 前。

Agent 应检查 `03 成卷（项目）/境·回溯/` 目录。

## 有回溯文件

若境·回溯目录中存在 `.md` 文件，Agent 应执行风格初始化：

1. 逐篇阅读回溯中的所有文档
2. 提取关键字，创建指向 Vault 内已有笔记的双向链接（`[[wikilink]]`）
3. 被链接的笔记同步更新 `## References`

风格初始化完成后，Agent 对创作者的语气、结构、偏好建立初始理解。此理解在后续共创中作为风格参考，不替代创作者决策。

## 无回溯文件（首次进入文境）

若境·回溯目录为空：

Agent 应给出以下提示：

> 📌 **境·回溯** 是文境的风格学习通道。
>
> 将你过去独立完成的文章放入 `03 成卷（项目）/境·回溯/` 目录，Agent 可以从中学习你的原生写作风格，在共创时更贴合你的语气。
>
> 不需要 AI 协作过的产物——你独自写的影评、散文、日记、知乎回答都可以。
>
> 跳过不影响当前使用，随时可以补入。

提示后，继续进入 Conversation Runtime。

---

完成 Workflow Index 加载后。

Agent 默认进入：

Conversation Runtime。

Conversation Runtime 是 Creator Mode 的默认运行状态。

进入 Conversation Runtime 后。

Agent 应持续关注创作者当前任务。

除非检测到 Workflow Trigger。

否则不得主动加载任何 Workflow。

不得主动读取 Development 文档。

不得主动读取 Knowledge Convention。

不得主动遍历 Inbox、成卷、归藏或整个 Vault。

所有 Workflow 均采用 Lazy Loading 原则。

仅在 Trigger 出现时加载对应 Convention。

Workflow 执行完成后。

Agent 应立即退出 Workflow。

恢复：

Conversation Runtime。

Current Workflow：

None。

---

# Runtime State

Mode：

Creator

Runtime：

Conversation Runtime

Current Workflow：

None

Status：

Ready