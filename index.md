---
title: "Agentic Research Workflows: AI and Validation"
start: true
---

### Natural-language specifications, CLI agents, and a four-layer validation stack

This lesson introduces researchers to Agentic Research Workflows, changing how we write and maintain research software. By using AI coding agents, we move from writing every line of syntax to defining intent and verifying outcomes.

The focus is not on replacing research thinking, but on reducing the cost of turning research intent into runnable code while maintaining standards for correctness, validation, and reproducibility.

## From 'Vibes' to Research Orchestration

The term "vibe coding" (coined by Andrej Karpathy) describes the early 2023-2024 shift toward guiding AI with natural-language prompts. While intuition is where we start, research demands more. This lesson teaches you how to turn conversational speed into **Spec-Driven Research Orchestration**—a disciplined, validated workflow.

### What this shift supports

- **Code orchestrator over author**: Your primary role shifts from writing syntax to auditing logic and specifying constraints in a **Living Spec (GEMINI.md)**.
- **Specification-driven development**: You spend more time defining what the data should look like and why, and less time debugging boilerplate.
- **Cognitive load management**: By offloading syntax to an agent, you free up mental resources for research decisions.

### What it does not do

- Validate your research question or choose your methods.
- Detect subtle statistical or causal errors by default.
- Reduce your responsibility for the final output.

Using AI to generate code is research-adjacent labor. It becomes research only when embedded in a disciplined process of validation, documentation, and justification.

:::::::::::::::::::::::::::::::::::::::: prereq

## Prerequisites

- Basic familiarity with the command line.
- Fundamental understanding of Python (variables, functions, scripts).
- No prior experience with AI coding agents is required.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Learning Objectives

By the end of this lesson, participants will be able to:

- Manage changes across a project using CLI-based AI agents.
- Orchestrate agents using a **Living Spec (GEMINI.md)**.
- Apply a four-layer validation stack (requirements, tests, metamorphic checks, **domain plausibility**).
- Implement approval gates to prevent fatigue and spec drift.
- Track the provenance and reproducibility of agent-generated results using Git.

## Acknowledgements
This lesson is adapted from the workshop "Vibe Coding for Research" developed by Bruno Smaniotto and Tom van Nuenen at the UC Berkeley D-Lab. 

The original materials can be found at [dlab-berkeley/Vibe-Coding-for-Research](https://github.com/dlab-berkeley/Vibe-Coding-for-Research).
