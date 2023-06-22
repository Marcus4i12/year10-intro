import os
from pathlib import Path

class colour:
    RED = '\033[31m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class Records:
    def __init__(self, file):
        self.file = file

    def add_record(self, opt1, opt2, opt3):                 # option = B
        with open(self.file, "a") as writerecord:
            writerecord.write(f"|\t{opt1}\t\t{opt2}\t\t\t{opt3}\n")

    def show_records(self):                     # option = B
        with open(self.file, "r") as f:
            print(f.read())

    def remove_line(self, line_number):         # option = C
        with open(self.file, "r") as f:
            lines = f.readlines()
        with open(self.file, "w") as f:
            for i in range(len(lines)):
                if i != line_number:
                    f.write(lines[i])

    def delete_all_records(self):               # option = D
        with open(self.file, "r+") as f:
            f.truncate(46)

def record_manager():
    file_path = Path(r"c:\Users\training.user\Downloads\record.txt")
    records = Records(file_path)

    while True:
        print()
        print(f"{colour.BOLD}-Record management system-{colour.RESET}")
        print()
        print("Select an option:")
        print("A | Add record")
        print("B | Show record")
        print("C | Remove a record")
        print("D | Delete all records")
        print()

        option = input("Choose an option: A | B | C | D : ").upper()

        print()

        def createfile():
            with open(r"c:\Users\training.user\Downloads\record.txt", "w+") as create:          #create headline at top when file made
                create.write("|\tName:\t\tFavourite Sport:\t\tFavourite Colour:\n")
        if Path(r"c:\Users\training.user\Downloads\record.txt"):
            if os.stat(r"c:\Users\training.user\Downloads\record.txt").st_size != 0:
                with open(r"c:\Users\training.user\Downloads\record.txt", "r+") as readfirstline:
                    first = readfirstline.readlines()[0][0]
                    if first != "|":
                        readfirstline.write("|\t\t\tName:\t\tFavourite Sport:\t\tFavourite Colour:\n")
            else:
                createfile()
        else:
            createfile()
        if option.upper() == "A":
            name = input("Enter your name: ")
            sport = input("What's your favourite sport? ")
            color = input("What is your favourite colour? ")
            records.add_record(name, sport, color)

        elif option.upper() == "B":
            records.show_records()

        elif option.upper() == "C":
            line_number = int(input("Enter the line number to delete: "))
            records.remove_line(line_number)
            print(f"{colour.RED}Removed record{colour.RESET}")

        elif option.upper() == "D":
            print(f"{colour.RED}Deleted all records{colour.RESET}")
            records.delete_all_records()
        
        else:
            print(f"{colour.RED}Invalid input{colour.RESET}")

if __name__ == "__main__":                  # Loop code
    record_manager()