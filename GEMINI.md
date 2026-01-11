# Project Context: Vibe Coding for Research

This repository contains the "Vibe Coding for Research" lesson, part of the IMLS Open Science curriculum hub. It is a Carpentries-style lesson (using the Sandpaper framework) designed to introduce researchers to AI-assisted programming and validation best practices.

## Recent Accomplishments

### Current Lesson Development (`vibe-coding-lesson`)
- **Vibe Coding Context**: Added sections on "Vibe Coding" and cognitive load management, emphasizing the shift from "writer" to "editor" in the development process.
- **Framework Integration**: Integrated the **CO-STAR** prompting framework and the **CLEAR/CONTEXT** frameworks into the curriculum.
- **Glossary & References**: Converted the glossary to a semantic definition list format and updated references.
- **Markdown Polish**: Performed multiple passes of markdown formatting improvements for better readability and accessibility.
- **Lesson Structure**: Defined 6 core episodes:
    1. Understanding CLI-Based AI
    2. Effective Prompting (CO-STAR/CLEAR)
    3. AI-Assisted Data Cleaning
    4. Validation Strategies
    5. Limitations & Bias
    6. Resources & Next Steps

### Broader IMLS Open Science Project
- **Astro v5 Migration**: Completed the migration of the curriculum hub to Astro v5.
- **Redesign**: Transformed the site into a dynamic curriculum hub with lesson and author pages.
- **Citations**: 
    - Generated `CITATION.cff` files for all 15 curriculum lessons.
    - Enriched CFF files with ORCIDs, versioning (1.0.0), and automated release dates.
    - Implemented dynamic APA/BibTeX citation cards on all lesson pages.
- **Automation**: Created and finalized `scripts/create_prs.sh` to automate the submission of CFF files as Pull Requests using the GitHub CLI.
- **About Page**: Unified leadership, team, and community partner information in a redesigned about page.

## Project Structure
- `episodes/`: Markdown files for each lesson chapter.
- `instructors/`: Teaching notes and guides.
- `learners/`: Setup instructions and reference materials.
- `site/`: Built static site files and configuration.
- `config.yaml`: Lesson configuration and episode order.

## Tech Stack & Conventions
- **Framework**: Carpentries Sandpaper (R-based lesson engine).
- **Language**: Markdown, with R-Markdown support.
- **Style**: Semantic HTML elements within markdown (e.g., definition lists), clear callout blocks.
- **Validation Focus**: Emphasis on Synthetic Data, Theoretical validation, Cross-AI verification, Unit Testing, and Documentation.

## Carpentries Workbench Standards

### Documentation
- **Pedagogy**: [Carpentries Lesson Development Training](https://carpentries.github.io/lesson-development-training/)
- **Technical**: [The Carpentries Workbench](https://carpentries.github.io/workbench/)

### Component Syntax
The Workbench uses **Pandoc fenced divs** (colons `:::`) for special blocks. The opening and closing tags must match in length (at least 3 colons, usually recommended to use more to distinguish from nested blocks).

**Episode Structure Blocks:**
*   `::::::::::::::::::::::::::::::::::::::: objectives` (Start of episode)
*   `:::::::::::::::::::::::::::::::::::::::: questions` (Start of episode)
*   `:::::::::::::::::::::::::::::::::::::::: keypoints` (End of episode)

**Interactive Blocks:**
*   `::::::::::::::::::::::::::::::::::::::::: challenge` (Exercises)
    *   `:::::::::::::::::::::::::::::::::::::::: solution` (Must be nested inside `challenge`)
    *   `:::::::::::::::::::::::::::::::::::::::::::: hint` (Optional; Must be nested inside `challenge`)

**Callout Blocks:**
*   `::::::::::::::::::::::::::::::::::::::::: callout` (General info/warning)
*   `:::::::::::::::::::::::::::::::::::::::::: prereq` (Prerequisites)
*   `::::::::::::::::::::::::::::::::::::::: checklist` (Checklists)
*   `:::::::::::::::::::::::::::::::::::::: discussion` (Discussion topics)
*   `::::::::::::::::::::::::::::::::::::: testimonial` (Quotes/Testimonials)

**Advanced Blocks:**
*   `::::::::::::::::::::::::::::::::::::::::: instructor` (Instructor-only notes - visible in instructor view)
*   `::::::::::::::::::::::::::::::::::::::::::::::::: spoiler` (Collapsible content)
*   `::::::::::::::::::::::::::::::::::::::::: output` (Output block for code results)
*   `::::::::::::::::::::::::::::::::::::::: div` (Generic div for custom styling)

**Tabs:**
*   `::::::::::::::::::::::::::::::::::::::::: panel-tabset` (Container for tabs - automatic tab creation from headers)
    *   OR
*   `:::::::::::::::::::::::::::::::::::::::::: group-tab` (Manual Container for tabs)
    *   `:::::::::::::::::::::::::::::::::::::::::: tab` (Individual tab content)

### Structure Rules
1.  **Front Matter**: Each episode (`.md` file) must start with YAML front matter defining `title`, `teaching` (minutes), and `exercises` (minutes).
2.  **Flow**: `objectives` and `questions` blocks must appear immediately after the front matter.
3.  **Closing**: The `keypoints` block must be the final element of the episode.
4.  **Nesting**: 
    - `solution` and `hint` blocks **must** be inside a `challenge` block.
    - Ensure nested blocks use a different number of colons than their parent block to avoid Markdown parsing errors (e.g., parent uses 40 colons, child uses 35).
    - Always check for matching closing tags.
