# 🤖 98 - Python Automation

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Automation](https://img.shields.io/badge/Automation-Selenium%20%7C%20Python-green)
![Status](https://img.shields.io/badge/Project-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

------------------------------------------------------------------------

## Overview

**98 -- Python Automation** is part of the **100 Python Projects
Challenge** and focuses on building practical automation tools using
Python.\
The project demonstrates how repetitive development tasks can be
streamlined through scripting and intelligent workflow automation.

The automation tool scans a repository, detects Python-based projects,
and automatically generates a structured project index.\
This ensures the repository remains organized, discoverable, and ready
for integration with portfolio platforms.

Designed with efficiency in mind, the automation reduces manual
documentation work and maintains an up‑to‑date overview of all projects.

------------------------------------------------------------------------

## Features

✔ Automatic detection of Python projects\
✔ Generates a structured project index file\
✔ Tracks project modification dates\
✔ Supports Git automation for commits and pushes\
✔ Lightweight implementation with no external dependencies

------------------------------------------------------------------------

## Project Structure

    98-python-automation
    │
    ├── auto_repo_manager.py
    ├── config.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## How It Works

The automation script performs the following actions:

1.  Scans the repository directory
2.  Detects folders containing Python files
3.  Extracts project metadata
4.  Generates a Markdown project index
5.  Optionally commits and pushes updates to GitHub

This workflow keeps project documentation synchronized with the
repository contents.

------------------------------------------------------------------------

## Running the Automation

``` bash
python auto_repo_manager.py
```

After execution, the script generates:

    PROJECT_INDEX.md

This file contains an automatically updated list of projects detected in
the repository.

------------------------------------------------------------------------

## Example Output

    # 100 Python Projects Challenge

    ## Projects

    ### 01-password-generator
    - Python files: main.py
    - Last updated: 2026-03-07

    ### 02-number-guessing
    - Python files: game.py
    - Last updated: 2026-03-06

------------------------------------------------------------------------

## Technology Stack

-   **Python**
-   **Filesystem Automation**
-   **Git Integration**
-   **Repository Management**

------------------------------------------------------------------------

## Use Cases

This automation approach can be adapted for:

-   Developer portfolio maintenance
-   Repository documentation generation
-   Continuous project indexing
-   Workflow automation for development environments

------------------------------------------------------------------------

## License

This project is released under the **MIT License**.
