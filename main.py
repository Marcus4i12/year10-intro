from random import randint
x = randint(1, 100)
number = int(input("pick a number 1-100 "))
tries = 1
while (x!=number):
    if x > number:
        print("bigger")
        number = int(input("try again "))
    elif x < number:
        print("smaller")
        number = int(input("try again "))
    tries = tries + 1
print(tries, " attempts")