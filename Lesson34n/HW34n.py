# HW on Command Pattern (behavioural design pattern)

import os

verbose = True


# CLASSES SECTION
class CreateFile:
    def __init__(self, path, txt='File content.\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print(f"[Creating file '{self.path}']")
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        try:
            delete_file(self.path)
        except:
            print('Delete action not successfully...'
                  '\n... file was already deleted.')


class ReadFile:
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print(f"[Reading file '{self.path}']")
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')


class RenameFile:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        if verbose:
            print(f"[Renaming '{self.src}' to '{self.dest}']")
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print(f"[Renaming '{self.dest}' back to '{self.src}']")
        os.rename(self.dest, self.src)


# FUNCTIONS SECTIONS
def delete_file(path):
    if verbose:
        print(f"Deleting file: {path}")
    os.remove(path)


def Undo():
    answer = input('Reverse the executed commands? [y/n] ')
    if answer not in 'yY':
        print(f"Current file remained named as {new_name}.")

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass


def ExitMenu():
    print('\nSession terminated.')
    exit()


def main():
    global orig_name, new_name, commands
    orig_name = ""
    new_name = ""

    commands = []
    df = delete_file
    commands.append(df)

    choice = 0
    while choice != 6:
        print('\n\tMenu:'
              '\n[1] Create new file'
              '\n[2] Read file'
              '\n[3] Rename file'
              '\n[4] Undo all'
              '\n[5] Exit')
        choice = int(input(f'\nPlease enter option from the menu: '))
        match choice:
            case 1:
                orig_name = str(input('Enter name of the file: '))
                cf = CreateFile(orig_name)
                cf.execute()
                commands.append(cf)

            case 2:
                try:
                    if orig_name != "":
                        rf = ReadFile(orig_name)
                        rf.execute()
                        commands.append(rf)
                    else:
                        print('No file to read...')
                except Exception:
                    print('No file to read...')

            case 3:
                try:
                    if orig_name != "":
                        new_name = str(input('Enter new name of the file: '))
                        rnf = RenameFile(orig_name, new_name)
                        rnf.execute()
                        commands.append(rnf)
                    else:
                        print('No file to rename...')
                except Exception:
                    print('No file to rename...')
            case 4:
                Undo()

            case 5:
                ExitMenu()


# INVOKE
if __name__ == "__main__":
    main()
