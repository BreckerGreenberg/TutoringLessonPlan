import random

# Make it so a player can quit between games
# Implement score

playing = True
score = 0

while(playing):
    user_input = input("Enter a number between 0 and 4:")

    if user_input=="x":
        break

    random_number = random.randint(0, 5)

    if (int(user_input) == random_number):
        score= score + 1
        print("gorlock likes mcyds")
    else:
        print("nonono beta..")

    print("\nEnter X to quit.")
    print (score)