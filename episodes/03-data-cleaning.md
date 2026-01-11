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

### Generating Messy Data

To practice cleaning, we first need a dataset with realistic inconsistencies. We can use the AI to simulate a multi-site study where each location used slightly different naming conventions or date formats. Run the following command to generate three CSV files—`site_A.csv`, `site_B.csv`, and `site_C.csv`. The prompt instructs the AI to purposefully include inconsistent column names (like `ParticipantID` vs `id`) and varied date formats to mimic real-world data collection errors.

```bash
gemini "Create a python script named 'make_messy_data.py'. It should generate 3 CSV files ('site_A.csv', 'site_B.csv', 'site_C.csv') with 50 rows each. Columns should include 'ID', 'Date', and 'Score', but make them inconsistent (e.g., 'ParticipantID' vs 'id', 'date' vs 'Date_Time'). Add some missing values and weird date formats (like '2023/01/05' vs 'Jan 5, 2023'). Run the script."
```

Once you run the generated script with `python make_messy_data.py`, you will have three headache-inducing files in your directory.

### Auditing the Data

Before attempting to fix the files, we need to understand the extent of the chaos. Instead of opening each file manually in a spreadsheet, we can ask the AI to write an inspection script. We want this script to read every CSV in the folder and report back on the filenames, the specific column names found in each, and the count of missing values. This audit gives us the "Source of Truth" needed to design our cleaning logic.

```bash
gemini "Write a Python script called 'inspect_data.py' that reads every CSV file in the current folder. For each file, print the filename, the list of column names, and the number of missing values in each column."
```

Run the inspection script. You should see the inconsistencies clearly, such as `site_A` using `ParticipantID` while `site_B` uses `id`.

### Harmonizing Inconsistent Files

With the audit complete, we can now perform the harmonization. We will ask Gemini to generate a single script that reads all three site files, standardizes the ID and date columns, and converts all dates to a uniform YYYY-MM-DD format. We'll also include logic to fill missing scores with the site-specific median to ensure our data is complete. Finally, the script will merge these into a master dataset.

```bash
gemini "Write a script called 'clean_and_merge.py'. It should read the 3 site CSVs, rename all ID columns to 'participant_id', and standardize date columns to 'date'. Convert all dates to standard YYYY-MM-DD format, fill missing scores with the median of that site, and save the result to 'master_dataset.csv'. Add comments explaining each step."
```

::::::::::::::::::::::::::::::::::::::::: instructor

## Safety Net: Backup Scripts
This step involves complex logic. If a learner's AI fails to generate a working `clean_and_merge.py` after 2-3 attempts, provide them with a pre-written version of the script (available in `episodes/files/backup_clean_and_merge.py`) so they can proceed to the next challenge without falling behind.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## Stop and Read: The Editor's Role

Before you run this code, open `clean_and_merge.py` in your editor. Evaluate whether the logic makes sense, if the comments accurately describe the code, and if there are any obvious syntax errors. Remember that while the AI acts as your co-pilot, you are the pilot responsible for the final output.

::::::::::::::::::::::::::::::::::::::::::::::::::

Run `python clean_and_merge.py`. You now have a single, clean dataset ready for analysis.

::::::::::::::::::::::::::::::::::::::::: callout

## Why ask for comments?

Notice we explicitly asked the AI to "Add comments explaining each step." In a Vibe Coding workflow, where you are editing rather than writing from scratch, these comments are essential. They transform a script from a "black box" into a readable methodology that you can verify and document.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Challenge Hint
This challenge is harder because it requires modifying *existing* code. 
If learners are stuck, hint: "Does the AI know what is inside `clean_and_merge.py` yet?"
**Strategy:** They should explicitly ask the AI to "Read clean_and_merge.py" *before* asking it to modify it, or use a command that combines both actions (e.g., `gemini "Read clean_and_merge.py and add..."`).

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: The Curveball

Research requirements often change mid-stream. Imagine your Principal Investigator (PI) just emailed you to exclude any participant with a Score below 10, as they are likely outliers.

Instead of editing `clean_and_merge.py` manually, use the Gemini CLI to update the script. Ask the AI to read the existing file and instruct it to add the filtering logic. Once done, run the updated script and verify the "Score" column in `master_dataset.csv`.

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

### Automating the Documentation

A reproducible project is only as good as its documentation. For the final step, we will have the AI generate a README that explains the entire pipeline we just built, from the original raw files through the cleaning and imputation steps to the final output format.

```bash
gemini "Create a README.md file that explains the data processing pipeline we just built. List the original files, the cleaning steps performed, and the final output format."
```

:::::::::::::::::::::::::::::::::::::::: keypoints

## Key Points

- Use AI to automate the tedious aspects of data harmonization and standardization.
- Auditing your data before cleaning helps identify specific inconsistencies.
- Verification is mandatory: always read and test generated code before execution.

::::::::::::::::::::::::::::::::::::::::::::::::::