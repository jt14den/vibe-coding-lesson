---
title: "Understanding CLI-Based AI"
teaching: 15
exercises: 10
---

## Why CLI Matters for Research

Most researchers are familiar with chat-based AI in a browser. However, for coding and data analysis, CLI-based tools offer significant advantages.

| Feature | Browser-Based AI | CLI-Based AI |
| :--- | :--- | :--- |
| **Interface** | Conversation in browser | Runs in your terminal |
| **File Access** | Manual copy-paste/upload | Reads/writes files directly |
| **Context** | Limited context window | Larger persistent memory |
| **Execution** | You run the code | AI runs code and sees results |
| **Autonomy** | One response at a time | Autonomous multi-step execution |

## The Power of the File System

CLI tools like the Gemini CLI can:
1. **Read** any file in your project directory.
2. **Create** new scripts, data files, or configurations.
3. **Iterate** automatically based on terminal errors.
4. **Maintain** context across long sessions.

## Project Context: GEMINI.md

To get the most out of a CLI agent, you should provide it with persistent context about your project. By creating a `GEMINI.md` file in your project root, you can define:
- Project goals.
- File structure overview.
- Tech stack (libraries/dependencies).
- Coding conventions.
- Specific constraints (e.g., "always use type hints").

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Create your GEMINI.md

In your project directory, create a file named `GEMINI.md` and add a brief description of a research project you are working on. Include at least two libraries you use and one coding convention (e.g., "Use snake_case for functions").

::::::::::::::::::::::::::::::::::::::::::::::::::
