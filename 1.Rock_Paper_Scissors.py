import random
import json

player1_name = ""
player2_name = "Computer User"

player1_score = 0
player2_score = 0

def user_choice():
    print("\n Enter your choice(1, 2, 3): ",end="")
    choice = int(input())
    while choice > 3 or choice <1:
      choice=int(input("\n Sorry!!! Enter a valid choice please."))
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"
    return choice_name

def determine_winner(user1, user2):
    if user1 == "Rock":
        if user2 == "Scissors":
            return "user1"
        elif user2 == "Paper":
            return "user2"

    elif user1 == "Paper":
        if user2 == "Rock":
            return "user1"
        elif user2 == "Scissors":
            return "user2"

    elif user1 == "Scissors":
        if user2 == "Paper":
            return "user1"
        elif user2 == "Rock":
            return "user2"

    return "Draw"

def file_edit():
    with open("data.json", "r") as f:
        d = json.load(f)
    fps = d["player_score"]

    if player1_score > player2_score:
        if player1_score > fps:
            d["player_name"] = player1_name
            d["player_score"] = player1_score
            with open("data.json", "w") as f:
                json.dump(d, f)

    elif player2_score > player1_score:
        if player2_score > fps:
            d["player_name"] = player2_name
            d["player_score"] = player2_score
            with open("data.json", "w") as f:
                json.dump(d, f)

    else:
        if player1_score > fps and player1_score > fps:
            d["player_name"] = player1_name
            d["player_score"] = player1_score
            with open("data.json", "w") as f:
                json.dump(d, f)
    f.close()

if __name__ == "__main__":
    print("\n Winning rules of the game ROCK PAPER SCISSORS are:\n"
          + " Rock vs Paper -> Paper wins \n"
          + " Rock vs Scissors -> Rock wins \n"
          + " Paper vs Scissors -> Scissor wins \n")

    with open("data.json", "r") as f:
        d = json.load(f)
    print("\n The highest score of the game is:",d["player_score"],"\n")
    f.close()

    print("\n USER-1:")
    player1_name = str(input(" Enter player-1 name: "))

    play = True
    while play == True:
        print("\n Enter the choice as:\n 1 for Rock\n 2 for Paper\n 3 for Scissors")
        
        user1 = user_choice()

        lst = ["Rock", "Paper", "Scissors"]
        user2 = random.choice(lst)
        
        print("\n Player choice is:",user1)
        print("\n Computer choice is:",user2)

        winner = determine_winner(user1, user2)

        if winner == "user1":
            player1_score += 10
            print("\n The winner of this game is:",player1_name)
        elif winner == "user2":
            player2_score += 10
            print("\n The winner of this game is:",player2_name)
        else:
            print("\n The match is drawn.")
        
        ans = input("\n Do you want to play again? (Y/N): ")
        if ans == 'Y' or ans == 'y':
            play = True
        else:
            break

    if player1_score > player2_score:
        print("\n The winner of the series is: ",player1_name)
    elif player2_score > player1_score:
        print("\n The winner of the series is: ",player2_name)
    else:
        print("\n The series is drawn.")
    file_edit()
