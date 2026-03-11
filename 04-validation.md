---
title: "Validation strategies: the approval gate"
teaching: 30
exercises: 20
---

:::::::::::::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Shift from a writer to an auditor mindset using the approval gate.
- Calculate rewrite time to measure workflow efficiency.
- Use a four-layer validation stack with explicit requirement constraints.
- Use multi-model verification to peer-review research code.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::: questions

- How do I move from vibe coding to research orchestration?
- What is rewrite time and why does it matter for research reproducibility?
- How can I use one AI to catch the errors of another?

::::::::::::::::::::::::::::::::::::::::::::::::::::

## The approval gate: verification over generation

In an agentic research workflow, your role is to audit and approve code rather than write it. The standard has shifted from vibe coding to spec-driven orchestration.

The approval gate is the point where you decide AI-generated code is robust enough for research production. It separates a working prototype from validated science.

:::::::::::::::::::::::::::::::::::::::::::::::::::::: callout

## The review-first standard
The bottleneck in research is no longer writing code; it is verifying it. A high-performance workflow follows this cycle:
Plan → Agent Implementation → Automated AI-Powered Testing → Human Review.

::::::::::::::::::::::::::::::::::::::::::::::::::::::

## Measuring efficiency: rewrite time

Rewrite time is a metric to determine if an AI workflow is actually helping your research.

- **Definition:** The manual effort in minutes a researcher spends making AI-generated output production-ready.
- **Goal:** If you spend 20 minutes prompting but then 40 minutes fixing the code, your rewrite time is too high. 

:::::::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: calculate your rewrite time

Look back at a script you recently generated with an AI agent.
1. How many minutes did you spend fixing or refactoring the code to make it run?
2. If this took more than 10% of the total task time, what was the likely cause? 
    - Ambiguous specs? 
    - AI over-confidence? 
    - Lack of local context?

::::::::::::::::::::::::::::::::::::::::::::::::::::::::

## The four-layer validation stack

To minimize rewrite time and ensure research rigor, use a structured validation stack.

### Layer 1: Requirement constraints (No-Go Zones)
Before the AI writes code, define requirement constraints in your `AGENTS.md`. These are rules the AI is not allowed to break.

*Example:* "Do not change the column names in `raw_data.csv`" or "Use only base R for this visualization to ensure compatibility."

### Layer 2: Automated unit tests
Ask the agent to write tests before the implementation. Use a prompt pattern like: "First, write five Pytest cases that define the success of this data cleaning script. I will approve the tests before you write the logic."

### Layer 3: Metamorphic and invariant checks
Test the relationships in your data that should never change.
- **Invariants:** The total number of participants must remain 150 after merging.
- **Metamorphic checks:** If I change the order of the input rows, the final mean score should not change.

### Layer 4: Domain plausibility
This is where your research expertise is irreplaceable. AI does not know that a negative blood pressure reading is impossible.

---

## Multi-model verification

We use a challenger model to audit an implementation model rather than trusting a single AI.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: orchestrate a peer review

1. Use Model A (such as Claude Code or Cursor) to generate a data cleaning script.
2. Provide the code to Model B (such as Gemini CLI) with the following prompt:
   
   "Read this script. Act as a skeptical senior data scientist. Identify three potential edge cases where this script will fail, such as empty strings, NaN values, or encoding issues. Suggest specific assert statements to catch these."

3. Reflect: Did the challenger model find something the implementation model missed?

::::::::::::::::::::::::::::::::::::::::::::::::: solution

## Why this works
Models have different blind spots. Forcing a second AI to act as an auditor helps bypass the tendency of the primary assistant to be over-confident. This process reduces your manual rewrite time.

:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: instructor

## Teaching tip: approval fatigue
Warn learners about approval fatigue the tendency to accept AI suggestions without reading them. The four-layer stack is designed to make the AI prove it is correct before you review the code.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: keypoints

- The approval gate separates experimental prototypes from validated research.
- Rewrite time is the primary metric for measuring AI workflow value.
- Requirement constraints prevent the AI from drifting away from research specs.
- Multi-model verification uses a second AI to act as a skeptical peer reviewer.

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
