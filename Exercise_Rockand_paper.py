import random
game_start = True

player_input = int(input("Rock(1)\n Paper(2)\n scissor(3)\n"))
Ai = random.randint(1,3)
if player_input == Ai:
    print("Choice Ai: ",Ai)
    print("let's go again ;)")
elif player_input != Ai:
    print(Ai)
    if (player_input == 1 and Ai == 2) or (player_input == 2 and Ai == 3) or (player_input == 3 and Ai ==1):
        print("Too bad, Try again Next time loser 3>")
    else:
        print("you win!")

