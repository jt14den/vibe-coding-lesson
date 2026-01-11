---
title: "Validation Best Practices"
teaching: 30
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Implement data integrity checks.
- Use assert statements for defensive programming.
- Perform Cross-AI auditing.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How do I know if the AI code is correct?
- What is a 'sanity check' in code?
- How can I use a second AI to check work?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Trust but Verify

AI is excellent at writing code that runs, but the primary challenge for researchers is ensuring that the code is *right*. In data cleaning, a common failure mode is "silent dropping"—a scenario where the AI's script executes without error but accidentally deletes significant portions of your data due to a minor date parsing mismatch or an unhandled edge case. To mitigate this, we must build validation into every step of the workflow.

### The "Sanity Check"

After processing or merging data, your first step should always be a high-level sanity check to verify basic facts about your dataset. Start by checking row counts: if you merged three files of 50 rows each, your master file should contain exactly 150 rows unless you explicitly filtered them. You should also verify column consistency to ensure all expected variables are present and check data types to confirm that dates and numbers are being treated as their correct types rather than generic strings.

### Defensive Programming

You can ask the AI to write "assert" statements inside your processing script. These will stop the script immediately if something looks wrong.

::::::::::::::::::::::::::::::::::::::::: instructor

## Teaching Tip: Future-Proofing
Remind learners: "Asserts aren't just for checking the AI today; they are for protecting you 6 months from now when you get new data."
This reframes validation from a "chore" to "insurance."

::::::::::::::::::::::::::::::::::::::::::::::::::

*   *Example:* `assert len(df) == 150, "Rows missing!"`

### Cross-AI Validation

Just as a researcher might ask a colleague to peer-review their methodology, you can use a second AI model to audit your cleaning scripts. By providing your script to a different model (such as Claude or ChatGPT) and asking it to look for edge cases, date parsing vulnerabilities, or logic errors, you gain a "second opinion" that often catches subtle bugs the first model might have missed.

::::::::::::::::::::::::::::::::::::::::: instructor

## Backup Plan
Live coding with AI can be unpredictable. If the Gemini API hangs or returns garbage code during this challenge, have a working `validate_data.py` ready to share (e.g., via a distinct "solution" file or a shared pad) so the class can proceed to running it.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: The Integrity Check

To prove our `master_dataset.csv` is clean, we will write a dedicated validation script using the Gemini CLI. Run the following command to create a script that loads the dataset and performs three specific checks: ensuring there are no duplicate IDs, verifying that all scores fall within the expected range, and confirming that there are no missing values.

```bash
gemini "Create a script called 'validate_data.py'. It should load 'master_dataset.csv' and check that there are no duplicate participant_ids, all 'score' values are between 0 and 100, and there are zero missing values. If any check fails, print a warning; otherwise, print 'PASS' for each step."
```

Once generated, run the script with `python validate_data.py`. If you see a "FAIL" or a warning, you will need to investigate your `clean_and_merge.py` script to find the source of the error.

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

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: The Second Opinion

Now that you have your validation script, let's practice the **Cross-AI Validation** strategy.

1.  Open a **new** chat session in a different AI tool (like Claude or ChatGPT).
2.  Paste the contents of your `validate_data.py` code into the chat.
3.  Ask the AI to review the script for potential bugs, specifically asking how it would handle empty files or columns containing unexpected text.

**Reflect:** Did the second AI identify any vulnerabilities that you or the first AI missed?

:::::::::::::::::::::::::::::::::::::::: solution

## Discussion

It is common for a second AI to point out important edge cases, such as the script crashing if a file is missing or failing to account for "N/A" strings that aren't automatically recognized as missing data. This "Peer Review" process significantly reduces your individual verification load and increases the robustness of your research.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

## Key Points

- Automated tests and 'sanity checks' prevent silent data corruption.
- Defensive programming with `assert` statements ensures that code fails loudly when errors occur.
- Cross-AI auditing provides a valuable second opinion for verifying complex logic.

::::::::::::::::::::::::::::::::::::::::::::::::::
