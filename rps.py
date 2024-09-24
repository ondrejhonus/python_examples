import random

computer = random.randrange(0,2)
p_points = 0
c_points = 0
play_more = 'y'

while play_more == 'y' or play_more == '':
    print("Choose rock, paper or scissors")
    decision = input().lower()
    if(computer == 0):
        computer_str = "rock"
    elif(computer == 1):
        computer_str = "paper"
    elif(computer == 2):
        computer_str = "scissors"

    if (decision == computer_str):
        print("The computer chose " + computer_str + ". \nIt's a Tie.")
    elif (decision == "rock"):
        if (computer_str == "paper"):
            print("The computer chose " + computer_str + ". \nYou lost.")
            c_points+=1
        else:
                print("The computer chose " + computer_str + ". \nYou won!")
                p_points+=1
    elif (decision == "paper"):
        if (computer_str == "scissors"):
            print("The computer chose " + computer_str + ". \nYou lost.")
            c_points+=1

        else:
            print("The computer chose " + computer_str + ". \nYou won!")
            p_points+=1

    elif (decision == "scissors"):
        if (computer_str == "rock"):
            print("The computer chose " + computer_str + ". \nYou lost.")
            c_points+=1

        else:
            print("The computer chose " + computer_str + ". \nYou won!")
            p_points+=1

    else:
        print("That's not a valid item")
    print(f"Computer: {c_points} You: {p_points}")
    play_more = input("Do you want to play again? [Y/n]")