---
title: "Reference"
---

## Glossary

Agent
: An AI system capable of using tools (like reading files, running code, or searching the web) to complete autonomous tasks.

Agentic Research Workflows
: A paradigm shift in research software where AI agents handle the imperative syntax generation, while the researcher focuses on declarative specification and rigorous validation.

Approval Gates
: Strategic points of friction in an agentic workflow (e.g., Test-First, Diff Budget) designed to prevent approval fatigue and ensure human oversight.

Chain of Thought
: A prompting technique that encourages the AI to explain its reasoning step-by-step. Reasoning models (like o1 or R1) have this capability built-in.

CLEAR Framework
: A prompt engineering model (Concise, Logical, Explicit, Adaptive, Reflective) developed by Leo Lo to optimize AI interactions.

CLI (Command Line Interface)
: A text-based interface for interacting with your computer's operating system. Essential for giving AI agents direct access to the file system.

CO-STAR Framework
: A prompt engineering framework (Context, Objective, Style, Tone, Audience, Response) emphasizing the importance of persona and audience.

Context Poisoning
: A failure mode where irrelevant, stale, or contradictory information within a long context window (e.g., an `/archive` folder) causes the AI to hallucinate or generate incorrect code.

Declarative Programming (with AI)
: A focus on describing the *desired outcome* (what the data should look like) rather than the *imperative steps* (how to write the loop), offloading the latter to an AI agent.

Determinism Collapse
: The risk that small variations in prompts or silent updates to AI model weights will result in different code outputs for the same task, threatening research reproducibility.

Evidence Mantra ("No Evidence, No Merge")
: The principle that a researcher should never approve an AI-generated change without supporting evidence (passing tests, invariant reports, or a readable diff).

Few-shot Prompting
: Providing examples in the prompt to guide the AI's output.

Hallucination
: When an AI generates factually incorrect or nonsensical information confidently.

Immutable Requirements
: Human-authored domain rules and constraints (e.g., "dates must be chronological") that act as the "Ground Truth" and cannot be modified by the AI agent.

LLM (Large Language Model)
: A deep learning model trained on vast amounts of text data to generate human-like text (e.g., GPT-4o, Gemini 2.0, Claude 3.5).

Metamorphic Testing
: A validation strategy that checks the *relationships* between inputs and outputs (e.g., "If I double the input, does the output also double?") rather than checking for a single fixed value.

Natural Language Orchestration
: Using natural language to guide an AI agent in performing complex, multi-step tasks across multiple files in a project.

Provenance Tracking
: The practice of documenting the metadata of an AI interaction (model version, prompt, context hashes) to ensure research accountability.

Reasoning Models
: A new class of AI models (e.g., o1, DeepSeek-R1) trained to perform complex logical reasoning and verification before producing an output.

Silent Semantic Drift
: A failure mode where an AI's code runs and passes basic tests but quietly changes the underlying research assumptions or data meanings.

Synthetic Data
: Artificially generated data used for testing validation pipelines without risking sensitive real-world data.

Vibe Coding
: The early (2023-2024) term for using AI to handle the "grunt work" of coding. In research, this has evolved into the more rigorous *Agent-Assisted Research Workflow*.

## References

1. Lo, L. S. (2023). The CLEAR path: A framework for enhancing information literacy through prompt engineering. *The Journal of Academic Librarianship*, 49(4), 102720. [https://doi.org/10.1016/j.acalib.2023.102720](https://doi.org/10.1016/j.acalib.2023.102720)
2. Teo, S. (2023). *How I Won Singapore’s GPT-4 Prompt Engineering Competition*. Towards Data Science. [https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41)
3. Smaniotto, B. & van Nuenen, T. (2024). Vibe Coding for Research: AI-Assisted Programming with Validation Best Practices. UC Berkeley D-Lab. [https://github.com/dlab-berkeley/Vibe-Coding-for-Research](https://github.com/dlab-berkeley/Vibe-Coding-for-Research)
4. Google Gemini API Documentation: [https://ai.google.dev/gemini-api/docs](https://ai.google.dev/gemini-api/docs)
