---
title: "Resources and Next Steps"
teaching: 10
exercises: 0
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- List alternative AI coding tools.
- Locate documentation and support.
- Understand plugins and Model Context Protocol (MCP).

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What other tools are available?
- Where can I find help?

::::::::::::::::::::::::::::::::::::::::::::::::::

## The AI Tool Landscape

### Coding Tools

- **Claude Code**: Anthropic's CLI (competitor to Gemini CLI).
- **GitHub Copilot**: IDE-integrated autocomplete.
- **Cursor**: A full code editor with built-in AI.

### Research-Specific Tools

- **Elicit**: Paper discovery and data extraction.
- **Consensus**: Searching for scientific consensus.
- **NotebookLM**: Chatting with your own research PDFs.

## Extending Capabilities

While we focused on the CLI, the ecosystem is evolving to let AI tools "reach out" to other software.

*   **Browser Extensions (Plugins)**: Tools like ChatGPT and Gemini (in browser) often have "extensions" to connect with Google Drive, Kayak, or WolframAlpha.
*   **Model Context Protocol (MCP)**: This is an emerging open standard (adopted heavily by **Claude** and others) that lets you connect an AI assistant to *any* local or remote data source—like your PostgreSQL database, your Slack, or your local file system—without uploading everything. It is the "USB-C port" for AI applications.

## Citing and Crediting AI

Transparent attribution is critical for Open Science. Current academic standards (including **COPE**, **Nature**, and **Elsevier**) agree that **AI tools cannot be listed as authors** because they cannot hold legal accountability. Instead, they should be cited as methodological tools.

### Recommended Attribution Pattern

**1. In Code Repositories (`README.md`):**
Add a specific "AI Usage" section to your project documentation:
::::::::::::::::::::::::::::::::::::::::: callout

## Example Attribution Block

*   **Model:** Google Gemini 1.5 Pro (Jan 2026 version)
*   **Role:** Code generation (scaffolding), Refactoring.
*   **Verification:** All code verified by [Your Name] via unit tests.

::::::::::::::::::::::::::::::::::::::::::::::::::

**2. In Manuscripts:**
Cite the model in the **Methods** section or **Acknowledgements**.
*   *Example:* "We used Google Gemini (version 1.5) to assist with data cleaning scripts. Prompts and raw outputs are available in the supplementary material."

### Resources & Standards
*   [**COPE (Committee on Publication Ethics)**](https://publicationethics.org/cope-position-statements/ai-author): Position statement on why AI cannot be an author.
*   [**Elsevier AI Policy**](https://www.elsevier.com/about/policies/publishing-ethics/usage-of-ai-tools-in-writing-for-research): Guidelines on declaring AI use in research.
*   [**CRediT Taxonomy**](https://credit.niso.org/): Use the "Software" or "Methodology" roles to describe *your* use of the tool, but do not assign a role to the AI itself.

::::::::::::::::::::::::::::::::::::::: checklist

## Summary Checklist

1. [ ] **CLI tools** operate directly on your files—use them for multi-step tasks.
2. [ ] **GEMINI.md** provides the persistent context your agent needs.
3. [ ] **CLEAR/CONTEXT** frameworks improve your results.
4. [ ] **Validate** using synthetic data and statistical theory.
5. [ ] **You are the pilot**; the AI is the co-pilot.

:::::::::::::::::::::::::::::::::::::::::::::::::

## Navigating the AI Landscape: Signal vs. Noise

One of the hardest parts of using AI in research is separating genuine utility from marketing hyperbole. New tools appear daily, promising to "write your paper" or "automate your analysis." How do you know what is worth your time?

:::::::::::::::::::::::::::::::::::::: discussion

## How do you find tools?
Ask learners: "Where do you hear about new AI tools? TikTok? Twitter/X? Academic journals? Word of mouth?"
*   **Goal:** Acknowledge that "hype" channels are often the fastest, but "reputable" channels are safer.

:::::::::::::::::::::::::::::::::::::::::::::::::

### The Hype Detection Kit

Before adopting a new AI tool for your research workflow, run it through this mental checklist:

::::::::::::::::::::::::::::::::::::::: checklist

## Hype vs. Reality Checklist

1. [ ] **The "Magic" Test:** Does the tool claim to do *everything* (write, analyze, cite, submit)? **Hype.** Real tools usually do *one* thing well (e.g., "summarize PDFs" or "generate Python code").
2. [ ] **The "Black Box" Test:** Can you see the intermediate steps? If it gives you a final answer without showing the code or logic, it is unsafe for science.
3. [ ] **The Citation Test:** Does it hallucinate sources? If it can't link to a real DOI or URL, treat it as a creative writing tool, not a research assistant.
4. [ ] **The "Free Lunch" Test:** If a service is free and seemingly unlimited, **you (and your data)** are likely the product. Check the privacy policy for "training on user data."

:::::::::::::::::::::::::::::::::::::::::::::::::

### Reputable Sources

To stay informed without drowning in noise, we recommend following a few high-signal, low-hype sources:

*   **[Import AI](https://importai.net/) (Jack Clark):** A weekly newsletter that covers technical breakthroughs and policy with a critical, realistic lens.
*   **[The Batch](https://www.deeplearning.ai/the-batch/) (DeepLearning.AI):** Andrew Ng's organization provides balanced coverage of how AI is being applied in industry and science.
*   **[Data Elixir](https://dataelixir.com/):** A broader data science newsletter that often highlights useful, practical tools rather than just the latest "shiny object."
*   **[The Gradient](https://thegradient.pub/):** Deep dives into AI research that explain the *why* and *how* without over-simplifying.

## Getting Help

- [Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [D-Lab Consultations](https://dlab.berkeley.edu/consulting)

:::::::::::::::::::::::::::::::::::::::: keypoints

## Key Points

- Gemini, Claude, and Copilot serve different needs.
- Community support is vital.
- Plugins and MCP allow AI to connect to external data.

::::::::::::::::::::::::::::::::::::::::::::::::::
