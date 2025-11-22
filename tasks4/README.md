# Task 4 — OpenAI Summarizer (tasks4)

This program demonstrates calling the OpenAI Chat Completions API from Python.
It reads multiple paragraph-length descriptions, sends each one to an OpenAI
model, and prints short summary phrases.

## Features
- Uses the OpenAI Python client library
- Loads your API key from the `OPENAI_API_KEY` environment variable
- Summarizes multiple paragraphs in a loop
- Can be run using `uv` as a command-line tool

## Requirements
- Python 3.13+ (handled automatically by `uv`)
- An OpenAI API key stored in your environment variables:
  - Windows (PowerShell):
    ```powershell
    setx OPENAI_API_KEY "your_real_key_here"
    ```
  - macOS/Linux:
    ```bash
    export OPENAI_API_KEY="your_real_key_here"
    ```

## How to Run
From the `tasks4` directory:

```bash
uv sync
uv run tasks4
