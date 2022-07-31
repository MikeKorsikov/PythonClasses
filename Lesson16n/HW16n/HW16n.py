import sys
import json

details = ["name", "surname", "age"]

#  connect to db.txt
try:
    file = open('db.txt', 'r')
    file_str = file.read()
    main_dict = json.loads(file_str)
    file.close()

except Exception as e:
    print(str(e))


def start_menu():
    choice = 0
    while choice != 5:
        print('\n\tMenu'
              '\n1. Add record'
              '\n2. Remove record'
              '\n3. Find record'
              '\n4. Update record'
              '\n5. Exit'
              '\n6. *** New *** Save records'
              '\n7. *** New *** Display all records')
        choice = int(input('>>> '))

        match choice:
            case 1:
                add_record()
            case 2:
                remove_record()
            case 3:
                find_record()
            case 4:
                update_record()
            case 5:
                exit_prog()
            case 6:
                save_db()
            case 7:
                display_records()


def add_record():
    record = {}
    for key in details:
        value = input(f'Enter {key} of the person: ')
        record[key] = value
    print(f'\nRecord {record["name"].upper()} added:')
    for key, value in record.items():
        print(f'{key}: {value}')

    # adding personal record (small dict) to dictionary of the main (big dict)
    person = record["name"].upper()
    main_dict[person] = record

    # asking if user wants to continue
    go_on()


def remove_record():
    choice = input('Enter name of the record to be removed: ')
    del main_dict[choice.upper()]
    print('\nRecord removed')

    # asking if user wants to continue
    go_on()


def find_record():
    print('\nEnter option to search by: ')
    for val in details:
        print(f'{details.index(val)} - {val}')
    selection = int(input('>>>'))
    value = str(input('Enter criteria >>>')).lower()
    result_list = []

    match selection:
        case 0:
            for i in main_dict:
                if (main_dict[i]['name']).lower() == value:
                    result = f"{main_dict[i]['name']} - {main_dict[i]['surname']} - {main_dict[i]['age']}"
                    result_list.append(result)

        case 1:
            for i in main_dict:
                if (main_dict[i]['surname']).lower() == value:
                    result = f"{main_dict[i]['name']} - {main_dict[i]['surname']} - {main_dict[i]['age']}"
                    result_list.append(result)

        case 2:
            for i in main_dict:
                if (main_dict[i]['age']).lower() == value:
                    result = f"{main_dict[i]['name']} - {main_dict[i]['surname']} - {main_dict[i]['age']}"
                    result_list.append(result)

    if len(result_list) < 1:
        print('No records found.')
    else:
        print(f"\nRecords found: ")
        for i in result_list:
            print(i)


         # save result to temp file
    try:
        temp_file = open('temp.txt', 'w')
        temp_file.write(str(result_list))
        temp_file.close()
    except Exception as e:
        print(str(e))

    # asking if user wants to continue
    go_on()


def update_record():
    choice = input('Enter name of the record to be found: ')
    try:
        person = main_dict.get(choice.upper())
        keys = []
        for key, value in person.items():
            keys.append(key)
        print('\nWhich attribute you want to update? ')
        for key in keys:
            print(f'{keys.index(key)} - {key}')
        attr_sel = int(input('>>> '))
        upd_val = input(f'Enter new {keys[attr_sel]}: ')
        person.update({keys[attr_sel]: upd_val})
        print('\nRecord updated')

        # asking if user wants to continue
        go_on()
    except AttributeError:
        print('Record not found.')

        # asking if user wants to continue
        go_on()


def exit_prog():
    try:
        file = open('db.txt', 'w')
        main_dict_str = json.dumps(main_dict)
        file.write(main_dict_str)
        file.close()

    except Exception as e:
        print(str(e))
    print('\nSession terminated.')
    sys.exit()


def save_db():
    try:
        file = open('db.txt', 'w')
        main_dict_str = json.dumps(main_dict)
        file.write(main_dict_str)
        file.close()

    except Exception as e:
        print(str(e))
    print('\n Records saved.')
    # asking if user wants to continue
    go_on()


def display_records():
    print('\n\t\t\t *** List of records ***')
    for record in main_dict.items():
        for value in record:
            print(f'{value}')

    # asking if user wants to continue
    go_on()


def go_on():
    print('\nDo you want to continue? [Y/N]')
    selection = str(input('>>>')).lower()
    if selection == 'n':
        exit_prog()
    else:
        pass


# invoking function
start_menu()
