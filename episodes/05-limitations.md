---
title: "Limitations and Cautions"
teaching: 15
exercises: 0
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Recognize high-risk scenarios.
- Identify hallucinated or outdated code.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- When should I NOT use AI?
- What are common failure modes?

::::::::::::::::::::::::::::::::::::::::::::::::::

## When NOT to Trust AI Code

Even with validation, there are areas where AI is particularly risky:

- **Security-Critical Code**: Authentication, encryption, or sensitive data handling.
- **Novel Research Methods**: If you are inventing a new statistical method, the AI only knows what has been published before.
- **Domain-Specific Quirks**: AI doesn't understand the specific "gotchas" of your field's data (e.g., specific sensor noise patterns).
- **Performance-Critical Sections**: AI often picks the most common (not the fastest) algorithm.

## Common Failure Modes

1. **Hallucinated Functions**: Invoking libraries or APIs that don't actually exist.
2. **Outdated Approaches**: Using deprecated code from its training data (e.g., old pandas syntax).
3. **Confident Incorrectness**: Presenting a wrong formula with absolute certainty.
4. **Over-engineering**: Adding 500 lines of code for a 5-line problem.

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Spot the Hallucination

AI models are trained to be helpful, which means they sometimes "guess" information they don't have. Let's see if we can trigger a hallucination.

**Task:**
Ask Gemini to explain a package or function that doesn't exist. For example:
`gemini "How do I use the 'pypanda-researcher' library to automatically write my conclusion?"`

What did it say? Did it admit it doesn't know, or did it invent instructions for this non-existent library?

:::::::::::::::::::::::::::::::::::::::: solution

## Discussion

Often, the AI will confidently describe how to install and use the fake library. It might even provide fake code snippets like `import pypanda_researcher`. 

This is a reminder to **always verify** the existence of libraries and functions the AI suggests before relying on them in your research.

::::::::::::::::::::::::::::::::::::::::::::::::::

## The Black Box Problem: Open Science vs. Proprietary AI

It is important to acknowledge a tension in this workshop: **The Gemini CLI is not Open Source.**

*   **Proprietary Models (Gemini, GPT-4, Claude):** These are "closed." You cannot verify their training data, and the model updates silently over time. Code generated today might be different next week.
*   **Open Weights Models (Gemma, Llama, Mistral):** These models can be downloaded and run locally (e.g., using tools like Ollama). They offer greater reproducibility because you can freeze the specific version of the "brain" you are using.

**Recommendation for Researchers:** 
Use powerful proprietary models (like Gemini) for the "Vibe Coding" phase—prototyping, cleaning, and writing scripts. However, be aware that the *generator* of your code is a black box. Always archive the *generated code* (which is open) rather than relying on the AI to regenerate it perfectly in the future.

::::::::::::::::::::::::::::::::::::::::: callout

## Key Lesson

You remain the scientist. AI augments your speed, but it does not replace your expertise or your responsibility for the results.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

## Key Points

- Avoid AI for security-critical tasks.
- You are responsible for the final output.

::::::::::::::::::::::::::::::::::::::::::::::::::