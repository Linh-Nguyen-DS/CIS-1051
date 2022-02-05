#CIS 1051 Section 9
#Linh Nguyen

import random

def holdAt20_Or_GoalTurn():
    score = int(input("Score? "))
    turntotal = 0
    while True:
        roll = random.randint(1,6)
        print("Roll:", roll)
        score += roll
        turntotal += roll

        if score >= 100 or turntotal >= 20:
            break

    print("Turn total:", turntotal)
    print("New score:", score)

holdAt20_Or_GoalTurn()
