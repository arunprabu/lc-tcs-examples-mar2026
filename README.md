# Multi-Agent AI Frameworks

This repository contains examples for modern multi-agent and generative AI frameworks in Python (and some TypeScript). The goal is to help developers compare approaches, run experiments, and build reusable patterns.

## 1. Core Multi-Agent Frameworks

- LangChain (Python, TypeScript)
- LangGraph (Python, TypeScript)
- Autogen (Python)
- CrewAI (Python)
- Agno (Python)

## 2. Traditional AI Use Cases

Common deterministic models and pipelines:

1. Recommendation systems
2. Classification
3. Prediction (regression and forecasting)
4. Object recognition

> These examples showcase structured machine learning workflows, pre-ML feature engineering, and deterministic inference paths.

## 3. Generative AI and LLMs

Key large language models covered or referenced:

1. OpenAI ChatGPT
2. Anthropic Claude
3. Google Gemini
4. xAI Grok
5. Deepseek
6. Alibaba Qwen
7. Mistral
8. Meta Llama

### Recommended Google Gemini variants

- `google_genai:gemini-3.1-pro-preview` (best quality, lower latency)
- `google_genai:gemini-3.1-flash-lite-preview` (lightweight + speed)
- `google_genai:gemini-3-flash-preview` (balanced performance)
- `google_genai:gemini-2.5-flash` (stable production)
- `google_genai:gemini-2.5-flash-lite` (cost-efficient)
- `google_genai:gemini-2.5-flash-preview-09-2025` (experimental)

## 4. Agent Tooling Guidelines

In agent custom tools, follow these rules:

- Implement tools as callable functions
- Include a concise `name`
- Add a clear `description`
- Return structured data (JSON-friendly)
- Pair tools with agent definitions
- One agent can share multiple tools

---

## Getting Started

1. Set up a Python virtual environment (e.g., `python -m venv .venv`)
2. Activate it (macOS / Linux: `source .venv/bin/activate`)
3. Install dependencies: `pip install -r requirements.txt` (if provided)
4. Run examples: `python example1.py`, etc.

## Contributing

- Add or update examples with reproducible code
- Add notes for API versions and required keys
- Keep model variants and prompts clearly documented
- Use comments to explain multi-agent coordination logic

============
