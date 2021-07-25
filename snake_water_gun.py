import random
l = ['s','w','g']

chance = 5
no_of_chance = 0
p_score = 0
c_score = 0

print("\t \t \tSnake Water Gun Game \n")
print("s for snake\n w for water\n g for gun\n")

while no_of_chance < chance:
    print("Player enter your input.")
    play = input("Snake, Water, Gun: ")
    comp = random.choice(l)

#When there's a tie
    if play == comp:
        print("It's a tie.")

#When user enter Snake
    elif play =='s' and comp =='g':
        c_score +=1
        print(f"Player choice was {play} and machine choice was {comp}.")
        print("The machine wins and gets 1 points.")
        print(f"The machine points is {c_score} and player score is {p_score}.")
        print()
    elif play == 's' and comp == 'w':
        p_score += 1
        print(f"Player choice was {play} and machine choice was {comp}.")
        print("The player wins and gets 1 points.")
        print(f"The machine points is {c_score} and player score is {p_score}.")
        print()

    #When user enter Water
    elif play == 'w' and comp == 'g':
        p_score += 1
        print(f"Player choice was {play} and machine choice was {comp}.")
        print("The player wins and gets 1 points.")
        print(f"The machine points is {c_score} and player score is {p_score}.")
        print()
    elif play =='w' and comp =='s':
        c_score += 1
        print(f"Player choice was {play} and machine choice was {comp}.")
        print("The machine wins and gets 1 points.")
        print(f"The machine points is {c_score} and player score is {p_score}.")
        print()

    #When player enter Gun
    elif play =='g' and comp =='w':
        c_score +=1
        print(f"Player choice was {play} and machine choice was {comp}.")
        print("The machine wins and gets 1 points.")
        print(f"The machine points is {c_score} and player score is {p_score}.")
        print()
    elif play =='g' and comp =='s':
        p_score +=1
        print(f"Player choice was {play} and machine choice was {comp}.")
        print("The machine wins and gets 1 points.")
        print(f"The machine points is {c_score} and player socer is {p_score}.")
        print()

    else:
        print("Wrong Input. \n")

    no_of_chance += 1
    print(f"{chance - no_of_chance} is left out of {chance}.\n")
print("\t \t \t Game Over")

if c_score == p_score:
    print("It's a tie and nobody wins.")

elif c_score > p_score:
    print("The machine wins.")

elif c_score < p_score:
    print("The player wins.")
print(f"Your point is {p_score} and machine points is {c_score}")