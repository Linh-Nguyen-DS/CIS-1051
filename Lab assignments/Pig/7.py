#CIS 1051 Section 9
#Linh Nguyen

import random

def twoPlayerPig():
    turnCount = 0
    playerOneScore = 0
    playerTwoScore = 0
    print("Player 1 score: 0")
    print("Player 2 score: 0")
    while playerOneScore < 100 and playerTwoScore < 100:
        dice = 0
        playerOneTotal = 0
        playerTwoTotal = 0
        print("It is player 1's turn")
        while dice != 1 and playerOneTotal < 20:
            dice = random.randint(1,6)
            print("Roll:", dice)
            if dice != 1:
                playerOneTotal += dice
            else:
                total = 0
                break
        print("Player 1 turn total:", playerOneTotal)
        playerOneScore += playerOneTotal
        print("Player 1 score total:", playerOneScore)
        dice = 0
        print("It is player 2's turn")
        while dice != 1 and playerTwoTotal < 20:
            dice = random.randint(1,6)
            print("Roll:", dice)
            if dice != 1:
                playerTwoTotal += dice
            else:
                playerTwoTotal = 0
                break
        print("Player 2 turn total:", playerTwoTotal)
        playerTwoScore += playerTwoTotal
        print("Player 2 score total:", playerTwoScore)

twoPlayerPig()
