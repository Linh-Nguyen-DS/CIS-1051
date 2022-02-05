#CIS 1051 Section 9
#Linh Nguyen

import random

def autoRollTo20():
    total = 0
    while total < 20:
        roll = random.randint(1,6)
        print("Roll:", roll)
        if roll == 1:
            total = 0
            print("Turn total:", total)
            return total
        else:
            total = total + roll
    print("Turn total:", total)
    return total

autoRollTo20()
