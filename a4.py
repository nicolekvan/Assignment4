# a4.py

# Nicole Kwan
# nkwan3@uci.edu
# 76647093

from ui import *
from menu import *

# /Users/nicolekwan/Workspace/journal.dsu

def main():
    try:
        print_menu()
        while True:
            commands = ["l", "q", "c", "d", "r", "o", "e", "p", "i"]
            user_input = input("\nEnter Command: ")
            command, *args = user_input.split()

            if command in commands:
                if command.lower() in ["e", "p", "i"]:
                    run_edits(command, args)
                else:
                    run(command, args)
            else:
                print("Invalid Command")
                continue

    except IndexError:
        print(f"Error: Improper amount of arguments.")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
