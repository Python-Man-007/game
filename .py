import random  # importing random function for ai
list_moves = ["rock", "paper", "scissors"]  # list of moves

print("\nwelcome to rock, paper, scissors!".capitalize())  # welcome to the game
start = input("start or quit with (Y/Q) ".upper())

if start == "Y":  # starting
    for start in range(5):
        print("\nhuman's first")  # players code
        move = input("Rock, paper, scissors ")
        print("you have chosen", move)

        print("\nAI's turn!")  # AI's code
        print("AI has choose", random.choice(list_moves))

elif start == "Q":  # quiting / wrong spelling
    print("quiting".capitalize())
else:
    print("check spelling!".upper())