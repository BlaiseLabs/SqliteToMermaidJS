import os
import unittest
import sqlite3
from SqliteToMermaidJS import SqliteToMermaidJS

def create_sample_database(db_path):
    """
    Creates a sample SQLite database for demonstration purposes.
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE Users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );
    ''')

    cursor.execute('''
        CREATE TABLE Posts (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES Users (id)
        );
    ''')

    cursor.execute('''
        CREATE TABLE Comments (
            id INTEGER PRIMARY KEY,
            post_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            comment TEXT NOT NULL,
            FOREIGN KEY (post_id) REFERENCES Posts (id),
            FOREIGN KEY (user_id) REFERENCES Users (id)
        );
    ''')

    connection.commit()
    connection.close()

def main():
    db_path = 'sample_db.db'
    create_sample_database(db_path)

    converter = SqliteToMermaidJS(db_path)
    html_output = converter.generate_schema_diagram()

    with open('schema_diagram.html', 'w') as file:
        file.write(html_output)
    print("Schema diagram generated as 'schema_diagram.html'.")

if __name__ == '__main__':
    main()
