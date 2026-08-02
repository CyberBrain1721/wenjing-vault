# Wenjing Vault Skill

This folder packages Wenjing Vault v0.2.0 as an Agent-readable Skill.

Wenjing is a local-first Obsidian creative system. It is not bound to Codex, WorkBuddy, OpenClaw, or any single AI environment.

## Install / Use

> The Agent will first verify Obsidian is installed locally (official download: https://obsidian.md/download). If absent, it guides installation and loads the community plugins listed in `Obsidian 插件清单.md`.

An Agent that supports Skills should read:

```text
skills/wenjing-vault/SKILL.md
```

Then it should enter the Vault through:

```text
04 Agent入口/00 文境入口.md
```

## Test Prompt

Give any Agent this prompt:

```text
请下载这个本地 Obsidian 创作系统：

https://github.com/CyberBrain1721/wenjing-vault.git

下载后不要遍历整个 Vault。
请先读取：

skills/wenjing-vault/SKILL.md

然后按照 Skill 指令读取：

04 Agent入口/00 文境入口.md

文境不是某个 AI 环境的项目，它的本体是本地 Obsidian Vault。
你只是接入者，必须按统一 Agent 入口执行。
```

## Version

Skill target: Wenjing Vault `v0.2.0`

