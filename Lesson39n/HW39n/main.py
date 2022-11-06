# 2 threads, use event or barrier, lock
import os
import threading
from colorama import Fore
from colorama import Style

directory = 0
final_directory = 'target_folder/file3.txt'
given_word = ''
list_of_all_files = []
list_of_files_to_process = []
list_of_bad_words = []


def request_path():
    print("\n\tPHASE 1 - Collecting data:")
    # requesting source folder or path to be processed
    global directory
    directory = input('(a) Enter path where you want to run scan? ')
    print(f"Scan will be executed in thr following directory - "
          f"{Fore.BLUE}{directory}{Style.RESET_ALL}")


def request_word():
    global given_word
    given_word = input('\n(b) Enter word you want to find? ')
    print(f"Following word will be searched in the files of the given directory - "
          f"{Fore.BLUE}{given_word}{Style.RESET_ALL}")


def dumping_forbidden_words():
    try:
        # dump to memory list of words to be found
        file = open('list_of_words.txt', 'r')
        content = file.readlines()
        file.close()

        # normalise and convert to proper list
        global list_of_bad_words
        for word in content:
            list_of_bad_words.append(word.strip())
    except Exception as e:
        print(f"Error while processing files: {Fore.RED}{e}{Style.RESET_ALL}")


def process_directory():
    print("\n\tPHASE 2 - Processing directory:")
    global list_of_all_files
    try:
        # iterating through content of the given directory
        for filename in os.listdir(directory):
            base = os.path.basename(filename)
            list_of_all_files.append(base)

        # checking if there are any files and listing if any
        if len(list_of_all_files) > 0:
            print("Following files are identified in the given directory:")
            for file_name in list_of_all_files:
                print(file_name)

            print("Directory was successfully processed!\n")
        else:
            print("Directory is empty.")

    except Exception as e:
        print(f"Error processing directory: {Fore.RED}{e}{Style.RESET_ALL}")

    processing_files()


def processing_files():
    print("\n\tPHASE 3 - Processing files:")
    # iterate files from list_of_all_files
    count = 0
    for file_name in list_of_all_files:
        count += 1
        try:
            file = open(f"{directory}/{file_name}", 'r')
            content = file.read()
            file.close()
            print(f"Content of file-{count} is: {content.upper()}")

            # identify files containing given_word
            encounter = content.upper().count(given_word.upper())
            if encounter > 0:
                # add identified files to list_of_files_to_process
                list_of_files_to_process.append(file_name)
        except Exception as e:
            print(f"\n\tError processing file: {Fore.RED}{e}{Style.RESET_ALL}")
    if count > 0:
        print(f"Files containing word {Fore.BLUE}{given_word}{Style.RESET_ALL}: "
              f"{list_of_files_to_process}")
        print("Files successfully processed!")
    else:
        print("No files to process.")
    transfer_content()


def transfer_content():
    print("\n\tPHASE 4 - Transferring content:")
    # content of files in list_of_files_to_process dump into file3 (target)
    count = 0
    for file_name in list_of_files_to_process:
        count += 1
        try:
            file = open(f"{directory}/{file_name}", 'r')
            content = file.read()
            file.close()

            with open(final_directory, 'a') as f:
                f.write(f"{content}\n")

        except Exception as e:
            print(f"\n\tError transferring content: {Fore.RED}{e}{Style.RESET_ALL}")
    if count > 0:
        print("Content was successfully transferred!")
        read_final_content()
    else:
        print("There is no content to be transferred.")


def read_final_content():
    try:
        file = open(final_directory, 'r')
        final_content = file.read()
        file.close()
        print(f"Transferred/consolidated content is:"
              f"\n{Fore.BLUE}{final_content}{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n\tError reading content: {Fore.RED}{e}{Style.RESET_ALL}")


def censorship():
    print("\n\tPHASE 5 - Censoring content:")
    # open in 'w' mode file3 and find words from list_of_bad_words
    try:
        with open(final_directory, 'r') as f:
            if f.readable():
                lines = ' '.join(
                    list(filter(
                        lambda x: x.replace('\n', ' ') not in list_of_bad_words, ' '.join(
                            list(map(lambda x: x, f.readlines()))).split(" "))))

        with open(final_directory, 'w') as f2:
            if f2.writable():
                f2.writelines(lines)

        print(f"Censored content is: \n{Fore.BLUE}{lines}{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n\tError censoring content: {Fore.RED}{e}{Style.RESET_ALL}")


def main():
    try:
        print("\n\t*** WORD SCANNER ***")
        request_path()
        request_word()
        dumping_forbidden_words()

        th1 = threading.Thread(target=process_directory)
        th1.start()
        th1.join()

        th2 = threading.Thread(target=censorship)
        th2.start()
        th2.join()

    except KeyboardInterrupt:
        print("\n\nSession terminated.")


# initiate program
if __name__ == "__main__":
    main()
