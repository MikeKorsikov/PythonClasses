import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/phonebook.db'
conn = sqlite3.connect(db_abs_path)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS contacts")

c.execute("""CREATE TABLE contacts(
                    id      INTEGER PRIMARY KEY AUTOINCREMENT,
                    name    TEXT,
                    phone   TEXT              
)""")


test_items = [
    ("Mykola Korsikov", "513-523-937"),
    ("Valeriia Kiparenko", "999-888-777")
]

c.executemany(
    "INSERT INTO contacts (name, phone) VALUES (?,?)", test_items)


conn.commit()
conn.close()

print("Database is created and initialized.")
print("You can see the table with the show_tables.py script.")
