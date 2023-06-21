import csv
import os
import sys
from pathlib import Path


class records:
    def __init__(self, option):
        self.option = option

        try:
            file = open(r"c:\Users\training.user\Downloads\flash.csv", "r") #opens file to use
        except FileNotFoundError:
            file = open(r"c:\Users\training.user\Downloads\flash.csv", "x") #opens anyway

        if option.lower() == "a":
            opt1 = str(input("Enter your name: "))
            opt2 = str(input("Whats your favourite sport? "))
            opt3 = str(input("What is your favourite colour? "))
            with open(r"c:\Users\training.user\Downloads\flash.csv", "a") as writerecord:
                writerecord.write(f"|\t{opt1}\t\t{opt2}\t\t\t{opt3}\n")            #add data to record

        elif option.lower() == "b":
            file = open(r"c:\Users\training.user\Downloads\flash.csv", "r")        #shows inside
            print(file.read())
            file.close()

        elif option.lower() == "c":
            print("Deleted content")
            file = open(r"c:\Users\training.user\Downloads\flash.csv", "r+")
            file.truncate(0)        #removes data at stated value

        csv_rowlist = [["#", "Name:", "Favourite Sport", "Favourite Colour" ], [1, opt1, opt2, opt3]]   #creates heading and data
        with open(r'c:\Users\training.user\Downloads\flash.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(csv_rowlist)
while True:
    print()
    print("Record management system")
    print()
    print("Pick an option:")
    print("a: add record")
    print("b: show record")
    print("c: delete record")
    print()

    option = input("Choose an option: a,b,c: ").upper()
    records(option)         #loop code
