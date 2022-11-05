# 2 threads, use event or barrier, lock
import os
import sys
import threading
from colorama import Fore
from colorama import Style

directory = 0
list_of_files = []


def process_files():
    try:
        # dump to memory list of words to be found
        file = open('list_of_words.txt', 'r')
        content = file.readlines()
        file.close()

        # normalise and convert to proper list
        list_of_words = []
        for word in content:
            list_of_words.append(word.strip())
    except Exception as e:
        print(f"Error while processing files: {Fore.RED}{e}{Style.RESET_ALL}")


def request_path():
    # requesting source folder or path to be processed
    global directory
    directory = input('\nEnter path where you want to run scan? ')
    print(f"\nScan will be executed in thr following directory - "
          f"{Fore.BLUE}{directory}{Style.RESET_ALL}")


def process_directory():
    global list_of_files
    try:
        # iterating through content of the given directory
        for filename in os.listdir(directory):
            base = os.path.basename(filename)
            list_of_files.append(base)

        # checking if there are any files and listing if any
        if len(list_of_files) > 0:
            print("\nFollowing files are identified:")
            for file_name in list_of_files:
                print(file_name)
        else:
            print("\nDirectory is empty.")

    except Exception as e:
        print(f"\n\tError processing directory: {Fore.RED}{e}{Style.RESET_ALL}")


def main():
    try:
        print("\n\t*** WORD SCANNER ***")
        process_files()
        request_path()
        th1 = threading.Thread(target=process_directory)
        th1.start()
        th1.join()
    except KeyboardInterrupt as e:
        print("\n\nSession terminated.")


# initiate program
if __name__ == "__main__":
    main()
