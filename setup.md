---
title: Setup
---

To follow this lesson, you will need the Gemini CLI and Python installed on your machine.

## Institutional Context & Access

Many universities, including campuses within the **University of California (UC)** system, have enterprise-wide agreements with major generative AI vendors (e.g., OpenAI for ChatGPT Enterprise/Edu and Google for Gemini). These agreements often provide **licensed web- or workspace-integrated access** with specific data protections and policy compliance.

However, access to **command-line (CLI) or API interfaces** through these institutional agreements is **not universal** and depends on local licensing and IT support. For this workshop, we will demonstrate the setup using the **Gemini CLI**. If your campus license does not include API access, you may need to use a personal account for the following steps.

::::::::::::::::::::::::::::::::::::::::: caution

## A Note on Privacy

Using **personal or consumer accounts** for sensitive institutional data or research may not meet your campus's compliance requirements and could pose privacy or security risks. Always check your institution’s IT guidance and acceptable use policies before using AI tools for institutional work.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Software Setup

::::::::::::::::::::::::::::::::::::::: discussion

### Details

We will be using the Gemini CLI (built on Node.js) and Python for data processing. Please follow the instructions below for your operating system.

:::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::: spoiler

### Windows

1. **Install Node.js**: Download the LTS version from [nodejs.org](https://nodejs.org).
2. **Install Python**: Download from [python.org](https://python.org) (ensure "Add to PATH" is checked).
3. **Open PowerShell as Administrator** and run:
   ```powershell
   npm install -g @google/generative-ai-cli
   ```
4. **Authenticate**:
   ```powershell
   gemini auth
   ```

::::::::::::::::::::::::

:::::::::::::::: spoiler

### MacOS

1. **Install Node.js**: `brew install node` (if you have Homebrew) or download from [nodejs.org](https://nodejs.org).
2. **Install Python**: `brew install python` or download from [python.org](https://python.org).
3. **Open Terminal** and run:
   ```bash
   npm install -g @google/generative-ai-cli
   ```
4. **Authenticate**:
   ```bash
   gemini auth
   ```

::::::::::::::::::::::::


:::::::::::::::: spoiler

### Linux

1. **Install Node.js and npm**:
   ```bash
   sudo apt install nodejs npm
   ```
2. **Install Gemini CLI**:
   ```bash
   npm install -g @google/generative-ai-cli
   ```
3. **Authenticate**:
   ```bash
   gemini auth
   ```

::::::::::::::::::::::::