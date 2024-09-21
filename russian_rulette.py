import random
import time

input("Press enter to spin the chamber")
chambered = random.randrange(1,6)
for i in range(chambered * 2):
    input("It's your turn, press enter to shoot")
    if(i == chambered):
        print("You lost!")
        break
    else:
        print("You didn't get shot")
    i+=1
    if(i+1 == chambered):
        print("It's the computers turn.")
        time.sleep(3)
        print("The computer lost")
        break
    else:
        print("It's the computers turn.")
        time.sleep(3)
        print("The computer didn't get shot")