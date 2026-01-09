---
title: "Live Demo: The Data Cleaning Agent"
teaching: 30
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Use Gemini to generate a realistic test dataset.
- Build a data processing pipeline that handles inconsistencies.
- Document the cleaning process automatically.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can AI handle messy, real-world data?
- Can I trust AI to standardize inconsistent files?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Live Demo Warning

This episode is designed as a **Live Demo**. The instructor plays the role of the "Data Janitor" while learners watch or follow along. 
**Prerequisite:** Ensure your `GEMINI_API_KEY` is set and active. Generating these scripts can take 10-30 seconds each.

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

Run `python clean_and_merge.py`. You now have a single, clean dataset ready for analysis.

::::::::::::::::::::::::::::::::::::::::: callout

## Why ask for comments?
Notice we explicitly asked the AI to "Add comments explaining each step." This is crucial for **Vibe Coding**. Since you didn't write the code yourself, these comments become your primary way of verifying the logic later. It transforms the script from a black box into a readable methodology.

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

::::::::::::::::::::::::::::::::::::::::::::::::::