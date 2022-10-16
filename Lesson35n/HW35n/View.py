# View - presents data to user
# HTML, chart, table or text
# View should never call owm methods (called by Controller)

import Model


def index():
    print('\n\tHome page'
          '\n[1] Display all stock'
          '\n[2] Find stock'
          '\n[3] Add stock'
          '\n[4] Exit')


def display_page():
    print('\n\tAll items:')
    for SKU in Model.stock:
        print(SKU)

    Model.go_on()


def search_page():
    print('\n\tSearch page')
    Model.find_stock()
    Model.go_on()


def add_shoes_page():
    print('\n\tAdding SKU page')
    Model.add_stock()
    Model.go_on()


def terminate_session_page():
    print('\n\tSession terminated.')
    exit()


def error_message_page():
    print('\n\tError message')
