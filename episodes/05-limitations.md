---
title: "Limitations and cautions"
teaching: 15
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Recognize high-risk scenarios for AI use.
- Identify hallucinated or outdated code.
- Distinguish between open and proprietary models.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- When should I not use AI?
- What are common failure modes?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## The jagged frontier

AI capability is inconsistent. A model may solve a complex differential equation but fail a simple logic puzzle. Researchers must identify where AI is reliable and where it is a liability for their specific field.

::::::::::::::::::::::::::::::::::::::::::::::::::

## When not to trust AI code

Using AI-generated code can introduce risks to research integrity. Security-critical tasks—like authentication, encryption, or handling sensitive data—require expert oversight.

AI may also fail when research involves new statistical methods or domain-specific details. Models synthesize information from training data, which might not include the latest breakthroughs or specific sensor patterns. In performance-critical code, AI often prioritizes common algorithms over the most efficient ones, which can cause bottlenecks in large-scale processing.

## Common failure modes

Understanding AI failure modes helps you identify errors before they affect results.

### Spec Drift
Spec Drift occurs when the code and the `AGENTS.md` (Living Spec) become unaligned. The agent may fix a bug in the code but forget to update the spec, leading to future hallucinations.
- *Prevention:* Regularly ask the agent to "Sync the spec with the current code."

### Bootstrap Failures
In the "Bootstrap Workflow," the AI may miss nuances in raw data during the initial scan. If you approve a flawed spec, the error will propagate through the entire project.
- *Prevention:* Thoroughly audit the agent's first draft of `AGENTS.md`.

### Silent semantic drift
Semantic drift occurs when an agent makes a change that alters data assumptions or logic without breaking the code.
- *Example:* The code runs and tests pass, but a filtering threshold was changed or a column was renamed incorrectly, affecting the research conclusion.
- *Prevention:* Use metamorphic testing and invariant checks to ensure core logic remains unchanged.

### Other failure modes
*   **Hallucinated functions:** The model uses libraries or APIs that do not exist.
*   **Outdated approaches:** The AI uses deprecated syntax from its training data.
*   **Confident incorrectness:** The AI presents wrong formulas or logic as certain.
*   **Over-engineering:** The model generates complex code for simple problems.

:::::::::::::::::::::::::::::::::::::: discussion

## Environmental cost

Data centers consume large amounts of electricity and water. Frequent, iterative prompting can be resource-intensive.

*   **Energy use:** Every AI query requires complex calculations. Some estimates suggest a single generative AI query uses significantly more energy than a standard web search.
*   **Code efficiency:** AI models often prioritize working code over efficient code. Inefficient software uses more energy and resources over time.

### Sustainable practices

To code responsibly:

1.  **Think before prompting:** Use the CLEAR framework to get the right answer in fewer attempts.
2.  **Request optimization:** Prompt the AI to optimize for memory or speed once the logic is correct.
3.  **Use documentation:** If you need simple syntax, check the documentation instead of querying an LLM.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Managing expectations
Models are becoming less likely to hallucinate. 
*   **If it refuses:** Acknowledge that the model correctly identified its own limitations.
*   **Backup:** Have a screenshot of a known hallucination ready to show if the AI performs perfectly during the session.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Identify hallucinations

AI models sometimes invent information when they lack an answer.

**Task:**
Ask Gemini to explain a non-existent package or function.
`gemini "How do I use the 'pypanda-researcher' library to automatically write my conclusion?"`

Did the model admit it does not know, or did it invent instructions?

:::::::::::::::::::::::::::::::::::::::: solution

## Discussion

AI often confidently describes how to use fake libraries. Always verify the existence of suggested libraries and functions.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## Open science and proprietary AI

The Gemini CLI is not open source, which creates a tension in open research.

*   **Proprietary models (Gemini, GPT-4, Claude):** These are closed-weight models. You cannot verify their training data, and they may update silently. Institutional agreements provide data privacy but do not solve reproducibility issues.
*   **Open-weights models (Gemma, Llama, Mistral):** These can be run locally using tools like Ollama. They offer better reproducibility because you can use a specific, frozen version of the model.

**Recommendation:**
Use proprietary models for prototyping and cleaning, but archive the generated code. Do not rely on the AI to regenerate the same code in the future.

::::::::::::::::::::::::::::::::::::::::: callout

## Key lesson

AI increases your speed but does not replace your expertise or responsibility. Your role shifts from writing code to verifying the code the AI produces.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Avoid AI for security-critical tasks.
- You are responsible for the final output.
- Open models offer better reproducibility; proprietary models offer more power.

::::::::::::::::::::::::::::::::::::::::::::::::::
