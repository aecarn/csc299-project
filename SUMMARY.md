# Development Summary for CSC 299 Final Project

This project started from a very simple idea and gradually turned into a more structured personal task management system with AI-assisted features. Over the quarter I used several different AI coding tools: Chat-based assistants (like ChatGPT), GitHub Copilot inside VS Code, and the Python testing ecosystem around `pytest` and `uv`. This summary explains how I used those tools, what worked, what did not, and how the different prototypes (tasks1–tasks5) fit together into a single development story.

## Overall Software Design

The main core of the project is a JSON-backed task manager that lives in the `tasks1`, `tasks2`, and `tasks3` directories. It started as a basic command-line tool that could add, list, and search tasks in a `tasks.json` file. Over time I iterated on this to add features like marking tasks as done, better formatting, and then eventually turning it into a proper Python package managed with `uv` in `tasks3`, with tests written in `pytest`.

On top of this base, I did a separate AI-related experiment in `tasks4`, where the goal was not to handle storage, but to call the OpenAI Chat Completions API to summarize paragraph-length task descriptions into short phrases. Finally, for `tasks5`, I used GitHub’s spec-kit tooling to initialize a separate project and then copied that spec-kit-generated structure into a `tasks5` directory in this repository, as requested.

## How I Used AI Coding Assistants

I used chat-based AI heavily throughout the project. For example, I used ChatGPT to help me:

- Plan the structure of the task manager in `tasks1` and `tasks2`.
- Understand and set up `uv`, virtual environments, and `pyproject.toml` for `tasks3`.
- Write and refine `pytest` test functions, especially for the `inc` function and for the `next_id` helper in the task manager.
- Debug confusing errors with `uv run`, script entrypoints, and environment variables.
- Set up `tasks4` with the OpenAI client and read the `OPENAI_API_KEY` from environment variables instead of hardcoding secrets.
- Navigate the spec-kit tooling for `tasks5` and understand how to copy the generated project into the correct place.

I also used GitHub Copilot inside VS Code. Copilot was most helpful for small things: auto-completing function definitions, suggesting basic test cases, and filling in boilerplate, especially in the parser code and in test files. Sometimes it suggested code that did not match my actual structure, so I had to double-check everything against my own logic and the assignment instructions.

## What Worked Well

Using AI as a “pair programmer” worked surprisingly well for:

- Breaking down tasks into smaller steps (e.g., “first set up `uv`, then move `main.py` into `src/`, then wire the entrypoint”).
- Translating the assignment’s technical wording into plain language so I understood what the professor actually wanted.
- Quickly writing README files and documentation that matched what my code already did.
- Short debugging sessions where I pasted error messages and got explanations of what they meant and which file to fix.

Tests were another thing that worked well. Once I had `pytest` running for `tasks3`, adding tests for `next_id` was straightforward, and seeing “3 passed” was a nice confirmation that my refactoring did not break anything.

## What Did Not Work or Was Hard

Several things did not go smoothly on the first try. My Windows environment is a bit messy: PowerShell is effectively broken, which made some of the recommended workflows (like npm-based tools and certain script commands) frustrating or impossible. I had to fall back to `uvx` and other workarounds for spec-kit, and in the end I could only partially run the generation locally before copying the generated structure into `tasks5` as required.

I also had multiple moments where entrypoints failed with “program not found” errors when running `uv run tasks3` or `uv run tasks4`. In those cases, the fix was usually something subtle in `pyproject.toml`, such as adding `[project.scripts]` or the `[build-system]` block and running `uv sync`. These were not obvious at first, and I needed help from the AI assistant to interpret the error messages.

Another challenge was managing all the moving parts at once: the original JSON task manager, the `uv` packaging, the tests, the OpenAI API experiment, and the spec-kit integration. The project instructions are dense, and I had to keep returning to them and cross-checking that each tasksN directory matched the professor’s expectations.

## Reflection

Overall, I really did use AI coding assistants as an integral part of my workflow for this project, but not as a one-click solution. They helped me get unstuck, understand tools like `uv` and `pytest`, and write cleaner documentation. At the same time, I still had to run the code myself, debug path and environment issues, and make sure everything worked on my own machine. The final result is a set of prototypes (tasks1–tasks5) that show my progress from a simple script to a tested package with some AI functionality, plus an honest record of the false starts and workarounds required to get there.
