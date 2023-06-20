from random import randint
x = randint(1, 100)
tries = 1
number = "x"
while (x!=number):
    try:
        number = int(input("pick a number 1-100 "))
        if x == number:
            print("Correct")
        elif x < number:
            print("smaller")
        elif x > number:
            print("Bigger")
    except ValueError:
        print("Invalid input")
    tries = tries + 1
print(tries, " attempts")
