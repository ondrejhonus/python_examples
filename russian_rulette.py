import random
import time

input("Press enter to spin the chamber")
chambered = random.randrange(1,6)
p_points = 0
c_points = 0
play_more = 'y'
while play_more == 'y' or play_more == '':
    for i in range(chambered * 2):
        input("It's your turn, press enter to shoot")
        if(i == chambered):
            print("You lost!")
            c_points+=1
            break
        else:
            print("You didn't get shot")
        i+=1
        if(i+1 == chambered):
            print("It's the computers turn.")
            time.sleep(3)
            print("The computer lost")
            p_points+=1
            break
        else:
            print("It's the computers turn.")
            time.sleep(3)
            print("The computer didn't get shot")
    print(f"Computer: {c_points} You: {p_points}")
    play_more = input("Do you want to play again?")