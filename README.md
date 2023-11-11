# SqliteToMermaidJS

## Overview
SqliteToMermaidJS is a Python tool for generating MermaidJS diagrams from SQLite database schemas. It extracts the table structure and relationships from an SQLite database and converts them into an interactive MermaidJS diagram.

## Installation
To use SqliteToMermaidJS, clone this repository and install the required dependencies:
```
git clone https:/github.com/SqliteToMermaidJS.git
cd SqliteToMermaidJS
pip install -r requirements.txt
```

## Usage
To use SqliteToMermaidJS in your project:

1. Import the `SqliteToMermaidJS` class from `SqliteToMermaidJS.py`.
2. Initialize the class with the path to your SQLite database.
3. Call the `generate_schema_diagram` method to create the diagram.

Example:
```python
from SqliteToMermaidJS import SqliteToMermaidJS

converter = SqliteToMermaidJS("path_to_your_database.db")
html_output = converter.generate_schema_diagram()
# Save or display the HTML output as needed
```

## Project Structure
- `templates/`: Contains the Jinja2 template.
- `tests/`: Unit tests for the SqliteToMermaidJS.
- `examples/`: Example scripts demonstrating the usage of the tool.

## Contributing
Contributions to the SqliteToMermaidJS project are welcome. Please follow the standard fork-and-pull request workflow.

## MIT License


Copyright (c) 2023 blaiselabs

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
