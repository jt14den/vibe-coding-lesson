---
title: "Validation Best Practices"
teaching: 40
exercises: 30
questions:
- "How do I ensure the cleaned data is correct?"
- "What is a 'sanity check' in code?"
objectives:
- "Implement data integrity checks."
- "Use assert statements for defensive programming."
keypoints:
- "Never trust a cleaning script without verifying the output."
- "Automated tests prevent 'silent' data corruption."
---

## Trust but Verify

AI is great at writing code that *runs*, but does it write code that is *right*? In data cleaning, a common failure is "silent dropping"—where the AI's script runs without error but accidentally deletes 50% of your data because of a date parsing mismatch.

### 1. The "Sanity Check" (Post-Processing Validation)

After merging data, you should always verify basic facts.
*   **Row Counts**: If you had 3 files of 50 rows, your master file should have 150 rows (unless you explicitly filtered).
*   **Column Consistency**: Do you have the expected columns?
*   **Data Types**: Are the dates actually dates, or just strings?

### 2. Defensive Programming

You can ask the AI to write "assert" statements inside your processing script. These will stop the script immediately if something looks wrong.

*   *Example:* `assert len(df) == 150, "Rows missing!"`

### 3. Cross-AI Validation

Just like with the regression model, you can ask a second AI (like Claude or ChatGPT) to audit your cleaning script.

*   *Prompt:* "Review this pandas script. Are there any edge cases where it might fail to parse a date? Does it handle the median imputation correctly if all values are missing?"

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: The Integrity Check

We need to prove our `master_dataset.csv` is clean. Use the Gemini CLI to write a validation script.

Run this command:

```bash
gemini "Create a script called 'validate_data.py'. It should load 'master_dataset.csv' and check three things: 1. There are no duplicate participant_ids (print 'Pass' or 'Fail'). 2. All 'score' values are between 0 and 100 (or whatever the range was). 3. There are zero missing values. If any check fails, print a warning."
```

Run the script. Did your cleaning pipeline actually work?

::::::::::::::::::::::::::::::::::::::::::::::::::