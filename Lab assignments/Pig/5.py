#CIS 1051 Section 2
#Linh Nguyen

import random

def holdAt20_Or_GoalGame():
    total = 0
    score = 0
    while total < 20 or score < 100:
        roll = random.randint(1,6)
        print("Roll:", roll)
        total = total + roll
        if roll == 1:
            total = 0
            print('Turn total:', total)
            print('New score:', score)
        elif total > 20:
            score = score + total
            print('Turn total:', total)
            print('New score:', score)
            
holdAt20_Or_GoalGame()
