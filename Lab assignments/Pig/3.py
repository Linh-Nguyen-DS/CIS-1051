import random

n = int(input("Hold at: "))
def autoRollTo100(n):
    total = 0
    while total < n:
        roll = random.randint(1,6)
        #print("Roll:", roll)
        if roll == 1:
            total = 0
            #print("Turn total:", total)
        else:
            total = total + roll
    #print("Turn total:", total)
    return total

print(autoRollTo100(n)/n)
