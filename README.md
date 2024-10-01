# AI Slide Creator: Workflow Guide

Welcome to the **AI Slide Creator** project! This guide provides a streamlined workflow to create professional slide decks effortlessly using Large Language Models (LLMs) and Marp.

## Overview

This project is about **suggesting a workflow** for generating slide content from a text prompt and transforming it into styled slide decks in both PDF and PPTX formats, using the power of AI and Marp.

## Table of Contents

- [AI Slide Creator: Workflow Guide](#ai-slide-creator-workflow-guide)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Workflow](#workflow)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Customization](#customization)
    - [Custom Theme CSS](#custom-theme-css)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- **Prompt-to-Slides Workflow:** A clear step-by-step process for generating slide content from text prompts.
- **Marp Integration:** Utilize the Marp VS Code extension for slide visualization and editing.
- **Export Formats:** Suggestions for exporting your slides to PDF and PPTX formats.
- **Customization Tips:** Guidance on how to customize the appearance of your slides with custom CSS.

## Getting Started

## Workflow

1. **Prepare Your Prompt:**
   - Create a prompt by editing the topic section in the `prompt_template.md` file in this repo.
2. **Generate Slides with LLM:**
   - Use an LLM to process the custom prompt and generate a clean markdown file (e.g. `slide-deck.md`) containing the slide content.
3. **Review and Edit:**
   - Open `slide-deck.md` in VS Code with the [Marp VS Code extension](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) to preview and refine the slides.
4. **Export Slides:**
   - Convert your slide deck to PDF or PPTX using the Marp CLI tool:
   
   ```sh
    npx @marp-team/marp-cli@latest slide-deck.md -o output.pdf
    npx @marp-team/marp-cli@latest slide-deck.md -o output.pptx
    ```
   - (Optional) For an editable PDF, use [Adobe’s online converter](https://www.adobe.com/acrobat/online/pdf-to-ppt.html). Note that the layout may be slightly altered.

## Installation

### Prerequisites

- Node.js and npm installed
- Marp VS Code extension

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ai-slide-creator.git
    cd ai-slide-creator
    ```

2. Install Marp CLI:
    ```sh
    npm install --save-dev @marp-team/marp-cli
    ```

## Customization

### Custom Theme CSS

For additional customization, refer to Marp’s [theme CSS documentation](https://marpit.marp.app/theme-css?id=create-theme-css). You can create your own theme.css file and apply it to your slide deck.

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This workflow aims to simplify and optimize the process of slide creation using AI and Marp. Should you have any questions, encounter issues, or have suggestions, feel free to open an issue or submit a pull request.

---

Let's make slide creation smarter and more efficient! 🚀