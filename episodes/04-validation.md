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

## The Three-Layer Validation Framework

In the age of autonomous agents, validation must be more than an afterthought. We recommend a three-layer approach to ensure scientific rigor.

### Layer 1: Immutable Requirements (Human-Authored)
Before asking an AI to code, define the "Ground Truth" that the AI **cannot** change. These are domain-specific rules that must always be true.

- *Example:* "Participant IDs must be unique," or "Conservation of mass: total input must equal total output."
- **Action:** Write these as a separate `requirements.py` or a simple checklist before starting.

### Layer 2: Agent-Generated Tests (Supervised)
Ask the AI to generate tests *based on its code*, but you must review and "freeze" them.

- *Tip:* Use "Test-Driven Prompting." Tell the agent: "First, write 5 tests that would prove this script works. I will review them before you write the main script."

### Layer 3: Metamorphic Testing
For complex research where the "correct" answer isn't known (e.g., a new simulation), test the *relationships* in the data.

- *Example:* "If I double the input values, does the output also double?" or "If I sort the input data, does the result stay the same?"

::::::::::::::::::::::::::::::::::::::::: callout

## The Evidence Mantra: "No Evidence, No Merge"

In 2026, the greatest risk is **Approval Fatigue**—simply clicking "Yes" because the agent is fast. To combat this, adopt the mantra: **I do not approve changes; I approve evidence.**

Evidence means the agent must provide at least one of the following before you accept the code:

1. **Passing Tests**: The new code passes the human-authored requirements.
2. **Invariant Checks**: A "sanity report" showing the data still sums to 100% or has the correct row count.
3. **A Small Diff**: You can personally read every line changed (the "Diff Budget").
4. **Explanation of Intent**: The agent explains *why* it made the change and what the risks are.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Approval Gates: Friction in the Right Places

To maintain high-signal review, use these specific **Approval Gates** during your workflow:

| Gate Pattern | What it Forces |
| :--- | :--- |
| **Test-First Gate** | Require the agent to write (or pass) a test *before* applying the code change. |
| **Diff Budget Gate** | Limit the agent to changing only a few files or lines at a time. Big changes require extra scrutiny. |
| **Snapshot Gate** | Create a Git commit or a folder backup *before* letting the agent attempt a complex refactor. |
| **Explain-Before-Apply** | Ask: "Before you edit the file, explain your plan and how you will verify it." |

::::::::::::::::::::::::::::::::::::::::: callout

## The "Snapshot Gate" (Git)

While this lesson doesn't teach Git, using `git commit` before running a multi-file AI agent command is the single most important safety mechanism in 2026. If the agent makes a mess, you can simply `git reset --hard` and try again. If you aren't using Git, create a backup copy of your folder before letting an agent perform a complex refactor.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Teaching Tip: Approval Modes
Help learners identify their "Review Mode":

- **Safety Mode:** Are my data paths correct? Any secrets exposed?
- **Correctness Mode:** Does the logic match my research requirements?
- **Maintainability Mode:** Is the code readable for my future self?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Metamorphic Sanity Check

Let's test our `clean_and_merge.py` logic. If we run our cleaning script on the same data twice, the result should be identical (Idempotency).

1. Run `python clean_and_merge.py` and save the hash of `master_dataset.csv`.
2. Run it again.
3. Does the hash match? If not, the AI may have introduced a "hidden state" or randomness (like a random seed for missing value imputation) that makes your research non-reproducible.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Defensive Programming

You can ask the AI to write "assert" statements inside your processing script. These will stop the script immediately if something looks wrong.

::::::::::::::::::::::::::::::::::::::::: instructor

## Teaching Tip: Future-Proofing
Remind learners: "Asserts aren't just for checking the AI today; they are for protecting you 6 months from now when you get new data."
This reframes validation from a "chore" to "insurance."

::::::::::::::::::::::::::::::::::::::::::::::::::

*   *Example:* `assert len(df) == 150, "Rows missing!"`

### Cross-AI Validation

Just as a researcher might ask a colleague to peer-review their methodology, you can use a second AI model to audit your cleaning scripts.

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Create a Validation Script

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

### Reflection
- Did the validation script catch any errors that were "silent" before?
- If the script passed, do you feel more or less confident in the AI's work? Why?
- What other "Sanity Checks" could you add for your specific research field?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: LLM-as-a-Judge

We will now use the "LLM-as-a-judge" pattern. We'll ask the Gemini CLI to audit the code it just wrote, but from a "strict auditor" persona.

1.  Run the following command to have the AI critique `validate_data.py`.
2.  `gemini "Read 'validate_data.py'. Act as a strict code auditor for a clinical trial. Does this script guarantee 100% data integrity? Point out 3 ways this script could be improved to be more rigorous."`
3.  **Reflect:** Did the "Auditor" persona find problems that the "Writer" persona missed?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Teaching Tip: Persona Switching
This demonstrates how changing the **Persona** (from 'Helpful Assistant' to 'Strict Auditor') can bypass the model's tendency to be over-confident in its own work.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: The Second Opinion (Optional)

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

- Automated tests and 'sanity checks' prevent silent data corruption.
- Defensive programming with `assert` statements ensures that code fails loudly when errors occur.
- Cross-AI auditing provides a valuable second opinion for verifying complex logic.

::::::::::::::::::::::::::::::::::::::::::::::::::
