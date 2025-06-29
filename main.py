import random
import art
from game_data import data

def compare(score):
    choice1=random.choice(data)
    choice2=random.choice(data)
    while choice1 == choice2:
        choice2 = random.choice(data)
    print("COMPARE:\n")
    print(f"{choice1['name']}, a {choice1['description']}, from {choice1['country']}")
    print(art.vs)
    print(f"{choice2['name']}, a {choice2['description']}, from {choice2['country']}")
    answer=input("Who has more followers?[ A/B ]").upper()
    if answer=='A'and choice1['follower_count']> choice2['follower_count']:
        score+=1
        print(f"You are correct:)\nYour Score is {score}\n")
        return score
    elif answer=='B'and choice2['follower_count']> choice1['follower_count']:
        score+=1
        print(f"You are correct:)\nYour Score is {score}\n")
        return score
    else:
        print("You Lose!!")
        print(f"Your Final score :{score}")
        return -1

print(art.logo)
# score=0
marks=0
cont="yes"
while cont=="yes":
    marks = 0
    game_over = False
    while not game_over:
        marks = compare(marks)
        if marks == -1:
            print("Game Over :(")
            game_over = True
    cont=input("Do you want to play again?Type[yes/no]").lower()
    if cont =="yes":
        print("\n"*20)
