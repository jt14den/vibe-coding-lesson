---
title: "Limitations and Cautions"
teaching: 15
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Recognize high-risk scenarios.
- Identify hallucinated or outdated code.
- Distinguish between Open and Proprietary models.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- When should I NOT use AI?
- What are common failure modes?

::::::::::::::::::::::::::::::::::::::::::::::::::

## When NOT to Trust AI Code

Even with robust validation practices, there are specific scenarios where using AI-generated code introduces unacceptable risks to research integrity. Security-critical tasks—such as authentication, encryption, or the handling of sensitive participant data—should never be left to an AI without expert oversight. Similarly, when your research involves novel statistical methods or domain-specific quirks, the AI may fail because it can only synthesize information from its training data, which might not include the latest breakthroughs or the specific sensor noise patterns unique to your field. In performance-critical sections of your code, AI models also tend to prioritize the most common algorithms rather than the most efficient ones, potentially leading to bottlenecks in large-scale data processing.

## Common Failure Modes

Understanding the common ways AI fails can help you spot errors before they impact your results. 

### The Most Dangerous Failure: Silent Semantic Drift
The most common 2026 failure mode is **Silent Semantic Drift**. This occurs when an agent makes a "reasonable" improvement or refactor that quietly changes your data semantics or assumptions. 
- *What it looks like:* The code runs, the tests still pass, but your research conclusion shifts because a filtering threshold was silently changed or a data column was renamed incorrectly.
- *How to catch it:* Use **Metamorphic Testing** and **Invariant Suites** (as discussed in Episode 4) to ensure your "Ground Truth" hasn't shifted.

### Other Failure Modes
*   **Hallucinated functions:** The model invokes libraries or APIs that do not exist.
*   **Outdated approaches:** The AI uses deprecated syntax from its training data.
*   **Confident incorrectness:** The AI presents a fundamentally wrong formula or logic with absolute certainty.
*   **Over-engineering:** The model generates hundreds of lines of complex code for a problem that requires only a few.

:::::::::::::::::::::::::::::::::::::: discussion

## The Environmental Cost

It is easy to forget that "the cloud" is actually a physical network of data centers that consume vast amounts of electricity and water. "Vibe Coding"—which relies on frequent, iterative prompting—can be surprisingly resource-intensive.

*   **Inference Costs:** Every time you ask an AI to "rewrite this function," servers run complex matrix multiplications. Research estimates that a single generative AI query can consume **4–5 times more energy** than a standard web search engine query (Source: *Joule*, 2023).
*   **Code Efficiency (Green Coding):** AI models often prioritize "working" code over "efficient" code. Recent studies suggest that AI-generated software can be significantly less energy-efficient than expert-written code, sometimes by margins of **30-40%** depending on the task (Source: *arXiv*, 2024). If you accept the AI's first draft without optimization, you may be deploying software that wastes battery life and server cycles for years.

### Sustainable Practice

To code responsibly in the age of AI, consider these three principles:

1.  **Think before you prompt:** Use frameworks like **CLEAR** to get the right answer in one shot, rather than regenerating 20 times to find the right "vibe."
2.  **Request optimization:** Explicitly prompt the AI to "rewrite this for memory efficiency" or "optimize for speed" once the logic is correct.
3.  **Don't generate what you can look up:** If you just need the syntax for `pd.read_csv`, checking the documentation is far greener than querying an LLM.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Managing Expectations
As models improve (e.g., Gemini 1.5 Pro vs Flash), they are becoming harder to trick into hallucinating. 
*   **If it refuses:** Praise the model! Point out that it correctly identified its lack of knowledge.
*   **Backup:** Have a screenshot ready of a "classic" hallucination (like the famous "recurse-center" library or a made-up court case) just in case everyone's AI behaves perfectly.

::::::::::::::::::::::::::::::::::::::::::::::::::

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

::::::::::::::::::::::::::::::::::::::::::::::::::

## The Black Box Problem: Open Science vs. Proprietary AI

It is important to acknowledge a tension in this workshop: **The Gemini CLI is not Open Source.**

*   **Proprietary Models (Gemini, GPT-4, Claude):** These are "closed." You cannot verify their training data, and the model updates silently over time. While **institutional agreements** (like those at UC) provide critical data privacy and compliance protections, they do not resolve the reproducibility challenges inherent in closed-weight models.
*   **Open Weights Models (Gemma, Llama, Mistral):** These models can be downloaded and run locally (e.g., using tools like Ollama). They offer greater reproducibility because you can freeze the specific version of the "brain" you are using.

**Recommendation for Researchers:** 
Use powerful proprietary models (like Gemini) for the "Vibe Coding" phase—prototyping, cleaning, and writing scripts. However, be aware that the *generator* of your code is a black box. Always archive the *generated code* (which is open) rather than relying on the AI to regenerate it perfectly in the future.

::::::::::::::::::::::::::::::::::::::::: callout

## Key Lesson

You remain the scientist. AI augments your speed, but it does not replace your expertise or your responsibility for the results. Your primary job shifts from "writing code" to managing the **Verification Load** of the code the AI produces.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

## Key Points

- Avoid AI for security-critical tasks.
- You are responsible for the final output.
- Open models offer reproducibility; proprietary models offer power.

::::::::::::::::::::::::::::::::::::::::::::::::::