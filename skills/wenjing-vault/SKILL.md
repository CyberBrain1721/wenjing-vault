---
name: wenjing-vault
description: Use when the user asks an Agent to enter, initialize, test, install, or collaborate inside a Wenjing local Obsidian Vault; when the user mentions 文境, Wenjing, Agent入口, 境·回溯, 藏阁, Capture, or protocol-driven Obsidian collaboration. This skill enforces the local-first Wenjing v0.2.0 entry path: read the Agent入口, do not traverse the whole Vault, initialize Creator Runtime, check 境·回溯, and only enter Workflows when triggered by the creator.
---

# Wenjing Vault Skill

Wenjing is not an AI product, cloud workspace, or a Codex-specific project.

Wenjing is a local-first Obsidian creative system.

The Agent is only a temporary collaborator that enters the Vault through a unified protocol.

## Core Rule

When working with a Wenjing Vault, this Skill does not replace the Vault protocols.

This Skill only tells the Agent how to enter the Vault safely.

The Vault protocols remain the authority.

## Trigger

Use this Skill when the user asks for any of the following:

- enter Wenjing / 进入文境
- open or initialize a Wenjing Vault
- use `Agent入口`
- test whether an Agent can access Wenjing
- clone or install `https://github.com/CyberBrain1721/wenjing-vault`
- work with `境·回溯`
- 收录 / 保存 / 记录下来 / 加入 Inbox / Capture / 保存到藏阁
- 整理 / 分类 / 重构 / 归档 / 复盘
- protocol-driven Obsidian collaboration

## Obsidian 环境检测

文境的本体是本地 Obsidian Vault。Agent 在与 Vault 交互前，应先确认宿主环境已安装 Obsidian。

### 检测

检查宿主环境是否已安装 Obsidian：

- Windows：`%LOCALAPPDATA%\Obsidian\Obsidian.exe` 或开始菜单项
- macOS：`/Applications/Obsidian.app`
- Linux：`obsidian` 命令或 `/usr/bin/obsidian`
- 或检测 `obsidian://` 协议是否可调用

### 若本地未安装

从 Obsidian 官网下载并安装：

```text
https://obsidian.md/download
```

- 优先使用系统包管理器（`brew install --cask obsidian` / `winget install Obsidian.Obsidian`）或官网安装包。
- 若 Agent 运行环境无权执行安装，必须明确提示用户访问上述官方链接完成安装，不得静默跳过或假定已就绪。

### 加载插件

安装完成后，确保 Vault 启用 `Obsidian 插件清单.md` 所列社区插件：Startpage、HTML Viewer +、Select Folder、Editing Toolbar、Full Calendar、Style Settings、PDF +、Notebook Navigator。

- 若插件未启用：进入 `设置 → 社区插件`，逐一启用；或直接以启用状态写入 `.obsidian/community-plugins.json`。
- 仅在 Vault 首次初始化或创作者确认时执行此步，不要每次进入都重写插件配置。

## If The Vault Is Not Present

If the user asks to download or install Wenjing and no local Vault path is available, clone:

```bash
git clone https://github.com/CyberBrain1721/wenjing-vault.git
```

After cloning, treat the cloned folder as the local Obsidian Vault.

Do not assume the clone path. Confirm or infer the local folder path from the command result or user-provided path.

## If The Vault Path Is Present

The Agent must begin from the local Vault folder.

Do not recursively scan the whole Vault.

Do not infer the current task from file names.

Do not read Inbox, 成卷, 归藏, 典阁, or the whole Vault unless a protocol explicitly requires it.

## Mandatory Entry Sequence

Read these files in order from the Vault root:

```text
04 Agent入口/00 文境入口.md
04 Agent入口/01 Agent 接入总则.md
04 Agent入口/02 共创入口（Creator Entry）.md
04 Agent入口/05 Workflow Index.md
```

The Agent must follow the files as protocol nodes, not as background documentation.

## Runtime Initialization

After reading `05 Workflow Index.md`, check:

```text
03 成卷（项目）/境·回溯/
```

If `.md` files exist there, perform the `境·回溯` initialization described in `02 共创入口（Creator Entry）.md`.

If no `.md` files exist, give the creator the short `境·回溯` prompt from `02 共创入口（Creator Entry）.md`, then continue.

After initialization, report only the runtime state:

```text
Mode: Creator
Runtime: Conversation Runtime
Current Workflow: None
Status: Ready
```

Then wait for the creator's next task.

## Workflow Rule

The Agent must stay in Conversation Runtime unless the creator triggers a Workflow.

Workflow triggers are defined by:

```text
04 Agent入口/05 Workflow Index.md
```

Do not invent Workflow triggers.

Do not enter a Workflow because it seems useful.

Do not continue reading Workflow conventions after the current Workflow exits.

## Capture Workflow

When the creator says 收录, 保存, 记录下来, 加入 Inbox, Capture, or 保存到藏阁, enter Capture Workflow.

Before executing Capture, read:

```text
04 Agent入口/10 Capture Convention.md
04 Agent入口/12 Knowledge Map Convention.md
02 养境（知识）/00 知识目录/00 知识地图Knowledge Map.md
04 Agent入口/11 Inbox Standard.md
```

Capture must create a Resource Registration before saving payload.

Default target path:

```text
02 养境（知识）/01 藏阁/01 Inbox/
```

After Capture, immediately exit the Workflow and restore:

```text
Runtime: Conversation Runtime
Current Workflow: None
```

## Boundary

The Agent may:

- read required protocol files
- initialize Runtime
- execute a creator-triggered Workflow
- create files when the active protocol requires it
- suggest possible tags, titles, or canonical matches

The Agent must not:

- treat Wenjing as an AI app or model-specific workspace
- traverse the entire Vault by default
- replace the creator's decisions
- decide the creator's direction
- promote a note to 成卷 or 已归档 without confirmation
- evaluate creator maturity or build a Creator Profile
- change system protocols unless the user explicitly asks to develop Wenjing itself

## Version

This Skill targets Wenjing Vault v0.2.0:

- unified Agent entry
- Creator Runtime
- `境·回溯` initialization
- Capture Workflow
- Knowledge Map matching
- Inbox Standard

