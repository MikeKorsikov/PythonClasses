# dictionary of dictionaries
firm_dict = {
    'TEST': {
        'name': 'Testname',
        'surname': 'Testsurname',
        'phone_number': '000-000-000',
        'e-mail': 'name@domain',
        'position': 'Testposition',
        'room_number': '000',
        'skype': 'Testskype'
    }
}


def main_firma():
    choice = 0
    while choice != 5:
        print('\n\tMenu'
              '\n1. Add record'
              '\n2. Remove record'
              '\n3. Find record'
              '\n4. Update record'
              '\n5. Exit')
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


def add_record():
    details = ['name', 'surname', 'phone_number', 'e-mail', 'position', 'room_number', 'skype']
    record = {}
    for key in details:
        value = input(f'Enter {key} of the person: ')
        record[key] = value
    print(f'\nRecord {record["name"].upper()} added:')
    for key, value in record.items():
        print(f'{key}: {value}')

    # adding personal record (small dict) to dictionary of the firm (big dict)
    person = record["name"].upper()
    firm_dict[person] = record


def remove_record():
    choice = input('Enter name of the record to be removed: ')
    del firm_dict[choice.upper()]
    print('\nRecord removed')


def find_record():
    choice = input('Enter name of the record to be found: ')
    try:
        person = firm_dict.get(choice.upper())
        print('\nSearch results:')
        for key, value in person.items():
            print(f'{key}: {value}')
    except AttributeError:
        print('Record not found.')


def update_record():
    choice = input('Enter name of the record to be found: ')
    try:
        person = firm_dict.get(choice.upper())
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
    except AttributeError:
        print('Record not found.')


def exit_prog():
    print('\nSession terminated')


# invoking function
main_firma()
