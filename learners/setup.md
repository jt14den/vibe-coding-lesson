---
title: Setup
---

To follow this lesson, you will need the Gemini CLI and Python installed on your machine.

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