# Coffee Shop Knowledge Assistant

A Python prototype for answering coffee-shop questions using a Markdown knowledge base and Google Gemini. The app is built as a LangGraph workflow: it prompts for a question, requests tags, selects a knowledge-base file by tag overlap, and asks Gemini to produce an answer.

## Requirements

- Python 3.13 (or a compatible Python version)
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/)

## Setup

1. Clone the repository and open a terminal in the project directory.
2. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Gemini API key:

   ```dotenv
   GEMINI_API_KEY=your_api_key_here
   ```

   `GOOGLE_API_KEY` is also accepted. Keep your key private; `.env` is excluded from Git.

## Run

From the project root, run:

```bash
python main.py
```

Enter a question when prompted. For example:

```text
What do u wanna ask? How much is a latte?
```

The workflow prints its resulting state, including the generated answer. Gemini API access, a valid key, and available API quota are required.

## Workflow

1. Prompt for a question.
2. Ask Gemini for structured tags using the uploaded knowledge-base index.
3. Compare those tags with the `tags` metadata in Markdown files under `knowledge_base/`.
4. Upload the selected file and ask Gemini to answer the question from it.

## Knowledge base

Knowledge-base documents are Markdown files with YAML frontmatter. For example:

```markdown
---
type: menu
title: Drink Menu
tags: [menu, coffee]
---

# Drink Menu

Document content goes here.
```

Add or edit `.md` files anywhere under `knowledge_base/`. Each document should have a `tags` list so the workflow can compare it with the predicted tags.

Current categories include `coffee`, `hot`, `cold`, `milk`, `menu`, `policy`, `staff`, `hardware`, and `operations`.

## Project structure

```text
.
├── main.py                 # Builds and runs the LangGraph workflow
├── nodes/
│   ├── input_question.py   # Reads a question from the terminal
│   ├── filter_tag.py       # Requests tags from Gemini
│   ├── feed_the_files.py   # Selects a Markdown file by tag overlap
│   └── final_ouput.py      # Generates the final answer with Gemini
├── others/
│   ├── models.py           # Gemini chat model configuration
│   ├── state.py            # Workflow state schema
│   └── structure.py        # Structured tag-output schema
├── knowledge_base/         # Markdown source documents
├── requirements.txt
└── .env                    # Local API key; do not commit
```

## Notes

- The tag model is configured to return two or three categories.
- The current tag step does not include the user's question in its prompt; tag selection may therefore not reflect the question until that step is updated.
- File selection is based on tag overlap, so make sure knowledge-base documents have useful, consistent tags.
- `tests.py` is currently a small manual script for reading the menu document, not a full automated test suite.
