---
title: "Limitations and Cautions"
teaching: 15
exercises: 0
questions:
- "When should I NOT use AI?"
- "What are common failure modes?"
objectives:
- "Recognize high-risk scenarios."
- "Identify hallucinated or outdated code."
keypoints:
- "Avoid AI for security-critical tasks."
- "You are responsible for the final output."
---

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

> ## Key Lesson
> You remain the scientist. AI augments your speed, but it does not replace your expertise or your responsibility for the results.