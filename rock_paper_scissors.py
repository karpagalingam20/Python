import random

emojies = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = ('r', 'p', 's')
system_selected = random.choice(choices)

while True:
    try:
        val = str(input("Enter your choices rock, papaer, scissors ? (r/p/s) : "))
        if val not in choices:
            print("Entered valid choice")
        elif val == system_selected:
            print(f"you selected : {emojies[val]}")
            print(f"system selected : {emojies[system_selected]}")
            print("You are win")
        else:
            print(f"you selected : {emojies[val]}")
            print(f"system selected : {emojies[system_selected]}")
            print("You are lose")
    except ValueError:
        print("Enter valid choice ")
