<p align="center">
    <a href="https://github.com/Devin-Cook/explORE-AI"><img src="./assets/explore_logo.svg" alt="explORE-AI Logo" width="5000"></a>
</p>

# explORE-AI — A Specialized Fork of Aider for Open Source Risk Engine (ORE)

<p align="center">
  <em>Built upon the amazing foundation of <a href="https://aider.chat/">Aider</a></em>
</p>

**explORE-AI** helps you navigate, understand, and contribute to the **Open Source Risk Engine (ORE)** codebase. Originally derived from the powerful [Aider](https://github.com/Aider-AI/aider) AI pair-programming tool, this fork is tailored for **domain-specific insights** into ORE. If you find Aider useful for general purposes, please check out their project. For **ORE-focused** development, read on!

<p align="center">
  <img
    src=".\assets\terminal.svg"
    alt="explORE-AI screencast"
  >
</p>

<p align="center">
<!--[[[cog
from scripts.badges import get_badges_md
text = get_badges_md()
cog.out(text)
]]]-->
  <a href="https://github.com/Aider-AI/aider/stargazers"><img alt="GitHub Stars" title="Total number of GitHub stars the Aider project has received"
src="https://img.shields.io/github/stars/Aider-AI/aider?style=flat-square&logo=github&color=f1c40f&labelColor=555555"/></a>
  <a href="https://pypi.org/project/aider-chat/"><img alt="PyPI Downloads" title="Total number of installations via pip from PyPI"
src="https://img.shields.io/badge/📦%20Installs-1.7M-2ecc71?style=flat-square&labelColor=555555"/></a>
  <img alt="Tokens per week" title="Number of tokens processed weekly by Aider users"
src="https://img.shields.io/badge/📈%20Tokens%2Fweek-15B-3498db?style=flat-square&labelColor=555555"/>
  <a href="https://openrouter.ai/"><img alt="OpenRouter Ranking" title="Aider's ranking among applications on the OpenRouter platform"
src="https://img.shields.io/badge/🏆%20OpenRouter-Top%2020-9b59b6?style=flat-square&labelColor=555555"/></a>
  <a href="https://aider.chat/HISTORY.html"><img alt="Singularity" title="Percentage of the new code in Aider's last release written by Aider itself"
src="https://img.shields.io/badge/🔄%20Singularity-92%25-e74c3c?style=flat-square&labelColor=555555"/></a>
<!--[[[end]]]-->
</p>

## Why explORE-AI?

[Open Source Risk Engine (ORE)](https://github.com/OpenSourceRisk/Engine) is a large and sophisticated library for risk analytics, financial instrument modeling, and more. Diving into ORE can be **intimidating** due to its size and complexity.

**explORE-AI**:

- Leverages **Aider**’s AI pair-programming features and **tailors** them for ORE development.
- Provides specialized insights into ORE’s architecture, including analytics, classes, and data relationships.
- Helps generate targeted refactors, test scaffolds, or risk analytics examples relevant to ORE.

We owe a **huge thanks** to [Aider](https://github.com/Aider-AI/aider) for providing the robust foundation that made this fork possible.

## Features

- 🏦 **ORE-Specific Insights** — **explORE-AI** can reference and analyze ORE’s specific code structure, giving more precise guidance.
- 🗺️ **Codebase Mapping** — Just like Aider, but with a deeper understanding of the ORE ecosystem.
- 🧠 **[Cloud and Local LLMs](https://aider.chat/docs/llms.html)** — Choose from Claude, DeepSeek, GPT variants, or almost any other LLM.
- `</>` **[Multi-Language Support](https://aider.chat/docs/languages.html)** — Even though ORE is mostly C++, explORE-AI supports 100+ coding languages.
- 🔀 **[Git Integration](https://aider.chat/docs/git.html)** — Automatic commits with sensible messages, so you can track AI-generated changes effortlessly.
- 🏗️ **Domain-Specific Testing & Linting** — Integrates smoothly with ORE’s tests or any specialized linters to ensure high-quality code.
- 🗣️ **Voice-to-Code** — Request new features, bug fixes, or run analytics queries by voice.
- 📋 **[Copy/Paste Web Chat](https://aider.chat/docs/usage/copypaste.html)** — If you need to jump into a browser-based LLM environment, explORE-AI makes it easier.

## Getting Started

```bash
# 1. Clone this explORE-AI repository
git clone https://github.com/Devin-Cook/explORE-AI.git

# 2. Install
python -m pip install ./explore-ai

# 3. Navigate to your ORE codebase
cd /path/to/OpenSourceRiskEngine

# 4. Launch explORE-AI with your preferred model:
aider --model deepseek --api-key deepseek=<key>

# Example for Claude:
aider --model sonnet --api-key anthropic=<key>

# Example for o3-mini:
aider --model o3-mini --api-key openai=<key>
