---
title: "Understanding CLI-Based AI"
teaching: 15
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Compare CLI and Browser-based AI tools.
- Create a project context file.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Why use a CLI for AI instead of a browser?
- What is the GEMINI.md file?

::::::::::::::::::::::::::::::::::::::::::::::::::

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

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Your First AI CLI Command

Let's verify the tool is working and see how it interacts with your system. In your terminal, run the following command:

```bash
gemini "Tell me what operating system I am currently using and list the files in this directory."
```

Compare the output to what you see when you run `ls` (or `dir` on Windows) and `uname -a`. Did the AI accurately describe your environment?

::::::::::::::::::::::::::::::::::::::::::::::::::

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

:::::::::::::::::::::::::::::::::::::::: solution

## Example GEMINI.md

```markdown
# Project: Arctic Sea Ice Analysis

## Goal
To analyze trends in sea ice extent using satellite data from 1980-2020.

## Tech Stack
- Python 3.9
- Libraries: xarray, pandas, matplotlib, cartopy

## Conventions
- Use snake_case for variable names.
- Include docstrings for all functions.
- Save all plots to the `figures/` directory.
```

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

## Key Points

- CLI tools can edit files directly.
- Persistent context in GEMINI.md improves AI performance.

::::::::::::::::::::::::::::::::::::::::::::::::::
