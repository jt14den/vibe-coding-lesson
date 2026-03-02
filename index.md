---
title: "Agentic Research Workflows: Orchestrating AI and Validation"
start: true
---

### Natural-language specifications, CLI agents, and a three-layer validation stack

This lesson introduces researchers to **Agentic Research Workflows**, a paradigm shift in how we write and maintain research software. By leveraging AI coding agents, we move from **Imperative Programming** (writing every line of syntax) to **Declarative Orchestration** (defining intent and verifying outcomes).

The focus is not on replacing research thinking, but on reducing the cost of turning research intent into runnable, inspectable code, while maintaining rigorous standards for **correctness, validation, and reproducibility**.

## From "Vibe Coding" to Validated Workflows

The term **"Vibe Coding"** (coined by Andrej Karpathy) describes the early 2023-2024 shift toward guiding AI with natural-language prompts. While "the vibe" is where we start, research demands more than intuition. This lesson teaches you how to turn that conversational speed into a disciplined, **validated workflow**.

### What this shift supports

- **From Code Author to Code Reviewer**: Your primary role shifts from writing syntax to auditing logic and specifying constraints.
- **Specification-Driven Development**: You spend more time defining *what* the data should look like and *why*, and less time debugging boilerplate.
- **Cognitive Load Management**: By offloading syntax to an agent, you free up mental resources for higher-level research decisions.

### What it does NOT do

- It does not validate your research question or choose your methods.
- It does not detect subtle statistical or causal errors by default.
- It does not reduce your responsibility for the final output.

Using AI to generate code is **research-adjacent labor**. It becomes research only when embedded in a disciplined process of validation, documentation, and justification.

:::::::::::::::::::::::::::::::::::::::: prereq

## Prerequisites

- Basic familiarity with the command line.
- Fundamental understanding of Python (variables, functions, scripts).
- No prior experience with AI coding agents is required.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Learning Objectives

By the end of this lesson, participants will be able to:

- **Orchestrate** changes across a project using CLI-based AI agents.
- **Maintain** persistent project context using `GEMINI.md` or `CONTEXT.md`.
- **Apply** a Three-Layer Validation stack (Immutable requirements, Agent tests, Metamorphic tests).
- **Implement** Approval Gates to prevent fatigue and semantic drift.
- **Track** the provenance and reproducibility of agent-generated results.

## Acknowledgements
This lesson is adapted from the workshop **"Vibe Coding for Research"** developed by **Bruno Smaniotto** and **Tom van Nuenen** at the **UC Berkeley D-Lab**. 

The original materials can be found at [dlab-berkeley/Vibe-Coding-for-Research](https://github.com/dlab-berkeley/Vibe-Coding-for-Research).
