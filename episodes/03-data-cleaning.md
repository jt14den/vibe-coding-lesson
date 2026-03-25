---
title: "Data cleaning with AI"
teaching: 30
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

## Objectives

- Generate a test dataset using Gemini.
- Build a data processing pipeline for inconsistent files.
- Verify AI-generated code before running it.
- Document the cleaning process.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can AI handle messy data?
- Can I trust AI to standardize inconsistent files?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Live coding
This episode uses live coding. Learners should follow along by running commands on their own machines.

:::::::::::::::::::::::::::::::::::::::::: prereq

## Prerequisites
Ensure your `GEMINI_API_KEY` is set. Generating scripts can take 10-30 seconds.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## Working inside the Gemini CLI

All prompts in this episode are typed inside an active Gemini CLI session. Start one in your project folder before the exercises:

```bash
cd path/to/your/project
gemini
```

Run Python scripts in a separate terminal window when instructed.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Cleaning messy data

Cleaning and merging inconsistent files is a common bottleneck in research. We will use Gemini to standardize messy CSV files.

### Generating test data

To practice cleaning, we need a dataset with inconsistencies. We can use AI to simulate a multi-site study where each location used different naming conventions or date formats. Run this command to generate three files: `site_A.csv`, `site_B.csv`, and `site_C.csv`.

```
Create a python script named 'make_messy_data.py'. It should generate 3 CSV files ('site_A.csv', 'site_B.csv', 'site_C.csv') with 50 rows each. Columns should include 'ID', 'Date', and 'Score', but make them inconsistent (e.g., 'ParticipantID' vs 'id', 'date' vs 'Date_Time'). Add some missing values and varied date formats (like '2023/01/05' vs 'Jan 5, 2023').
```

After running `python make_messy_data.py`, you will have three inconsistent files in your directory.

### Auditing the data

Before fixing the files, we need to understand the inconsistencies. We can ask the AI to write an inspection script that reads every CSV in the folder and reports the filenames, column names, and missing value counts.

```
Write a Python script called 'inspect_data.py' that reads every CSV file in the current folder. For each file, print the filename, the list of column names, and the number of missing values in each column.
```

Run the inspection script. You should see inconsistencies like `site_A` using `ParticipantID` while `site_B` uses `id`.

::::::::::::::::::::::::::::::::::::::::: callout

## Reasoning models
If your data files are extremely inconsistent, reasoning models (like o1 or DeepSeek-R1) are often more effective. They can identify subtle naming patterns that standard models might miss.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Spec-guided cleaning

In **Spec-Driven Research Orchestration**, we don't just ask for a script. We refer to the `AGENTS.md` file to ensure the script follows the project's rules.

### Harmonizing files with the Spec

We will now ask Gemini to generate a script using the rules defined in `AGENTS.md`.

```
Read 'AGENTS.md' and the 3 site CSVs. Write a script called 'clean_and_merge.py' that renames IDs and standardizes dates according to the schema in the spec. Fill missing scores with the median and save to 'master_dataset.csv'. Add comments linking code steps to spec rules.
```

::::::::::::::::::::::::::::::::::::::::: instructor

## Backup scripts
If a learner's AI fails to generate working code, provide the pre-written versions from `instructors/files/`:
- `backup_make_messy_data.py`
- `backup_inspect_data.py`
- `backup_clean_and_merge.py`

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: callout

## The editor role
Before running the code, open `clean_and_merge.py`. Check if the logic is sound, if the comments match the code, and if there are syntax errors. You are responsible for the final output.

::::::::::::::::::::::::::::::::::::::::::::::::::

Run `python clean_and_merge.py` to create the clean dataset.

::::::::::::::::::::::::::::::::::::::::: callout

## Using comments
We asked the AI to "Add comments explaining each step." These comments make the script readable and help you verify the methodology.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: instructor

## Challenge tip
This challenge requires modifying existing code. If learners are stuck, suggest they ask the AI to read `clean_and_merge.py` before asking for modifications.

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Update the script

Imagine you need to exclude any participant with a score below 10. Use the Gemini CLI to update `clean_and_merge.py` instead of editing it manually. Ask the AI to read the file and add the filtering logic. Run the updated script and verify the results in `master_dataset.csv`.

:::::::::::::::::::::::::::::::::::::::: solution

## Example command

```
Read 'clean_and_merge.py'. Modify the script to filter out any rows where 'score' is less than 10. Keep all other logic the same. Save the updated script.
```

### Reflection

*   Did the AI edit the relevant part or rewrite the whole file?
*   Did it include the necessary imports?
*   Did you check the changes before running the script?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Automating documentation

For the final step, have the AI generate a README that explains the data pipeline, including the raw files, cleaning steps, and final output format.

```
Create a README.md file that explains the data processing pipeline we just built. List the original files, the cleaning steps performed, and the final output format.
```

::::::::::::::::::::::::::::::::::::::::: challenge

## Challenge: Provenance tracking

To ensure research is reproducible, track which model generated your code and when.

1. Use the Gemini CLI to add a provenance header to `clean_and_merge.py`.
2. The header should be a Python docstring containing:
    - The model used (e.g., Gemini 2.0 Flash)
    - The date
    - A summary of the prompt.

:::::::::::::::::::::::::::::::::::::::: solution

## Example command

```
Read 'clean_and_merge.py'. Add a docstring at the very top of the file as a provenance header. Include the model name 'Gemini 2.5 Flash', today's date, and a summary of the prompt: 'Standardize site IDs, format dates, and impute missing scores with site medians.'
```

### Reflection
- Why record the model version and date?
- Does it matter if the AI model is updated later?
- How does this header help with reproducibility?

::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Use AI to automate data harmonization and standardization.
- Audit data before cleaning to identify inconsistencies.
- Read and test all generated code before running it.

::::::::::::::::::::::::::::::::::::::::::::::::::
