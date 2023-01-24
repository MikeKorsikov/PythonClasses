import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/phonebook.db'
conn = sqlite3.connect(db_abs_path)
c = conn.cursor()


def show_records():
    try:
        records = c.execute("SELECT c.id, c.name, c.phone FROM contacts AS c")

        print("Contacts:")
        print("#############")
        for row in records:
            print("ID:    ", row[0]),
            print("Name:  ", row[1]),
            print("Phone: ", row[2])

            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()


show_records()

conn.close()
