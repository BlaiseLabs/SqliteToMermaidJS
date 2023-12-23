import sqlite3

from jinja2 import Environment


class SqliteToMermaidJS:
    def __init__(self, db_path):
        """Initializes a SqliteToMermaidJS object.

        Args:
            db_path (str): The path to the SQLite database file.
        """
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.env = Environment(trim_blocks=True, lstrip_blocks=True)
        with open("./templates/mermaid_template.html") as template_file:
            self.mermaid_template = template_file.read()

    def get_tables(self):
        """Retrieves a list of table names from the SQLite database.

        Returns:
            list: A list of table names.
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [table[0] for table in self.cursor.fetchall()]

    def get_table_details(self, table_name):
        """Retrieves column information and foreign key information for a given
        table.

        Args:
            table_name (str): The name of the table.

        Returns:
            tuple: A tuple containing two lists - columns and foreign_keys.
                - columns: A list of column details.
                - foreign_keys: A list of foreign key details.
        """
        self.cursor.execute(f"PRAGMA table_info({table_name});")
        columns = self.cursor.fetchall()
        self.cursor.execute(f"PRAGMA foreign_key_list({table_name});")
        foreign_keys = self.cursor.fetchall()
        return columns, foreign_keys

    def preprocess_schema(self, schema):
        """Processes the schema data to a format more suitable for the
        template.

        Args:
            schema (dict): The original schema data with tables and details.

        Returns:
            dict: Preprocessed schema data.
        """
        processed_schema = {}
        for table, details in schema.items():
            processed_columns = [
                {"name": col[1], "type": col[2]} for col in details["columns"]
            ]
            processed_foreign_keys = [
                {"table": table, "ref_table": fk[2], "ref_column": fk[3]}
                for fk in details["foreign_keys"]
            ]
            processed_schema[table] = {
                "columns": processed_columns,
                "foreign_keys": processed_foreign_keys,
            }
        return processed_schema

    def generate_schema_diagram(self):
        """Generates an HTML schema diagram using the Mermaid.js template and
        the database schema information."""
        tables = self.get_tables()
        schema_info = {}
        for table in tables:
            columns, foreign_keys = self.get_table_details(table)
            schema_info[table] = {"columns": columns, "foreign_keys": foreign_keys}
        processed_schema = self.preprocess_schema(schema_info)
        template = self.env.from_string(self.mermaid_template)
        return template.render(schema=processed_schema)
