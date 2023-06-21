import os
from pathlib import Path

class records:
    def __init__(self, option):
        self.option = option

        try:
            file = open(r"c:\Users\training.user\Downloads\record.txt", "r") #opens file to use
        except FileNotFoundError:
            file = open(r"c:\Users\training.user\Downloads\record.txt", "x") #opens anyway

        if option.lower() == "a":
                opt1 = str(input("Enter your name: "))
                opt2 = str(input("Whats your favourite sport? "))
                opt3 = str(input("What is your favourite colour? "))
                with open(r"c:\Users\training.user\Downloads\record.txt", "a") as writerecord:
                    writerecord.write(f"|\t{opt1}\t\t{opt2}\t\t\t{opt3}\n")            #add data to record

        elif option.lower() == "b":
            file = open(r"c:\Users\training.user\Downloads\record.txt", "r")        #shows inside
            print(file.read())
            file.close()

        elif option.lower() == "c":
            def delete_line(file_name, line_number):
                with open(file_name, "r") as f:
                    lines = f.readlines()
                with open(file_name, "w") as f:
                    for i in range(len(lines)):
                        if i != line_number:
                            f.write(lines[i])
            if __name__ == "__main__":
                file_name = r"c:\Users\training.user\Downloads\record.txt"
                line_number = int(input("Enter the line number to delete: "))
                delete_line(file_name, line_number)

        elif option.lower() == "d":
            print("Deleted content")
            file = open(r"c:\Users\training.user\Downloads\record.txt", "r+")
            file.truncate(0)        #removes data at stated value

while True:
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

    print()
    print("Record management system")
    print()
    print("Pick an option:")
    print("a: add record")
    print("b: show record")
    print("c: remove a record")
    print("d: delete all records")
    print()

    option = input("Choose an option: a,b,c,d: ").upper()
    records(option)         #loop code
