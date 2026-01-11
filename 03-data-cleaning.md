---
title: "Live Demo: The Data Cleaning Agent"
teaching: 30
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Use Gemini to generate a realistic test dataset.
- Build a data processing pipeline that handles inconsistencies.
- Verify AI-generated code before execution.
- Document the cleaning process automatically.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can AI handle messy, real-world data?
- Can I trust AI to standardize inconsistent files?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Active Participation

This episode is designed for **Live Coding**. Learners should follow along, executing the commands on their own machines. 
:::::::::::::::::::::::::::::::::::::::::: prereq

## Prerequisites

Ensure your `GEMINI_API_KEY` is set and active. Generating these scripts can take 10-30 seconds each.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

## The Universal Headache: Messy Data

For most researchers, the bottleneck isn't implementing complex algorithms—it's cleaning and merging inconsistent files. In this demo, we will use Gemini to act as our "Data Janitor," automating the standardization of messy CSV files.

### Step 1: generating the "Messy" Data

First, we need something to clean. Ironically, we can use the AI to generate our problem. Run this command to create three inconsistent data files simulating a multi-site study:

```bash
gemini "Create a python script named 'make_messy_data.py'. It should generate 3 CSV files ('site_A.csv', 'site_B.csv', 'site_C.csv') with 50 rows each. Columns should include 'ID', 'Date', and 'Score', but make them inconsistent (e.g., 'ParticipantID' vs 'id', 'date' vs 'Date_Time'). Add some missing values and weird date formats (like '2023/01/05' vs 'Jan 5, 2023'). Run the script."
```

Once you run the generated script (`python make_messy_data.py`), you will have three headache-inducing files in your directory.

### Step 2: The Audit

Before fixing anything, we need to know what we're dealing with. Instead of opening each Excel file manually, let the AI inspect them.

```bash
gemini "Write a Python script called 'inspect_data.py' that reads every CSV file in the current folder. For each file, print: 1. The filename 2. The list of column names 3. The number of missing values in each column."
```

Run the inspection script. You should see the chaos clearly (e.g., `site_A` has `ParticipantID`, `site_B` has `id`).

### Step 3: The Harmonization

Now for the magic. We will ask Gemini to write a script that handles these specific inconsistencies and merges them into a clean master dataset.

```bash
gemini "Write a script called 'clean_and_merge.py'. It should: 1. Read the 3 site CSVs. 2. Rename all ID columns to 'participant_id' and date columns to 'date'. 3. Convert all dates to standard YYYY-MM-DD format. 4. Fill missing scores with the median of that site. 5. Save the result to 'master_dataset.csv'. Add comments explaining each step."
```

::::::::::::::::::::::::::::::::::::::::: instructor

## Safety Net: Backup Scripts
This step involves complex logic. If a learner's AI fails to generate a working `clean_and_merge.py` after 2-3 attempts, provide them with a pre-written version of the script (available in `episodes/files/backup_clean_and_merge.py`) so they can proceed to the next challenge without falling behind.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## Stop and Read: The Editor's Role

Before you run this code, open `clean_and_merge.py` in your editor. 
*   Does the logic make sense?
*   Are the comments clear?
*   Do you see any obvious errors?

Remember: You are the pilot; the AI is just the co-pilot.

::::::::::::::::::::::::::::::::::::::::::::::::::

Run `python clean_and_merge.py`. You now have a single, clean dataset ready for analysis.

::::::::::::::::::::::::::::::::::::::::: callout

## Why ask for comments?
Notice we explicitly asked the AI to "Add comments explaining each step." This is crucial for **Vibe Coding**. Since you didn't write the code yourself, these comments become your primary way of verifying the logic later. It transforms the script from a black box into a readable methodology.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Challenge Hint
This challenge is harder because it requires modifying *existing* code. 
If learners are stuck, hint: "Does the AI know what is inside `clean_and_merge.py` yet?"
**Strategy:** They should explicitly ask the AI to "Read clean_and_merge.py" *before* asking it to modify it, or use a command that combines both actions (e.g., `gemini "Read clean_and_merge.py and add..."`).

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: The Curveball

Research requirements change. Imagine your Principal Investigator (PI) just emailed you: "We need to exclude any participant with a Score below 10, as they are likely outliers."

**Your Task:**
Instead of editing `clean_and_merge.py` manually, use the Gemini CLI to update the script.
1.  Ask the AI to read the existing file.
2.  Instruct it to add the filtering logic.
3.  Run the updated script and verify the "Score" column in `master_dataset.csv`.

:::::::::::::::::::::::::::::::::::::::: solution

## Possible Command

```bash
gemini "Read 'clean_and_merge.py'. Modify the script to filter out any rows where 'score' is less than 10. Keep all other logic the same. Save the updated script."
```

### Reflection
*   Did the AI rewrite the whole file or just edit the relevant part?
*   Did it remember to import `pandas` again?
*   Did you trust it enough to run it without looking, or did you check the diff first?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Step 4: Automating Documentation

Finally, a reproducible project needs a README.

```bash
gemini "Create a README.md file that explains the data processing pipeline we just built. List the original files, the cleaning steps performed (normalization, imputation), and the final output format."
```

:::::::::::::::::::::::::::::::::::::::: keypoints



## Key Points



- AI excels at tedious data harmonization tasks.

- Asking the AI to 'audit' data first prevents errors.
- Always read the code before running it.



::::::::::::::::::::::::::::::::::::::::::::::::::