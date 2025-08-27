import random

while True:
    val = input("Roll your dice?: (y/n) :").lower()
    if val == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'You rolled ({die1}, {die2}) ')
    elif val == 'n':
        print("Thank you for playing")
        break
    else:
        print("Invalid choice")
