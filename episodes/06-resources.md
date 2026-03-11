---
title: "Resources and next steps"
teaching: 10
exercises: 10
---

:::::::::::::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- List alternative AI coding tools.
- Locate documentation and support.
- Understand plugins and Model Context Protocol (MCP).

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: questions

- What other tools are available?
- Where can I find help?

::::::::::::::::::::::::::::::::::::::::::::::::::

## AI tool landscape

The ecosystem of AI tools for research is expanding. For coding, tools like Claude Code (Anthropic's CLI), GitHub Copilot, and Aider (a CLI agent that works with multiple models) provide terminal support.

Some researchers use AI-native code editors like Cursor to interact with an entire repository. Models like Gemini 2.0 and DeepSeek-V3/R1 have increased the speed of these interactions.

Research-specific tools are also emerging. Elicit and Consensus focus on scientific paper discovery and evidence-based claims. Google's NotebookLM allows you to ground an AI's knowledge in your own collection of research PDFs for summarizing and querying documents.

## Extending capabilities

AI tools can now connect with other software. Many browser-based models offer extensions for Google Drive, WolframAlpha, and other services. The Model Context Protocol (MCP) is an open standard that allows AI assistants to connect to local or remote data sources—such as a PostgreSQL database or your local file system—without requiring you to upload data to a central server.

## Local models and open tooling

For researchers handling sensitive data or requiring reproducibility, local AI is a growing trend. Running models on your own hardware ensures that data does not leave your machine.

*   **Ollama**: A tool for running open-weights models (like Llama 3, Mistral, or Gemma) locally on macOS, Linux, and Windows. It provides a CLI and a local API.
*   **Aider**: A CLI coding agent that connects to proprietary APIs and local models (via Ollama). It is designed for pair programming and refactoring in the terminal.
*   **Qwen Coder**: High-performance open models from Alibaba (e.g., Qwen2.5-Coder) that can be run offline for security.

:::::::::::::::::::::::::::::::::::::::::::::::::: callout

## Privacy and performance

Local models offer privacy but require significant hardware (especially GPU VRAM) to match the performance of cloud models like Gemini 2.0. Many researchers use a hybrid approach: cloud models for general scripting and local models for sensitive data.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Advanced trends

### Multi-model ensembles
In advanced workflows, you can use different models for different tasks. For example, one model generates code, another critiques it, and a third writes validation tests. This reduces the chance of a single model's bias affecting results.

### Provenance tracking
Include metadata in the header of AI-generated files to ensure reproducibility:

- Model name and version.
- Date and a link to the prompt used.
- A hash of the context files provided.

### Cost and efficiency
With long-context models, it is easy to include unnecessary files in prompts, which increases costs.

- **Monitor tokens:** Check your API usage dashboard.
- **Optimize context:** Only include the files needed for the current task.

## Citing and crediting AI

Transparent attribution is essential for open science. Academic standards (including COPE, Nature, and Elsevier) state that AI tools cannot be listed as authors because they lack legal accountability. Instead, cite them as methodological tools.

### Recommended attribution

**1. In code repositories (`README.md`):**
Add an AI usage section to your project documentation:

:::::::::::::::::::::::::::::::::::::::::::::::::: callout

### Example attribution

*   **Model:** Google Gemini 2.0 Thinking (via Aider)
*   **Role:** Spec drafting and spec-guided cleaning.
*   **Verification:** Verified by [Your Name] via **AGENTS.md** rules and `validate_data.py`.

::::::::::::::::::::::::::::::::::::::::::::::::::

**2. In manuscripts:**
Cite the model in the methods or acknowledgements section.

*   *Example:* "We used Google Gemini (version 1.5) to assist with data cleaning scripts. Prompts and raw outputs are available in the supplementary material."

### Resources and standards

*   [**COPE (Committee on Publication Ethics)**](https://publicationethics.org/cope-position-statements/ai-author): Position statement on why AI cannot be an author.
*   [**Elsevier AI Policy**](https://www.elsevier.com/about/policies/publishing-ethics/usage-of-ai-tools-in-writing-for-research): Guidelines on declaring AI use in research.
*   [**CRediT Taxonomy**](https://credit.niso.org/): Use "Software" or "Methodology" roles to describe your use of the tool.

:::::::::::::::::::::::::::::::::::::::::::::::::: checklist

## Summary checklist

- [ ] CLI agents coordinate actions directly on your files.
- [ ] **AGENTS.md** acts as your 'Living Spec' and source of truth.
- [ ] The **Bootstrap Workflow** creates your spec from your data.
- [ ] Use **Layer 4: Domain Plausibility** to catch research logic errors.
- [ ] **Commit-as-Draft** with Aider ensures every change is traceable.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Navigating the AI landscape

Separating utility from marketing is a challenge. New tools appear daily, but many are more hype than substance.

:::::::::::::::::::::::::::::::::::::::::::::::::: discussion

## Finding tools

Where do you hear about new AI tools? Social media, academic journals, or word of mouth? Note that while social media is fast, reputable channels are more reliable.

::::::::::::::::::::::::::::::::::::::::::::::::::

### Identifying hype

Before adopting a new tool, consider these points:

:::::::::::::::::::::::::::::::::::::::::::::::::: checklist

## Hype detection

- [ ] **Scope:** Does the tool claim to do everything? Specialized tools usually perform better than those claiming to automate the entire research process.
- [ ] **Transparency:** Can you see the intermediate steps? Tools that provide answers without showing the underlying logic are less safe for research.
- [ ] **Citations:** Does it provide real DOIs or URLs? Verify all sources.
- [ ] **Data privacy:** If a service is free, check if your data is used for training.

::::::::::::::::::::::::::::::::::::::::::::::::::

### Reputable sources

Follow sources that focus on the practical and ethical aspects of AI in research:

*   **[Simon Willison’s Weblog](https://simonwillison.net/):** Focuses on AI engineering and security risks.
*   **[Ethan Mollick’s "One Useful Thing"](https://www.oneusefulthing.org/):** Analyzes how AI impacts cognitive labor.
*   **[Hamel Husain’s Blog](https://hamel.dev/):** Focuses on systematic evaluation of AI performance.
*   **[Import AI](https://importai.net/) (Jack Clark):** Covers technical breakthroughs and policy.
*   **[The Batch](https://www.deeplearning.ai/the-batch/):** Balanced coverage of AI in industry and science.
*   **[Data Elixir](https://dataelixir.com/):** Highlights practical tools for data science.
*   **[The Gradient](https://thegradient.pub/):** Detailed articles on AI research.

:::::::::::::::::::::::::::::::::::::::::::::::::: callout

## From vibes to evals

When AI scripts become critical for research, move to systematic evaluation. Create a "gold standard" dataset of known correct answers and test new iterations of AI-generated code against it.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: checklist

- [Gemini API Docs](https://ai.google.dev/gemini-api/docs)

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Your research protocol

Draft a plan for integrating these tools into your research workflow while maintaining rigor.

1.  **Select a project:** Which project would benefit most from an AI cleaning or validation pipeline?
2.  **Choose your gates:** Which approval gates (Test-first, Diff budget, Snapshot) will you use?
3.  **Define requirements:** What are 2-3 requirements for that project that the AI cannot change?
4.  **Verification strategy:** Will you use a second model, unit tests, or metamorphic checks?

:::::::::::::::::::::::::::::::::::::::: solution

### Discussion

A pre-defined protocol reduces decision fatigue during complex coding sessions. Deciding how to verify work early prevents approval fatigue later.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Gemini, Claude, and Copilot serve different needs.
- Community support is vital.
- Plugins and MCP allow AI to connect to external data.

::::::::::::::::::::::::::::::::::::::::::::::::::
