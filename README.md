# SqliteToMermaidJS

## Overview
SqliteToMermaidJS is a Python tool for generating MermaidJS diagrams from SQLite database schema. It extracts the table structure and relationships from a SQLite database and converts them into an interactive MermaidJS diagram.

## Installation
To use SqliteToMermaidJS, clone this repository and install the required dependencies:
```
git clone https:/github.com/SqliteToMermaidJS.git
cd SqliteToMermaidJS
pip install -r requirements.txt
```

## Usage
To use SqliteToMermaidJS in your project:

1. Import the `SqliteToMermaidJS` class from `sqlite_to_mermaidjs.py`.
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
- `src/`: Contains the main module and Jinja2 templates.
- `tests/`: Unit tests for the SqliteToMermaidJS.
- `examples/`: Example scripts demonstrating the usage of the tool.

## Contributing
Contributions to the SqliteToMermaidJS project are welcome. Please follow the standard fork-and-pull request workflow.

## License
[Specify the license here, if applicable]
