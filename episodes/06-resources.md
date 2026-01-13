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

The ecosystem of AI tools for research is expanding rapidly, offering a variety of specialized interfaces for different stages of the development cycle. For direct coding, tools like **Claude Code** (Anthropic's CLI competitor to Gemini) and **GitHub Copilot** provide integrated autocomplete and refactoring support within your existing environment. Some researchers prefer a full AI-native code editor like **Cursor**, which is built from the ground up to integrate AI into every aspect of file management and script generation.

Beyond general-purpose coding assistants, research-specific tools are emerging to handle the literature and data extraction phases of scholarship. **Elicit** and **Consensus** focus on scientific paper discovery and extracting evidence-based claims, while Google's **NotebookLM** allows you to ground an AI's knowledge in your own collection of research PDFs, providing a private environment for summarizing and querying your specific documents.

## Extending Capabilities

While we have focused on the CLI, the ecosystem is evolving to allow AI tools to "reach out" to other software. Many browser-based models now offer extensions that connect with Google Drive, WolframAlpha, or other professional services. A significant development in this space is the **Model Context Protocol (MCP)**, an emerging open standard that allows an AI assistant to securely connect to any local or remote data source—such as a PostgreSQL database or your local file system—without requiring you to upload your data to a central server. This "USB-C port" for AI applications is quickly becoming the standard for tool interoperability.

## Citing and Crediting AI

Transparent attribution is critical for Open Science. Current academic standards (including **COPE**, **Nature**, and **Elsevier**) agree that **AI tools cannot be listed as authors** because they cannot hold legal accountability. Instead, they should be cited as methodological tools.

### Recommended Attribution Pattern

**1. In Code Repositories (`README.md`):**
Add a specific "AI Usage" section to your project documentation:

::::::::::::::::::::::::::::::::::::::::: callout

### Example Attribution Block

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

- [ ] **CLI tools** operate directly on your files—use them for multi-step tasks.
- [ ] **GEMINI.md** provides the persistent context your agent needs.
- [ ] **CLEAR/CONTEXT** frameworks improve your results.
- [ ] **Validate** using synthetic data and statistical theory.
- [ ] **You are the pilot**; the AI is the co-pilot.

:::::::::::::::::::::::::::::::::::::::::::::::::

## Navigating the AI Landscape: Signal vs. Noise

One of the hardest parts of using AI in research is separating genuine utility from marketing hyperbole. New tools appear daily, promising to "write your paper" or "automate your analysis." How do you know what is worth your time?

:::::::::::::::::::::::::::::::::::::: discussion

## How do you find tools?

Where do you hear about new AI tools? TikTok? Twitter/X? Academic journals? Word of mouth?

* Acknowledge that "hype" channels are often the fastest, but "reputable" channels are safer.

:::::::::::::::::::::::::::::::::::::::::::::::::

### The Hype Detection Kit

Before adopting a new AI tool for your research workflow, run it through this mental checklist:

::::::::::::::::::::::::::::::::::::::: checklist

## Hype vs. Reality Checklist

- [ ] **The "Magic" Test:** Does the tool claim to do *everything* (write, analyze, cite, submit)? **Hype.** Real tools usually do *one* thing well (e.g., "summarize PDFs" or "generate Python code").
- [ ] **The "Black Box" Test:** Can you see the intermediate steps? If it gives you a final answer without showing the code or logic, it is unsafe for science.
- [ ] **The Citation Test:** Does it hallucinate sources? If it can't link to a real DOI or URL, treat it as a creative writing tool, not a research assistant.
- [ ] **The "Free Lunch" Test:** If a service is free and seemingly unlimited, **you (and your data)** are likely the product. Check the privacy policy for "training on user data."

:::::::::::::::::::::::::::::::::::::::::::::::::

### Reputable Sources

To stay informed without drowning in noise, we recommend following a few high-signal, low-hype sources:

*   **[Import AI](https://importai.net/) (Jack Clark):** A weekly newsletter that covers technical breakthroughs and policy with a critical, realistic lens.
*   **[The Batch](https://www.deeplearning.ai/the-batch/) (DeepLearning.AI):** Andrew Ng's organization provides balanced coverage of how AI is being applied in industry and science.
*   **[Data Elixir](https://dataelixir.com/):** A broader data science newsletter that often highlights useful, practical tools rather than just the latest "shiny object."
*   **[The Gradient](https://thegradient.pub/):** Deep dives into AI research that explain the *why* and *how* without over-simplifying.

## Getting Help

- [Gemini API Docs](https://ai.google.dev/gemini-api/docs)

:::::::::::::::::::::::::::::::::::::::: keypoints

## Key Points

- Gemini, Claude, and Copilot serve different needs.
- Community support is vital.
- Plugins and MCP allow AI to connect to external data.

::::::::::::::::::::::::::::::::::::::::::::::::::
