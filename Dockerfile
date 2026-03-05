# Use a Node.js LTS base image
FROM node:20-bullseye-slim

# Install Python and other necessary tools
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set up a non-root user for security
RUN useradd -m -s /bin/bash researcher
USER researcher
WORKDIR /home/researcher/project

# Install the Gemini CLI globally as the researcher user
# Note: npm global install might need some configuration for non-root, 
# but in a container we can often just use a local bin or adjust PATH.
ENV NPM_CONFIG_PREFIX=/home/researcher/.npm-global
ENV PATH=$PATH:/home/researcher/.npm-global/bin

RUN npm install -g @google/generative-ai-cli

# Default command
CMD ["bash"]
