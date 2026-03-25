---
title: Setup
---

To follow this lesson, you will need the Gemini CLI and Python installed on your machine. The steps below get you set up with a direct local install, which is the approach used throughout the lesson.

## 1. Install Node.js and Python

- **Node.js**: Download the LTS version from [nodejs.org](https://nodejs.org) or use a package manager (`brew install node` on macOS).
- **Python**: Ensure you have Python 3.9+ installed. Check with `python --version`.

## 2. Install the Gemini CLI

```bash
npm install -g @google/gemini-cli
```

## 3. Authenticate

Run this command and sign in with your Google account when the browser opens:

```bash
gemini auth login
```

The CLI stores your credentials locally. You will not need to repeat this step.

## 4. Verify the install

```bash
gemini --version
```

If you see a version number, you are ready. If the command is not found, restart your terminal and try again.

<!-- TODO: Add a step here to configure the default model to gemini-2.5-flash-lite.
     This keeps all learners on the same free-tier model during the workshop.
     Need to confirm the correct mechanism for @google/gemini-cli:
       - Is it a config file (e.g. ~/.gemini/config.json or settings.json)?
       - An environment variable (GEMINI_MODEL or similar)?
       - A flag passed when starting the CLI?
       - A setting in GEMINI.md?
     Also decide whether to provide a pre-configured starter folder that learners
     download before class (with GEMINI.md and model config pre-set).
     Reflect the chosen approach in setup.md, episode 01 GEMINI.md example,
     and instructor notes. -->

:::::::::::::::::::::::::::::::::::::::::::::::::: caution

### Security and working directory

The Gemini CLI runs in your terminal and has direct access to the files in your current folder. A few habits to keep in mind:

1. Always start the CLI from a dedicated project folder, not your home directory.
2. Keep files under version control (Git) so you can revert unwanted changes.
3. Never start the CLI in folders with sensitive system files, credentials, or private data.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: callout

### Running in a sandbox (optional)

Some researchers prefer to isolate the CLI from their personal files entirely. Two options worth knowing about:

- **Docker**: The lesson repository includes a `Dockerfile` that builds a container with the Gemini CLI pre-installed. The agent can only see files you explicitly mount into it. See the [Docker documentation](https://docs.docker.com/) for setup, or [Docker AI Sandboxes](https://docs.docker.com/ai/sandboxes/) for a purpose-built option.
- **Agent Safehouse**: [agent-safehouse.dev](https://agent-safehouse.dev/) is a dedicated environment for running AI agents with built-in isolation controls.

Both approaches require more setup and are not needed for this workshop, but are worth exploring if you plan to use these tools regularly with sensitive data.

::::::::::::::::::::::::::::::::::::::::::::::::::

## Institutional context and access

Many campuses (like the University of California) have enterprise AI agreements. CLI access is often a separate feature that requires IT provisioning. If your institution's license does not cover the CLI, you may need to use a personal Google account for this workshop. Always follow your institution's data privacy policies.
