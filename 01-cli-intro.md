---
title: "CLI-based AI"
teaching: 15
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Compare CLI and browser-based AI tools.
- Create a 'Living Spec' (AGENTS.md) to guide an agent.
- Explain the shift from writer to orchestrator.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Why use a CLI for AI instead of a browser?
- What is the AGENTS.md file?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Setup check
Before starting, ensure all learners can authenticate. There are two paths:

- **API key**: Ask them to run `echo $GEMINI_API_KEY`. If it returns a blank line, they need to run the export command again.
- **Google account (OAuth)**: Learners who authenticated via `gemini auth login` will not have an API key set — this is fine. Ask them to run `gemini --version` to confirm the tool is working.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Why CLI matters for research

Most researchers use chat-based AI in a browser. These tools are good for brainstorming but run in an isolated sandbox. They cannot see your files, run your code, or understand your project structure without manual uploads.

CLI tools run in your terminal and have access to your project's file system. They can read data, write scripts, and execute commands. This turns the AI into a research assistant that can iterate on tasks within your working environment.

::::::::::::::::::::::::::::::::::::::::: caution

## Data privacy and institutional context

The University of California and many other campuses have enterprise agreements with AI vendors like OpenAI and Google. These agreements usually state that your data will not be used to train public models.

However, CLI or API access under these agreements is not always documented. Campus IT often needs to provision this access, and terms can vary. Verify with your institution whether your license covers both web interfaces and CLI/API access.

**Warning:** Personal accounts may allow CLI/API usage but often lack the privacy protections of institutional licenses. Consult your campus IT policy before using AI tools with sensitive data.

**Looking ahead:** If your research requires absolute privacy, these skills transfer to open LLMs (like Gemma or Llama) run locally via Ollama.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Shift from writer to orchestrator

Traditional programming requires you to remember the syntax and logic of a script. **Spec-Driven Research Orchestration** offloads syntax generation to the AI, letting you focus on the high-level logic and the **Living Spec**.

```mermaid
graph TD
    A[Researcher/Orchestrator] -->|High-Level Goal| B(AGENTS.md: The Living Spec)
    B -->|Spec + Data| C(AI Agent)
    C -->|Draft Code/Update| D{Verification}
    D -->|Passed| E[Final Output]
    D -->|Failed| F[Refinement]
    F --> B
    style D fill:#f9f,stroke:#333,stroke-width:2px
```

::::::::::::::::::::::::::::::::::::::::: instructor

## Discussion prompt
Ask learners: "Have you ever used ChatGPT to write code that looked correct but failed when you ran it?"
This is a good time to introduce the concept of orchestration. The goal is not just to "fix" code, but to ensure the AI's *intent* (the spec) is correct.

::::::::::::::::::::::::::::::::::::::::::::::::::

This introduces a new challenge: **verification load**. You must coordinate and validate the agent's actions against your requirements.

::::::::::::::::::::::::::::::::::::::::: callout

## Managing cognitive load

It is common to feel "out of the loop" when the AI generates many lines of code quickly. To manage this, focus on anchoring your understanding. Read the comments the AI generates and test small pieces of code frequently. If a block of logic is confusing, ask the AI to explain it before moving on.

::::::::::::::::::::::::::::::::::::::::::::::::::

## File system access

Unlike browser tools, the Gemini CLI has access to your working environment. It can read project context from the directory structure and modify files. Instead of copying and pasting code, the agent writes scripts to your disk and can iterate based on terminal errors.

::::::::::::::::::::::::::::::::::::::::: caution

## Security responsibility

Giving an AI agent access to your filesystem is a security responsibility. A buggy or misaligned agent could delete files or access sensitive data like `.ssh` keys or `.env` files.

### Mitigating risk with sandboxing

Sandboxing runs the AI tool in a restricted environment where it can only see and modify specific files.

In this lesson, we use Docker to create a sandbox. When you run the agent inside a Docker container:
1.  **Isolation**: The agent is isolated from your personal files and operating system.
2.  **Controlled access**: You choose which folder the agent can see by mounting it as a volume.
3.  **Safe failure**: If the agent runs a destructive command, it only affects temporary files inside the container.

Always consider the blast radius of your tools. Ensure files are backed up or under version control (like Git) so you can revert unwanted changes.

::::::::::::::::::::::::::::::::::::::::::::::::::

### Long context

Models like Gemini 2.5 have a long context window of 1 million to 2 million tokens. You can provide the AI with your entire project folder—scripts, documentation, and small datasets—at once.

This allows you to describe the desired state of your project, and the agent coordinates changes across multiple files. In a research context, this is declarative programming with AI agents.

::::::::::::::::::::::::::::::::::::::::: caution

## Context poisoning

Large context windows carry a risk of context poisoning. If your directory contains old scripts or contradictory documentation in an `/archive` folder, the AI may hallucinate based on that outdated information.

**Best practice:** Use explicit scoping. Tell the agent: "Ignore the `/archive` folder and only consider `.py` files in the `src/` directory."

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## How much context is enough?

