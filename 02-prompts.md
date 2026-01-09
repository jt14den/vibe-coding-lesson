---
title: "Best Practices for Prompting"
teaching: 20
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Apply the CLEAR framework.
- Identify sneaky AI behaviors.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How do I write effective prompts?
- What are common AI failures?

::::::::::::::::::::::::::::::::::::::::::::::::::

## The Five Principles

1. **Be Specific**: Include constraints, filenames, and expected outputs.
2. **Provide Context**: Explain the "why" and what you already have.
3. **Specify Outputs**: Define where to save results or how to format tables.
4. **Iterate**: Start simple and add complexity in follow-up prompts.
5. **Include Validation**: Explicitly ask the AI to "verify" or "test".

::::::::::::::::::::::::::::::::::::::::: callout

## Concrete Example: From Bad to Good

| Aspect | Bad Prompt | Good Prompt |
| :--- | :--- | :--- |
| **Vague vs Specific** | "Clean this data." | "In `data.csv`, remove rows with missing values in the 'age' column and save as `clean_data.csv`." |
| **No Context vs Context** | "Write a plot script." | "I am building a report for a climate study. Write a Python script using seaborn to create a line plot of 'temp' over 'year' from `results.csv`." |
| **Silent vs Validated** | "Run a t-test." | "Perform a paired t-test between 'pre' and 'post' columns. Print the t-statistic, p-value, and an interpretation of the result at alpha=0.05." |

::::::::::::::::::::::::::::::::::::::::::::::::::

## The CLEAR Framework

The CLEAR framework, developed by [Leo Lo](https://doi.org/10.1016/j.acalib.2023.102720), provides a structured approach to prompt engineering:

- **C**oncise: Prioritize important information.
- **L**ogical: Follow a coherent sequence of steps.
- **E**xplicit: Specify scope, persona, and tone.
- **A**daptive: Rephrase or split tasks if the AI gets stuck.
- **R**eflective: Evaluate output and use lateral reading (verify elsewhere).

## Watch Out for "Sneaky" AI

AI agents want to be helpful, and sometimes they take shortcuts to appear successful:

- **Synthetic Data Substitution**: Silently generating fake data if it can't find a file.
- **Model Swap**: Switching to a simpler (but less accurate) model if the requested one fails.
- **Fabricated Results**: Generating plausible-looking p-values that aren't actually calculated.
- **Silent Failure**: Using `try/except` blocks that hide errors from you.

::::::::::::::::::::::::::::::::::::::::: callout

## Discussion: How to Catch It?

Have you ever seen an AI make a confident mistake? In your own research, what "tells" might indicate the AI is hallucinating?

**Common Strategies:**

*   Always ask: "Show me the first 10 rows of the data you loaded."
*   Demand proof: "How did you calculate that p-value? Show the intermediate steps."
*   Check the file sizes of outputs: Is the "cleaned" file 0 bytes?

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

## Key Points

- Be specific and provide context.
- Always validate AI outputs.

::::::::::::::::::::::::::::::::::::::::::::::::::
