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
> **AI Attribution**
> *   **Model:** Google Gemini 1.5 Pro (Jan 2026 version)
> *   **Role:** Code generation (scaffolding), Refactoring.
> *   **Verification:** All code verified by [Your Name] via unit tests.

**2. In Manuscripts:**
Cite the model in the **Methods** section or **Acknowledgements**.
*   *Example:* "We used Google Gemini (version 1.5) to assist with data cleaning scripts. Prompts and raw outputs are available in the supplementary material."

### Resources & Standards
*   [**COPE (Committee on Publication Ethics)**](https://publicationethics.org/cope-position-statements/ai-author): Position statement on why AI cannot be an author.
*   [**Elsevier AI Policy**](https://www.elsevier.com/about/policies/publishing-ethics/usage-of-ai-tools-in-writing-for-research): Guidelines on declaring AI use in research.
*   [**CRediT Taxonomy**](https://credit.niso.org/): Use the "Software" or "Methodology" roles to describe *your* use of the tool, but do not assign a role to the AI itself.

## Summary Checklist

1. [ ] **CLI tools** operate directly on your files—use them for multi-step tasks.
2. [ ] **GEMINI.md** provides the persistent context your agent needs.
3. [ ] **CLEAR/CONTEXT** frameworks improve your results.
4. [ ] **Validate** using synthetic data and statistical theory.
5. [ ] **You are the pilot**; the AI is the co-pilot.

## Getting Help

- [Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [D-Lab Consultations](https://dlab.berkeley.edu/consulting)

:::::::::::::::::::::::::::::::::::::::: keypoints

## Key Points

- Gemini, Claude, and Copilot serve different needs.
- Community support is vital.
- Plugins and MCP allow AI to connect to external data.

::::::::::::::::::::::::::::::::::::::::::::::::::
