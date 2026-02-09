---
title: "Vibe Coding for Research"
start: true
---

AI-Assisted Programming with Validation Best Practices.

This lesson introduces researchers to **Vibe Coding**, the practice of using AI tools to accelerate *implementation* work in research software, while maintaining strong standards for **correctness, validation, and reproducibility**.

The focus is not on replacing research thinking, but on reducing the cost of turning research intent into runnable, inspectable code, and on learning how to verify what AI systems produce.

## What is “Vibe Coding”?

Coined by Andrej Karpathy, **Vibe Coding** describes a workflow in which you guide an AI system with natural-language prompts to generate, modify, and iterate on code, rather than writing every line manually.

In practice, this means describing what you want the code to do, running the code and inspecting the outputs, and iterating based on failures or surprises.

Vibe coding reduces the friction of writing and revising code. It does **not** remove the need to understand, validate, or justify what that code is doing.

## What Vibe Coding Does, and Does Not Do, for Research

### What it supports

- **Less Boilerplate, More Research Decisions**  
  You spend less time assembling scaffolding and more time specifying assumptions, transformations, and checks.
- **From Code Author to Code Reviewer**  
  Your role shifts toward inspecting outputs, auditing logic, and writing validations that catch quiet failures.
- **Faster Iteration, Not Faster Truth**  
  You can prototype analyses and pipelines quickly, which helps exploration and feasibility testing.
  
### What it does not do

- It does not validate your research question.
- It does not choose appropriate methods for your data.
- It does not detect subtle statistical, causal, or measurement errors by default.
- It does not reduce your responsibility for interpretation or reproducibility.

Using AI to generate code is **research-adjacent labor**. It becomes research only when embedded in a disciplined process of validation, documentation, and justification.

:::::::::::::::::::::::::::::::::::::::: prereq

## Prerequisites

- Basic familiarity with the command line, including navigating directories and running commands.
- Fundamental understanding of Python, including variables, functions, and scripts.
- No prior experience with AI coding agents is required.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Learning Objectives

By the end of this lesson, participants will be able to:

- Install and authenticate a CLI-based AI coding tool.
- Explain how autonomous agents differ from chat-based code assistance.
- Use structured prompting approaches to clearly specify intent and constraints.
- Apply validation strategies including:
  - sanity checks,
  - defensive programming,
  - and cross-model or cross-tool auditing.
- Identify where AI-assisted programming accelerates research workflows, and where additional caution is required.

## Acknowledgements
This lesson is adapted from the workshop **"Vibe Coding for Research: AI-Assisted Programming with Validation Best Practices"** developed by **Bruno Smaniotto** and **Tom van Nuenen** at the **UC Berkeley D-Lab**. 

The original materials and repository can be found at [dlab-berkeley/Vibe-Coding-for-Research](https://github.com/dlab-berkeley/Vibe-Coding-for-Research).
