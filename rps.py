import random

print("Choose rock, paper or scissors")
decision = input().lower()

computer = random.randrange(0,2)
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
    else:
            print("The computer chose " + computer_str + ". \nYou won!")
elif (decision == "paper"):
    if (computer_str == "scissors"):
        print("The computer chose " + computer_str + ". \nYou lost.")
    else:
        print("The computer chose " + computer_str + ". \nYou won!")
elif (decision == "scissors"):
    if (computer_str == "rock"):
        print("The computer chose " + computer_str + ". \nYou lost.")
    else:
        print("The computer chose " + computer_str + ". \nYou won!")
else:
    print("That's not a valid item")