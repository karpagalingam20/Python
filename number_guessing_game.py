import random

number = random.randint(1, 100)

while True:
    try:
        val = int(input("Enter the number between 1 to 100 : "))
        if val > number:
            print("Entered number is too high")
        elif val < number:
            print("Entered number is too low")
        else:
            print("Thank you for the guessing number")
    except ValueError:
        print("Enter valid number")
