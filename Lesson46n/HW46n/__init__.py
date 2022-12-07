# HW to create app which will communicate with mySQL database

from mysql.connector import connect
import sys
import time
import csv

# global variables
selected_table = ""
dict_of_columns = {}
dict_of_tables = {}
dict_of_reports = {}
updated_record = {}


# my_db = ""
# my_cursor = ""

# Menu 0
def menu():
    try:
        choice = 0
        while choice != 7:
            print(f"\n\tMENU:"
                  f"\n[1] Connect to DB"
                  f"\n[2] Show available tables"
                  f"\n[3] Add new record"
                  f"\n[4] Update record"
                  f"\n[5] Delete record"
                  f"\n[6] Generate report"
                  f"\n[7] Quit")

            choice = int(input(f'\nPlease enter option from the menu: '))
            time.sleep(1)

            match choice:
                case 1:
                    connect_db()
                case 2:
                    show_tables()
                case 3:
                    add_new_record()
                case 4:
                    update_record()
                case 5:
                    delete_record()
                case 6:
                    generate_report()
                case 7:
                    quit_program()

    except Exception as e:
        print(f"[0] Error: {e}")
    except KeyboardInterrupt:
        print("\n\n\t>>> Session terminated <<<")


# Submenu 1
def connect_db():
    global my_db, my_cursor
    print("\n\t[1] Connect to DB")
    try:
        # host_given = str(input("Enter host IP to db: "))
        # user_given = str(input("Enter user login to db: "))
        # password_given = str(input("Enter password to db: "))
        database_given = str(input("Enter DB name to connect to: "))

        my_db = connect(
            host='127.0.0.1',  # '127.0.0.1'
            user='root',  # root
            password='2020Gsk+my')  # '2020Gsk+my'

        my_cursor = my_db.cursor(buffered=True)
        my_cursor.execute(f"USE {database_given};")

        # checking if connection is successful
        if test_connection():
            print(f"\nSuccessfully connected to database: {database_given}!")

        time.sleep(1)

    except Exception as e:
        print(f"[1] Error: {e}")


# Submenu 2
def show_tables():
    print("\n\t[2] Show available tables")
    try:
        if test_connection():
            extract_tables()
            for key, value in dict_of_tables.items():
                print(f"[{key}] - {value}")
        go_on()
    except Exception as e:
        print(f"[2] Error: {e}")


# Submenu 3
def add_new_record():
    print("\n\t[3] Add new record")
    global selected_table
    try:
        if test_connection():
            extract_tables()  # to get the latest list of tables
            print("Which table would you like to update?")
            for key, value in dict_of_tables.items():
                print(f"[{key}] - {value}")
            selection = int(input(">>> "))
            selected_table = dict_of_tables[selection]  # will be used for writing query
            print(f"CHECK - Selected Table: {selected_table}")

            # extract list of columns
            extract_columns()

            print(f"\nProvide details for the following fields:")
            new_record = {}
            for key, value in dict_of_columns.items():
                input_given = input(f"[{key}] - {value}: ")

                if isinstance(input_given, str):
                    new_record[value] = str(input_given)
                elif isinstance(input_given, int):
                    new_record[value] = int(input_given)
            print(f"CHECK - New Record: {new_record}")

            # statement
            list_of_columns = []
            list_of_values = []
            for key, value in new_record.items():
                list_of_columns.append(key)
                if isinstance(value, int):
                    list_of_values.append(int(value))
                elif isinstance(value, str):
                    list_of_values.append(f"'{value}'")

            list_of_columns2 = ', '.join(list_of_columns)
            print(f"CHECK - List of columns: {list_of_columns2}")

            list_of_values2 = ', '.join(list_of_values)
            print(f"CHECK - List of values: {list_of_values2}")

            statement = f"INSERT INTO {selected_table} ({list_of_columns2}) VALUES ({list_of_values2})"
            print(f"CHECK - MySQL statement: {statement}")

            my_cursor.execute(statement)
            my_db.commit()
            print("New record added successfully!")

        go_on()
    except Exception as e:
        print(f"[3] Error (add new record): {e}")


# Submenu 4
def update_record():
    print("\n\t[4] Update existing record")
    try:
        global updated_record
        global selected_table

        if test_connection():
            print("Which table would you like to update?")

            extract_tables()
            for key, value in dict_of_tables.items():
                print(f"[{key}] - {value}")
            selection = int(input(">>> "))
            selected_table = dict_of_tables[selection]  # will be used for writing query
            print(f"CHECK - Selected Table: {selected_table}")

            statement = f"SELECT * FROM {selected_table};"
            print(f"CHECK - MySQL statement: {statement}")
            my_cursor.execute(statement)

            print(f"\nTable content:")
            table_content = my_cursor.fetchall()
            for record in table_content:
                print(str(record))
            time.sleep(2)

            print(f"\nWhich record ID you want to update?")
            id_selected = int(input(">>> "))

            id_statement = f"SELECT * FROM {selected_table} WHERE Id = {id_selected};"
            my_cursor.execute(id_statement)
            record_content = my_cursor.fetchall()
            print(record_content)

            extract_columns()

            # collecting details for the record to be updated
            print(f"\nWhich field do you want to update:")
            for key, value in dict_of_columns.items():
                print(f"[{key}] - {value}")
            selected_field = int(input(">>> "))

            print(f"Enter new value for {dict_of_columns[selected_field]}.")
            new_value = input(">>> ")
            if isinstance(new_value, str):
                new_value2 = str(new_value)
            elif isinstance(new_value, int):
                new_value2 = int(new_value)

            # statement
            statement = f"UPDATE {selected_table} SET {dict_of_columns[selected_field]} = '{new_value2}' WHERE Id = '{id_selected}';"
            print(f"CHECK - MySQL statement: {statement}")

            my_cursor.execute(statement)
            my_db.commit()
            print("Record updated successfully!")

        go_on()
    except Exception as e:
        print(f"[4] Error: {e}")


