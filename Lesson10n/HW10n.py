# two related lists, enable sorting by ID and by phone number

phone_numbers = ['777-888-999',
                 '555-444-333',
                 '111-555-333',
                 '444-999-000',
                 '999-000-999',
                 '222-222-222',
                 '333-777-111']

list_of_id = ['001',
              '002',
              '003',
              '004',
              '005',
              '006',
              '007']


def sorting_PH_ID():
    zipped_lists_BP = zip(phone_numbers, list_of_id)
    zipped_lists_BID = zip(list_of_id, phone_numbers)

    sorted_list_BP = sorted(zipped_lists_BP)
    sorted_list_BID = sorted(zipped_lists_BID)

    print('How do you want to sort? By phone [P] or by ID [I]? ')
    choice = input('>>> ')

    if choice.lower() == 'p':
        for i in sorted_list_BP:
            print(i, end='\n')

    elif choice.lower() == 'i':
        for i in sorted_list_BID:
            print(i, end='\n')

    else:
        print('Wrong input. Try again with [P] or [I].')


sorting_PH_ID()
