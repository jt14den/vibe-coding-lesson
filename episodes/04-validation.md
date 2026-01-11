---
title: "Validation Best Practices"
teaching: 30
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Implement data integrity checks.
- Use assert statements for defensive programming.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How do I know if the AI code is correct?
- What is a 'sanity check' in code?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Trust but Verify

AI is great at writing code that *runs*, but does it write code that is *right*? In data cleaning, a common failure is "silent dropping"—where the AI's script runs without error but accidentally deletes 50% of your data because of a date parsing mismatch.

### 1. The "Sanity Check" (Post-Processing Validation)

After merging data, you should always verify basic facts.
*   **Row Counts**: If you had 3 files of 50 rows, your master file should have 150 rows (unless you explicitly filtered).
*   **Column Consistency**: Do you have the expected columns?
*   **Data Types**: Are the dates actually dates, or just strings?

### 2. Defensive Programming

You can ask the AI to write "assert" statements inside your processing script. These will stop the script immediately if something looks wrong.

::::::::::::::::::::::::::::::::::::::::: instructor

## Teaching Tip: Future-Proofing
Remind learners: "Asserts aren't just for checking the AI today; they are for protecting you 6 months from now when you get new data."
This reframes validation from a "chore" to "insurance."

::::::::::::::::::::::::::::::::::::::::::::::::::

*   *Example:* `assert len(df) == 150, "Rows missing!"`

### 3. Cross-AI Validation

Just like with the regression model, you can ask a second AI (like Claude or ChatGPT) to audit your cleaning script.

*   *Prompt:* "Review this pandas script. Are there any edge cases or might fail to parse a date? Does it handle the median imputation correctly if all values are missing?"

::::::::::::::::::::::::::::::::::::::::: instructor

## Backup Plan
Live coding with AI can be unpredictable. If the Gemini API hangs or returns garbage code during this challenge, have a working `validate_data.py` ready to share (e.g., via a distinct "solution" file or a shared pad) so the class can proceed to running it.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: The Integrity Check

We need to prove our `master_dataset.csv` is clean. Use the Gemini CLI to write a validation script.

Run this command:

```bash
gemini "Create a script called 'validate_data.py'. It should load 'master_dataset.csv' and check three things: 1. There are no duplicate participant_ids (print 'Pass' or 'Fail'). 2. All 'score' values are between 0 and 100 (or whatever the range was). 3. There are zero missing values. If any check fails, print a warning."
```

Once generated, run the script with `python validate_data.py`. Did your cleaning pipeline actually work?

:::::::::::::::::::::::::::::::::::::::: solution

## Expected Output

If your cleaning pipeline was successful, you should see something like:

```text
Checking for duplicates... PASS
Checking score range (0-100)... PASS
Checking for missing values... PASS
Validation complete. No errors found.
```

If you see "FAIL" or "Warning", investigate your `clean_and_merge.py` script!

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

## Key Points

- Never trust a cleaning script without verifying the output.
- Automated tests prevent 'silent' data corruption.

::::::::::::::::::::::::::::::::::::::::::::::::::
