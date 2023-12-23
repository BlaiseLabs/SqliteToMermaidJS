# SqliteToMermaidJS

## Overview

SqliteToMermaidJS is a Python script for generating MermaidJS diagrams from SQLite database schemas. It extracts the table structure and relationships from an SQLite database and converts them into an interactive MermaidJS diagram.

![Animation of user interface](sq2m.webp)

Certainly, I'll break down the installation instructions into detailed subsections with explanations and provide Windows alternatives where applicable.

## Installation

### 1. Clone the Repository

First, you need to clone the SqliteToMermaidJS repository from GitHub. This step downloads the project's source code to your local machine.

```sh
git clone https:/github.com/SqliteToMermaidJS.git
```

**Alternative:** You can use Git Bash or the GitHub Desktop application to clone repositories. The command remains the same.

### 2. Navigate to the Project Directory

Change your current working directory to the newly cloned repository. This step is necessary to access and work with the project's files.

```sh
cd SqliteToMermaidJS
```

### 3. Create a Virtual Environment

Creating a virtual environment is a best practice to isolate project dependencies. It ensures that the required packages won't interfere with other Python projects on your system.

```sh
python -m venv .venv
```

### 4. Activate the Virtual Environment

Activating the virtual environment allows you to work within the isolated environment where you can install project-specific packages without affecting your global Python installation.

```sh
source .venv/bin/activate
```

On Windows, use the following command to activate the virtual environment in Command Prompt:

```sh
.venv\Scripts\activate
```

### 5. Install Required Dependencies

Finally, you need to install the project's required Python packages, as listed in the `requirements.txt` file. This ensures that your environment has all the necessary libraries to run SqliteToMermaidJS.

```sh
pip install -r requirements.txt
```

To update your README with instructions for running tests and the example file, you can add new sections under the "Usage" part. Here's a suggestion for how to structure and word these additions:

---

## Usage

### Running the Example Script

To see SqliteToMermaidJS in action, you can run the example script provided in the `examples/` directory. This script demonstrates how to use the tool to generate a MermaidJS diagram from an SQLite database.

1. Navigate to the project's root directory.
2. Run the following command:

```sh
python -m examples.example_usage
```

This will execute the example script and produce an output demonstrating the tool's functionality.

### Running Tests

To ensure that SqliteToMermaidJS works as expected, you can run the unit tests provided in the `tests/` directory. These tests verify various aspects of the tool's functionality.

1. Ensure you are in the project's root directory.
2. Run the tests using the following command:

```sh
python -m tests.sq2m_tests
```

This command runs all the unit tests and outputs the results, indicating whether each test passed or failed.

## Project Structure

- `templates/`: Contains the Jinja2 template.
- `tests/`: Unit tests for the SqliteToMermaidJS.
- `examples/`: Example scripts demonstrating the usage of the tool.

## Pre-commit Hooks

This project uses [pre-commit hooks](https://pre-commit.com/) to ensure code quality and consistency. Pre-commit hooks run checks on your files before you commit them, helping to catch issues early in the development process.

### Installing Pre-commit

To use these hooks, you need to install `pre-commit` on your machine. Follow the detailed installation instructions on the [pre-commit installation page](https://pre-commit.com/#install).

### Setting up Pre-commit in the Project

Once `pre-commit` is installed, set it up in your local repository with the following command:

```sh
pre-commit install
```

This command will install the pre-commit hooks defined in the `pre-commit-config.yaml` file into your local `.git/hooks` directory.

### Running Pre-commit Hooks

With pre-commit installed, the hooks will automatically run on each `git commit` attempt. If any hooks make changes or fail, you'll need to re-stage your changes and commit again.

You can also manually run the hooks on all files in the repository with:

```sh
pre-commit run --all-files
```

This command is particularly useful to run before creating a pull request or as part of your regular development process to ensure your changes conform to the project's standards.

## Contributing

Contributions to the SqliteToMermaidJS project are welcome. Please follow the standard fork-and-pull request workflow.

## MIT License

Copyright (c) 2023 Blaiselabs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
