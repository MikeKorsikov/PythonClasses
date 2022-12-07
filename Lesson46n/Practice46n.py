# 29/11/2022 cancelled
# 01/12/2022 MySQL, MongoDB, SQLite
from getpass import getpass

from mysql.connector import connect

create_table = '''CREATE TABLE IF NOT EXISTS person(
        id INT AUTO_INCREMENT PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        AGE INT)'''

try:
    with connect(
            host='127.0.0.1',
            user='root',
            password='2020Gsk+my',
            # database='classicmodels'
    ) as conn:
        with conn.cursor() as cur:
            cur.execute('USE mydb')
            cur.execute(create_table)  # see create_table above
            cur.execute('SHOW DATABASES;')
            for row in cur:
                print(row)

except Exception as e:
    print(f"Error: {e}")
