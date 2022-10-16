# Controller accepts user's input
# It delegates data representation to View
# It delegates data handling to Model


import View, Model


def main():
    Model.retrieve_data()
    answer = 0
    while answer != 4:
        View.index()
        answer = int(input('>>> '))
        match answer:
            case 1:
                View.display_page()
            case 2:
                View.search_page()
            case 3:
                View.add_shoes_page()
            case 4:
                View.terminate_session_page()


if __name__ == '__main__':
    main()
