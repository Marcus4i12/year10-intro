print()
print("Record management system")
print()
print("Pick an option:")
print("a: add record")
print("b: show record")
print("c: delete record")
print()
option = str(input("Choose an option: a,b,c: "))

try:
    file = open(r"c:\Users\training.user\Downloads\record.txt", "r")
except FileNotFoundError:
    file = open(r"c:\Users\training.user\Downloads\record.txt", "x")

if option.lower() == "a":
    opt1 = str(input("Enter your name: "))
    opt2 = str(input("Whats your favourite sport? "))
    opt3 = str(input("What is your favourite colour? "))
    with open(r"c:\Users\training.user\Downloads\record.txt", "a") as writerecord:
        writerecord.write(f"{opt1}      {opt2}      {opt3}  |   ")            #add data to record

elif option.lower() == "b":
    file = open(r"c:\Users\training.user\Downloads\record.txt", "r")        #shows inside
    print(file.read())
    file.close()

elif option.lower() == "c":
    print("Deleted content")
    file = open(r"c:\Users\training.user\Downloads\record.txt", "r+")
    file.truncate(0)        #removes data untill stated value
