import os
import sys
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
            print("Deleted content")
            file = open(r"c:\Users\training.user\Downloads\record.txt", "r+")
            file.truncate(0)        #removes data at stated value

while True:
    def createfile():
        with open(r"c:\Users\training.user\Downloads\record.txt", "w+") as create:
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
    print("c: delete record")
    print()

    option = input("Choose an option: a,b,c: ").upper()
    records(option)
