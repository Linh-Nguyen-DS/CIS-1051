#CIS 1051 Section 9
#Linh Nguyen

import random

def autoRollTo20():
    total = 0
    while total < 20:
        roll = random.randint(1,6)
        #print("Roll:", roll)
        if roll == 1:
            total = 0
            #print("Turn total:", total)
            return total
        else:
            total = total + roll
    #print("Turn total:", total)
    return total

def rollTo20Outcomes(numRuns):
    outcomes = {}
    for _ in range(numRuns):
        score = autoRollTo20()
        if score not in outcomes:
            outcomes[score] = 1
        else:
            outcomes[score] += 1
    return outcomes

ask = int(input("How many Hold-at-20 turn simulations? "))
outcomes = rollTo20Outcomes(ask)
print("Score\t Estimated Probability")
for score in sorted(outcomes):
    print(score, outcomes[score]/ask, sep='\t')
