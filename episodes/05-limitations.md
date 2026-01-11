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

Understanding the common ways AI fails can help you spot errors before they impact your results. One frequent issue is the generation of **hallucinated functions**, where the model invokes libraries or APIs that simply do not exist. You may also encounter **outdated approaches**, as the AI might use deprecated syntax from its training data that no longer works with current software versions.

Perhaps the most dangerous failure mode is **confident incorrectness**, where the AI presents a fundamentally wrong formula or logic with absolute certainty. This is often accompanied by **over-engineering**, where the model generates hundreds of lines of complex code for a problem that requires only a few. Recognizing these patterns allows you to maintain the "Editor's mindset," treating the AI's output as a draft that requires careful scrutiny rather than a finished product.

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

*   **Proprietary Models (Gemini, GPT-4, Claude):** These are "closed." You cannot verify their training data, and the model updates silently over time. Code generated today might be different next week.
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