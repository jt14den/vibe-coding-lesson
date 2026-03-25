---
title: Setup
---

To follow this lesson, you will need the Gemini CLI and Python installed on your machine. The primary benefit of a CLI-based AI is its ability to interact directly with your local files and environment. For advanced users, we recommend using a **Sandbox** to isolate the agent from your sensitive files.

## Path 1: Direct Local Install (Recommended)

This is the standard way to use CLI AI tools. It gives the agent direct access to your project files, allowing it to read data, write scripts, and run commands in your actual working directory.

:::::::::::::::::::::::::::::::::::::::::::::::::: caution

### A Note on Security & Sandboxing

Giving an AI agent direct access to your filesystem is a significant responsibility. A buggy or misaligned agent could theoretically modify or delete important files. 

**Some researchers prefer to run these tools in a "Sandbox"** to isolate the agent from their personal files. We provide a `Dockerfile` and instructions for this in the **Path 2: Docker** below. However, for this workshop, you can run the tool directly as long as you:
1. Only run the agent in dedicated project folders.
2. Ensure you have a backup or use Git to track changes.
3. Never run the agent in folders containing sensitive system configuration or personal data (like your Home directory or `.ssh` folder).

::::::::::::::::::::::::::::::::::::::::::::::::::

### 1. Install Node.js & Python
- **Node.js**: Download the LTS version from [nodejs.org](https://nodejs.org) or use a package manager (`brew install node`).
- **Python**: Ensure you have Python 3.9+ installed (`python --version`).

### 2. Install the Gemini CLI
Open your terminal and run:
```bash
npm install -g @google/gemini-cli
```

### 3. Authenticate
You will need an API key from [Google AI Studio](https://aistudio.google.com/).
```bash
export GEMINI_API_KEY=your_api_key_here
```
*(Tip: Add this line to your `.bashrc` or `.zshrc` to make it permanent.)*

---

## Path 2: Local Sandbox (Advanced / Docker)

If you are comfortable with Docker and want the extra security of an isolated environment, you can use our pre-configured sandbox. This requires some additional setup but ensures the AI cannot see anything outside the folder you "mount" to it.

1.  **Install Docker Desktop**: Download from [docker.com](https://www.docker.com/).
2.  **Build the Sandbox**:
    ```bash
    docker build -t vibe-coding-sandbox .
    ```
3.  **Run the Sandbox**:
    ```bash
    docker run -it -v "$(pwd):/home/researcher/project" -e GEMINI_API_KEY=$GEMINI_API_KEY vibe-coding-sandbox
    ```
    *This command "mounts" your current folder into the container, allowing the AI to work only on those files.*

---

## Path 3: Dedicated AI Sandboxes (Automated)

Modern tools now offer automated sandboxing specifically for AI agents. These provide a more seamless experience than manual Docker configuration.

*   **[Agent Safehouse](https://agent-safehouse.dev/)**: A specialized environment for running AI agents safely with built-in security controls.
*   **[Docker AI Sandboxes](https://docs.docker.com/ai/sandboxes/)**: Docker's official solution for creating isolated, ephemeral environments for AI development.

---

## Path 4: GitHub Codespaces (Zero-Install Trial)

If you just want to try the tools without installing anything, you can launch this lesson in a browser. This is great for a quick demo, but remember that **you are not acting on your own local files**; you are in a temporary cloud environment.

1.  **Open the Repository**: [jt14den/vibe-coding-lesson](https://github.com/jt14den/vibe-coding-lesson)
2.  **Launch Codespace**: Click **Code > Codespaces > Create codespace on main**.
3.  **Set Key**: Run `export GEMINI_API_KEY=your_key` inside the codespace terminal.

---

## Institutional Context & Access

Many campuses (like the University of California) have enterprise AI agreements. However, CLI/API access is often a separate feature that must be requested from IT. If your campus license doesn't cover the CLI, you may need to use a personal account for this workshop. **Always follow your institution's data privacy policies.**
