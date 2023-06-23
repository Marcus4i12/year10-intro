import os
from pathlib import Path

class colour:
    """colours for ui"""

    RED = '\033[31m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class Records:
    """manages commands for options"""

    def __init__(self, file):
        """start up"""
        self.file = file

    def add_record(self, opt1, opt2, opt3):                 # option = A
        """format for data when writen"""
        with open(self.file, "a") as writerecord:
            writerecord.write(f"|\t{opt1}\t\t{opt2}\t\t\t{opt3}\n")

    def show_records(self):                     # option = B
        """reads what is on file"""
        with open(self.file, "r") as f:
            print(f.read())

    def remove_line(self, line_number):         # option = C
        """reads and writes all lines, whateven line is stated is skipped"""
        with open(self.file, "r") as f:
            lines = f.readlines()
        with open(self.file, "w") as f:
            for i in range(len(lines)):
                if i != line_number:
                    f.write(lines[i])

    def delete_all_records(self):               # option = D
        """clears data untill heading"""
        with open(self.file, "r+") as f:
            f.truncate(46)


def record_manager():
    """"holds commands of options and print statements"""

    file_path = os.path.join("record.txt")
    records = Records(file_path)

    while True:
        print()
        print(f"{colour.BOLD}-Record management system-{colour.RESET}")
        print()
        print(f"{colour.RED}A{colour.RESET} | Add a record")
        print(f"{colour.RED}B{colour.RESET} | Show all records")
        print(f"{colour.RED}C{colour.RESET} | Remove a record")
        print(f"{colour.RED}D{colour.RESET} | Delete all records")
        print(f"{colour.RED}E{colour.RESET} | Exit")
        print()

        option = input(f"Choose an option: {colour.RED}A{colour.RESET} | {colour.RED}B{colour.RESET} | {colour.RED}C{colour.RESET} | {colour.RED}D{colour.RESET} | {colour.RED}E{colour.RESET}: ").upper()

        print()

        try:
            with open(file_path, "r") as f: #opens file to use
                pass
        except FileNotFoundError:
            with open(file_path, "x") as f: #opens anyway
                pass

        def create_file():
            """creating heading when file is opened"""
            with open(file_path, "w+") as create:          #create headline at top when file made
                create.write("|\tName:\t\tFavourite Sport:\t\tFavourite Colour:\n")
        if Path(file_path):
            if os.stat(file_path).st_size != 0:
                with open(file_path, "r+") as readfirstline:
                    first = readfirstline.readlines()[0][0]
                    if first != "|":
                        readfirstline.write("|\t\t\tName:\t\tFavourite Sport:\t\tFavourite Colour:\n")
            else:
                create_file()
        else:
            create_file()

        if option.upper() == "A":
            name = input("What is your name?  ")
            sport = input("What is your favourite sport? ")
            color = input("What is your favourite colour? ")
            records.add_record(name, sport, color)

        elif option.upper() == "B":
            print(f"{colour.RED}Showing records{colour.RESET}\n")
            records.show_records()

        elif option.upper() == "C":
            line_number = int(input("Enter the line number to delete: "))
            records.remove_line(line_number)
            print(f"\n{colour.RED}Removed record{colour.RESET}")

        elif option.upper() == "D":
            print(f"{colour.RED}Deleted all records{colour.RESET}")
            records.delete_all_records()

        elif option == "E":
            print(f"{colour.BOLD}Goodbye!{colour.RESET}")
            print()
            break
        
        else:
            print(f"{colour.RED}Invalid input{colour.RESET}")

if __name__ == "__main__":                  # Loop code
    record_manager()