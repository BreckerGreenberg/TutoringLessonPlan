import random

# Make it so a player can quit between games
# Implement score

playing = True
score = 0

while(playing):
    user_input = int((input("Enter a number between 0 and 4:")))

    random_number = random.randint(0, 5)

    if (user_input == random_number):
        print("Thats the ticket!")
    else:
        print("Maybe this isn't for you..")

    print("\nEnter X to quit.")

