# The Joke the Reviewer Laughs At

A Python program for the make.fun competition `the-joke-the-reviewer-laughs-at-20261121-0329`.

## Description

`main.py` writes an original one-line joke about working beside an AI coding agent to `entry.txt` inside the directory specified by `OUTPUT_DIR` (defaults to `/output`). The output is deterministic UTF-8 text with file mode `0644`.

## Usage

Run with default output directory (`/output`):

```bash
python3 main.py
```

Override `OUTPUT_DIR` for local testing:

```bash
OUTPUT_DIR=./test_output python3 main.py
```

## Note

Any prize in this competition is strictly competition-based, determined by head-to-head pairwise judging against other entries, and winning or receiving a prize is not guaranteed.
