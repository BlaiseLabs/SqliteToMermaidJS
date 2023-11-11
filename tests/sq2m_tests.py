import unittest
import sqlite3
import os
from jinja2 import Environment, Template
from SqliteToMermaidJS import SqliteToMermaidJS
# Unit test for the SqliteToMermaidJS class
class TestSqliteToMermaidJS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up a test database

        cls.db_path = './test_db.db'
        if os.path.exists(cls.db_path):
            os.remove(cls.db_path)
        connection = sqlite3.connect(cls.db_path)

        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE Users (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE
                        )''')
        cursor.execute('''CREATE TABLE Posts (
                            id INTEGER PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            title TEXT NOT NULL,
                            content TEXT NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES Users (id)
                        )''')
        cursor.execute('''CREATE TABLE Comments (
                            id INTEGER PRIMARY KEY,
                            post_id INTEGER NOT NULL,
                            user_id INTEGER NOT NULL,
                            comment TEXT NOT NULL,
                            FOREIGN KEY (post_id) REFERENCES Posts (id),
                            FOREIGN KEY (user_id) REFERENCES Users (id)
                        )''')
        connection.commit()
        connection.close()

    @classmethod
    def tearDownClass(cls):
        # Clean up the database file after tests
        os.remove(cls.db_path)

    def test_schema_generation(self):
        converter = SqliteToMermaidJS(self.db_path)
        html_output = converter.generate_schema_diagram()

        self.assertIn("class Users", html_output)
        self.assertIn("class Posts", html_output)
        self.assertIn("class Comments", html_output)
        self.assertIn("Posts --> Users", html_output)
        self.assertIn("Comments --> Posts", html_output)
        self.assertIn("Comments --> Users", html_output)

        # Read the XML content again
        with open('./test_html.html', 'w') as file:
             file.write(html_output)

if __name__ == '__main__':
    # Execute the test
    unittest.TextTestRunner().run(
      unittest.TestLoader().loadTestsFromTestCase(TestSqliteToMermaidJS)
    )
          