More context is not always better. Attention quality can degrade when the context window is very full — the model may lose track of information buried in the middle. A rough guide for research projects:

| Project size | What to include | What to exclude |
|---|---|---|
| Small (< 10 files) | Everything | Nothing — just start |
| Medium (10–50 files) | Spec + files relevant to the current task | Archives, unrelated scripts, raw data |
| Large (50+ files) | Explicit file references per task | Everything else |

For research data specifically: never load full datasets. Provide a schema, column list, or the first few rows instead. If the agent starts making errors that feel like it "forgot" earlier instructions, that is often a sign the context is too large and diluted — try starting a fresh session with tighter scoping.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Starting a Gemini CLI session

Navigate to your project folder in the terminal, then run `gemini` with no arguments to open an interactive session:

```bash
cd path/to/your/project
gemini
```

The CLI loads your `GEMINI.md` automatically if one exists, then displays a prompt where you type requests directly. To exit at any time, type `exit` or press Ctrl+D.

::::::::::::::::::::::::::::::::::::::::: callout

## Working directory matters

Always start the Gemini CLI from inside your project folder. The agent uses the current directory to find your files and spec. Starting from the wrong folder — such as your home directory — is one of the most common sources of confusion in a workshop.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Your first AI CLI command

Navigate to your project folder and start a session:

```bash
cd path/to/your/project
gemini
```

Once the CLI is running, type the following prompt and press Enter:

```
Tell me what operating system I am currently using and list the files in this directory.
```

Compare the output to what you see when you run `ls` (or `dir` on Windows) and `uname -a`. Did the AI accurately describe your environment?

:::::::::::::::::::::::::::::::::::::::: solution

## Example output

The AI should return a response similar to:

"You are currently using macOS (Darwin). The files in this directory are: 
- index.md
- config.yaml
- episodes/
- data/
..."

### Reflection
- Did the AI see files that you didn't manually upload?
- How does this change your approach to copying and pasting code?

::::::::::::::::::::::::::::::::::::::::: callout

## Note on variations

The AI's exact wording will vary, but it should correctly identify your OS and the files in your folder.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## The Living Spec

To get the most out of a CLI agent, provide it with persistent context about your project. This acts as a "Living Spec"—a set of rules and goals the agent must follow across every session.

Every major CLI tool has its own **native** spec file that it loads automatically when you start a session:

| Tool | Native spec file | Auto-loaded? |
|---|---|---|
| Gemini CLI | `GEMINI.md` | Yes |
| Claude Code | `CLAUDE.md` | Yes |
| OpenAI Codex | `AGENTS.md` | Yes |
| Cursor | `.cursorrules` | Yes |

You can also use a **portable** spec file—`AGENTS.md` is a common convention—that you explicitly reference in any prompt: `"Read AGENTS.md and then..."`. It is not auto-loaded by any single tool, but it travels with your project if you switch tools.

::::::::::::::::::::::::::::::::::::::::: callout

## Which approach should you use?

- **Stick with one tool?** Use the native file (`GEMINI.md` here) for a smoother experience — you never have to mention it in your prompts.
- **Move between tools?** Keep a portable `AGENTS.md` and reference it explicitly. The spec stays the same; only the tool changes.

For this lesson we use `GEMINI.md` as the native file. The same content and concepts apply if you switch to any other tool.

::::::::::::::::::::::::::::::::::::::::::::::::::

### Initialize your project

The Gemini CLI includes an `init` command that creates a `GEMINI.md` template in your working directory:

```bash
gemini init
```

This generates a starter file with placeholder sections for you to fill in. Open it in any text editor to customize it for your project.

### What to include in your spec file

Use this file to define:

- **Current Goal**: What you are working on right now.
- **Rules of the Road**: Technical constraints (e.g., "Always use `pandas` for dataframes").
- **Verification Gates**: How you will confirm the code is correct.

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Initialize and customize your spec file

In your project directory, run `gemini init` to create a `GEMINI.md` file. Then edit it to define one "Hard Constraint" (something the AI *must* do) and one "Success Metric" (how you know it's done).

:::::::::::::::::::::::::::::::::::::::: solution

## Example spec file

```markdown
# Project: Arctic Sea Ice Analysis

## Goal
To analyze trends in sea ice extent from 1980-2020.

## Rules of the Road
- **Hard Constraint**: Only use the `xarray` library for spatial data processing.
- **Success Metric**: All final plots must include a valid DOI reference for the data source.

## Conventions
- Use snake_case for variable names.
- Save all plots to the `figures/` directory.
```

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- CLI agents coordinate actions across multiple files.
- Run `gemini init` to create a `GEMINI.md` Living Spec that reduces "context drift."
- A portable `AGENTS.md` lets the same spec travel across different AI tools.
- Research orchestration shifts focus from writing syntax to validating intent.

::::::::::::::::::::::::::::::::::::::::::::::::::
