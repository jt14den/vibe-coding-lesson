# Vibe Coding for Research: AI-Assisted Programming with Validation Best Practices

[![Status](https://img.shields.io/badge/Status-pre--alpha-red.svg)](https://github.com/carpentries/vibe-coding-lesson)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This lesson introduces researchers to **Vibe Coding**—the practice of using AI agents and CLI tools to accelerate research software development while maintaining high standards of software correctness and reproducibility.

**[View the Lesson Website](https://carpentries.github.io/vibe-coding-lesson/)**

## Overview

Traditional programming requires you to hold the entire syntax and logic of a script in your working memory. Vibe coding offloads the *syntax* generation to the AI, freeing up your cognitive resources for higher-level tasks. This lesson focuses on the **Gemini CLI** but teaches principles applicable to any "Open LLM" or coding agent.

## Key Features
*   **CLI-First Approach**: Learn to use AI directly in your terminal where your data lives.
*   **Project Context**: Master the use of `GEMINI.md` (and the standard `CONTEXT.md`) to ground your AI in your specific project goals.
*   **Validation**: Learn strategies like Synthetic Data Generation, Theoretical Validation, and Cross-AI Auditing to ensure code correctness.

## Contributing

We welcome contributions! This lesson is built using [The Carpentries Workbench](https://carpentries.github.io/workbench/).

To get started:
1.  Fork this repository.
2.  Clone your fork locally.
3.  Install the required tools (R, Pandoc, Sandpaper).

## Building the Lesson Locally

This lesson is written in Markdown and built with [Sandpaper](https://carpentries.github.io/sandpaper/).

1.  **Install R and the Workbench:**
    Follow the instructions in the [Workbench Documentation](https://carpentries.github.io/workbench/).

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/carpentries/vibe-coding-lesson.git
    cd vibe-coding-lesson
    ```

3.  **Preview the Lesson:**
    Open R/RStudio and run:
    ```r
    sandpaper::serve()
    ```

## Credits

This lesson is adapted from the workshop "Vibe Coding for Research" by **Bruno Smaniotto** and **Tom van Nuenen** at the **UC Berkeley D-Lab**.

## AI Attribution

This lesson was developed with the assistance of AI tools, adhering to the project's own transparency standards:

*   **Model:** Google Gemini 1.5 Pro (Jan 2026 version)
*   **Role:** 
    *   **Porting & Conversion:** Assisted in porting the lesson content from original D-Lab workshop slides into the Carpentries Workbench markdown format.
    *   **Curriculum Validation:** Performed automated checks for completeness and alignment with Carpentries pedagogical standards.
    *   **Content Refactoring:** Identified gaps in the "Validation" and "Limitations" sections and assisted in refactoring the glossary into semantic HTML.
*   **Verification:** All AI-assisted content was reviewed, edited, and validated by the maintainers to ensure pedagogical accuracy and technical correctness.

## License

This content is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