# Submenu 5
def delete_record():
    print("\n\t[5] Delete record")
    try:
        global selected_table
        if test_connection():
            print("Which table would you like to update?")

            extract_tables()
            for key, value in dict_of_tables.items():
                print(f"[{key}] - {value}")
            selection = int(input(">>> "))
            selected_table = dict_of_tables[selection]  # will be used for writing query
            print(f"CHECK - Selected Table: {selected_table}")

            statement = f"SELECT * FROM {selected_table};"
            print(f"CHECK - MySQL statement: {statement}")
            my_cursor.execute(statement)

            print(f"\nTable content:")
            table_content = my_cursor.fetchall()
            for record in table_content:
                print(str(record))
            time.sleep(2)

            print(f"\nWhich record ID you want to delete?")
            id_to_delete = int(input(">>> "))

            delete_statement = f"DELETE FROM {selected_table} WHERE Id = '{id_to_delete}';"
            print(f"CHECK - MySQL statement: {delete_statement}")

            my_cursor.execute(delete_statement)
            my_db.commit()
            print("Record successfully deleted!")

        go_on()
    except Exception as e:
        print(f"[5] Error: {e}")


# Submenu 6
def generate_report():
    print("\n\t[6] Generate report")
    try:
        global dict_of_reports
        global dict_of_columns
        list_of_column_names = []
        if test_connection():
            print("\n\tList of available reports:"
                  "\n[1] Information about all groups"
                  "\n[2] Information about all teachers"
                  "\n[3] List of departments"
                  "\n[4] Teachers per group"
                  "\n[5] List of groups per department"
                  "\n[6] Department with maximum number of groups"
                  "\n[7] Department with smallest number of groups"
                  "\n[8] List of subjects per teacher")

            report_selected = int(input(">>> "))

            dict_of_reports = {
                1: f"SELECT * FROM `Groups`;",
                2: f"SELECT * FROM `Teachers`",
                3: "",
                4: "",
                5: "",
                6: "",
                7: "",
                8: "",
            }

            report_statement = dict_of_reports[report_selected]
            my_cursor.execute(report_statement)
            extracted_report = my_cursor.fetchall()
            print(f"CHECH - report: {extracted_report}")

            # extract columns
            field_names = [i[0] for i in my_cursor.description]
            print(f"CHECK - columns: {tuple(field_names)}")

            time.sleep(2)

            print("\nReport:")
            for record in extracted_report:
                print(str(record))

            choice = str(input("\nDo you want to save report? [Y/N]"
                               "\n>>> ")).lower()
            if choice == 'y':
                file = open("report_results.txt", "w+")
                file.write(f"{str(tuple(field_names))}\n")
                for row in extracted_report:
                    file.write(f"{str(row)}\n")
                file.close()

            else:
                go_on()

    except Exception as e:
        print(f"[6] Error: {e}")


# Submenu 7
def quit_program():
    try:
        try:  # to address instance where Quit invoked prior connecting to DB
            if test_connection():
                my_db.close()
                print(f"\n\tDatabase connection is closed.")
        except Exception:
            print("\n\t(No database was connected)")

        print("\n\t>>> Session terminated <<<")
        sys.exit()
    except Exception as e:
        print(f"[7] Error: {e}")


# go_on - invoke after each instruction being executed
def go_on():
    try:
        print('\nDo you want to continue? [Y/N]')
        selection = str(input('>>> ')).lower()
        if selection == 'n':
            quit_program()
        else:
            pass
    except Exception as e:
        print(f"Error: {e}")


# test_connection - invoke prior executing SQL statement, to address instance where DB not connected
def test_connection():
    try:
        test = my_db.is_connected()
        if test:
            return True
    except Exception:
        print("(There is no connection to database established)")


# extract_tables supports submenu 2,3
def extract_tables():
    global dict_of_tables
    dict_of_tables = {}
    key_index = 0
    try:
        if test_connection():
            my_cursor.execute(f"SHOW TABLES;")
            my_results = my_cursor.fetchall()

            # cleaning data
            char_to_remove = [",", "'", "(", ")"]
            for dirty_result in my_results:
                clean_result = ""
                for i in str(dirty_result):
                    if i in char_to_remove:
                        pass
                    else:
                        clean_result += i
                key_index += 1

                # add names to dictionary
                dict_of_tables[key_index] = clean_result
            print(f"CHECK - Extracted tables: {dict_of_tables}")
    except Exception as e:
        print(f"[2-3] Error (extract tables): {e}")


def extract_columns():
    global dict_of_columns
    global selected_table
    dict_of_columns = {}
    key_index = 0
    try:
        if test_connection():
            query = f"SELECT * FROM {selected_table};"
            print(f"CHECK - query: {query}")
            # after this point I have error in SQL syntax but ONLY for table Groups...
            # when replacing {selected_table} with a string 'Groups', error is gone...

            my_cursor.execute(query)
            field_names = [i[0] for i in my_cursor.description]

            # cleaning data
            char_to_remove = [",", "'", "(", ")"]
            for dirty_result in field_names:
                clean_result = ""
                for i in str(dirty_result):
                    if i in char_to_remove:
                        pass
                    else:
                        clean_result += i
                key_index += 1

                # add names to dictionary
                dict_of_columns[key_index] = clean_result

            print(f"CHECK - Extracted columns: {dict_of_columns}")
    except Exception as e:
        print(f"[2-3] Error (extract columns): {e}")


# invoke menu
menu()
