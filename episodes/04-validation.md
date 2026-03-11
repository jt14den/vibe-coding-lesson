---
title: "Validation best practices"
teaching: 30
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Implement data integrity checks.
- Use assert statements for defensive programming.
- Perform cross-AI auditing.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How do I know if the AI code is correct?
- What is a 'sanity check' in code?
- How can I use a second AI to check work?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Validation framework

Validation is essential when using AI agents. A structured approach ensures research rigor.

### Layer 1: Human-authored requirements
Before asking an AI to code, define the rules it cannot change. These are domain-specific requirements.

- *Example:* "Participant IDs must be unique," or "Total input must equal total output."
- **Action:** Write these as a checklist or a separate `requirements.py` file.

### Layer 2: Supervised tests
Ask the AI to generate tests based on its code, then review and finalize them.

- *Tip:* Use test-driven prompting. Tell the agent: "First, write 5 tests that prove this script works. I will review them before you write the main script."

### Layer 3: Metamorphic testing
For complex research where the correct answer is unknown, test the relationships in the data.

- *Example:* "If I double the input values, does the output also double?" or "If I sort the input data, does the result stay the same?"

::::::::::::::::::::::::::::::::::::::::: callout

## Approve evidence, not changes

To avoid approval fatigue, focus on evidence. An agent should provide proof before you accept the code:

1. **Passing tests**: The code passes human-authored requirements.
2. **Invariant checks**: A report shows the data sums correctly or has the right row count.
3. **Small diffs**: You can read every line changed.
4. **Explanation of intent**: The agent explains why it made the change and what the risks are.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Approval gates

Use specific gates in your workflow to maintain high-quality reviews:

| Gate pattern | Purpose |
| :--- | :--- |
| **Test-first** | Require the agent to pass a test before applying a code change. |
| **Diff budget** | Limit the agent to changing only a few lines at a time. |
| **Snapshot** | Create a Git commit or folder backup before complex refactors. |
| **Explain-before-apply** | Ask the agent to explain its plan and verification strategy before editing files. |

::::::::::::::::::::::::::::::::::::::::: callout

## Using Git for snapshots

Using `git commit` before running an AI agent command is an important safety mechanism. If the agent makes a mistake, you can use `git reset --hard` to revert. If you are not using Git, back up your folder before complex changes.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Teaching tip: Review modes
Help learners identify their review focus:

- **Safety:** Are data paths correct? Are secrets exposed?
- **Correctness:** Does the logic match research requirements?
- **Maintainability:** Is the code readable?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Idempotency check

Test the `clean_and_merge.py` logic. Running the script on the same data twice should produce identical results.

1. Run `python clean_and_merge.py` and save the hash of `master_dataset.csv`.
2. Run it again.
3. Does the hash match? If not, the AI may have introduced randomness (like a random seed for missing values) that affects reproducibility.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Defensive programming

Ask the AI to include `assert` statements in your scripts. These will stop the script if a condition is not met.

::::::::::::::::::::::::::::::::::::::::: instructor

## Teaching tip: Future-proofing
Remind learners that assertions protect them in the future when they receive new data, acting as a form of research insurance.

::::::::::::::::::::::::::::::::::::::::::::::::::

*   *Example:* `assert len(df) == 150, "Rows missing!"`

### Cross-AI validation

You can use a second AI model to audit your cleaning scripts, similar to peer review.

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Create a validation script

Use the Gemini CLI to create a script that validates `master_dataset.csv`. The script should check for duplicate IDs, verify that scores are between 0 and 100, and confirm there are no missing values.

```bash
gemini "Create a script called 'validate_data.py'. It should load 'master_dataset.csv' and check that there are no duplicate participant_ids, all 'score' values are between 0 and 100, and there are zero missing values. If any check fails, print a warning; otherwise, print 'PASS' for each step."
```

Run the script with `python validate_data.py`. If it fails, investigate `clean_and_merge.py`.

:::::::::::::::::::::::::::::::::::::::: solution

## Expected output

A successful pipeline should return:

```text
Checking for duplicates... PASS
Checking score range (0-100)... PASS
Checking for missing values... PASS
Validation complete. No errors found.
```

### Reflection
- Did the validation script catch any silent errors?
- How does this script affect your confidence in the AI's work?
- What other sanity checks would be useful for your field?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Auditor persona

Use the LLM-as-a-judge pattern by asking the Gemini CLI to audit the code it wrote from a strict persona.

1.  Ask the AI to critique `validate_data.py`.
2.  `gemini "Read 'validate_data.py'. Act as a strict code auditor for a clinical trial. Does this script guarantee 100% data integrity? Point out 3 ways this script could be improved."`
3.  **Reflect:** Did the auditor persona find problems that the writer persona missed?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Teaching tip: Persona switching
This shows how changing the persona from 'Helpful Assistant' to 'Strict Auditor' can bypass model over-confidence.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Second opinion (optional)

Practice cross-AI validation with a different tool.

1.  Open a new chat in another AI tool (like Claude or ChatGPT).
2.  Paste your `validate_data.py` code.
3.  Ask the AI to review the script for bugs, specifically edge cases like empty files or unexpected text.

**Reflect:** Did the second AI identify any vulnerabilities missed by the first one?

:::::::::::::::::::::::::::::::::::::::: solution

## Discussion

A second AI often identifies edge cases, such as the script crashing on missing files or "N/A" strings. This peer review process reduces verification load and increases robustness.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Automated tests and sanity checks prevent data corruption.
- Assert statements ensure code fails loudly when errors occur.
- Cross-AI auditing provides a second opinion for verifying logic.

::::::::::::::::::::::::::::::::::::::::::::::::::
