---
title: "Instructor Notes"
---

## Teaching Philosophy: The Shift from Writer to Editor

This lesson is designed to help researchers navigate the transition from **imperative coding** (writing every line) to **agentic orchestration** (guiding an AI to write code and then validating it). The core challenge for learners isn't learning syntax—it's managing **Cognitive Load** and maintaining a rigorous **Editor's Mindset**.

### Key Concepts to Emphasize:
- **Verification Load:** It is often harder to *verify* code you didn't write than to write it yourself. Normalize this "friction" as a sign of high-quality research.
- **Evidence Mantra:** "I do not approve changes; I approve evidence." This should be the recurring theme of the workshop.
- **Sandboxing:** Always emphasize the security implications of giving an AI direct access to the filesystem.

---

## Episode 1: Understanding CLI-Based AI
- **Auth Check:** Ensure all learners have their `GEMINI_API_KEY` exported. If they are using Docker, confirm they passed the environment variable correctly.
- **The Browser vs. CLI distinction:** Use the analogy of a "consultant" (Browser) vs. a "research assistant with keys to the lab" (CLI).
- **Discussion:** The prompt about "ChatGPT writing code that looks correct but fails" is a great way to bond over shared frustration and set the stage for why we need the CLI (to run and test immediately).

## Episode 2: Best Practices for Prompting
- **CO-STAR vs. CLEAR:** Don't get bogged down in the acronyms. The goal is *intentionality*.
- **Live Demo Tip:** Show a "Bad Prompt" vs. a "Good Prompt" live. Purposely run a vague command and show how it fails or produces messy output before using the refined version.
- **Self-Correction:** This is the "lightbulb" moment. Demonstrate asking the AI, "Are you sure? Review your code for edge cases."

## Episode 3: Data Cleaning (Live Demo)
- **High Intensity:** This is the most technically demanding episode. 
- **The "Safety Net":** If a learner's AI fails to generate working code after two attempts, have them copy the pre-written script from `instructors/files/backup_clean_and_merge.py`. This prevents them from falling behind.
- **Stop and Read:** Literally tell the class to "hands off keyboards" for 2 minutes to read the generated script before they run it.

## Episode 4: Validation Best Practices
- **Three-Layer Framework:** 
    1. Human Rules (Ground Truth)
    2. AI Tests (Supervised)
    3. Metamorphic Tests (Relationships)
- **Activity:** Encourage learners to try the "Metamorphic Sanity Check" (Challenge). It's a powerful way to show how "reproducibility" can be subtly broken by AI randomness.

## Episode 5: Limitations and Cautions
- **Silent Semantic Drift:** This is the most "dangerous" failure. Use the example of a filtering threshold (e.g., `> 0.5` vs. `>= 0.5`) that might not crash the code but changes the science.
- **Environmental Cost:** This is often a new topic for researchers. It grounds the "Spec-Driven Research Orchestration" hype in physical reality.

## Episode 6: Resources and Next Steps
- **The Toolscape:** Acknowledge that tools (Aider, Cursor, Claude Code) change weekly. Focus on the *principles* (CLI, validation, provenance) rather than specific software.
- **Attribution:** Remind learners that while AI can't be an author, transparency about its use is a core tenet of Open Science.

---

## Troubleshooting & Common Issues

### API Quotas & Limits
If learners hit "Resource Exhausted" errors, it's likely they've exceeded their free tier quota or are prompting too rapidly. Suggest they wait 60 seconds or use a smaller "context" (don't send every file in the folder).

### "Gemini Not Found"
Ensure the global npm install worked and that their `PATH` is updated. In Docker, this is handled automatically. On host machines, they might need to restart their terminal.

### Hallucinations
If a learner gets a script that imports a non-existent library (e.g., `import science_cleaner`), use it as a "teachable moment" for the whole class about verification.
