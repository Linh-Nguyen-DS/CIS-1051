#CIS 1051 Section 9
#Linh Nguyen

import random

def game():
    turnCount = 0
    playerOneScore = 0
    playerTwoScore = 0
    print("Player 1 score: 0")
    print("Player 2 score: 0")
    
    pick = random.randint(1,2)

    if pick == 1:
        print("You will be player 1.")
        while playerOneScore < 100 and playerTwoScore < 100:
            if playerOneScore >= 100 or playerTwoScore >= 100:
                break
            dice = 0
            playerOneTotal = 0
            playerTwoTotal = 0
            
            #YOU
            print("It is player 1's turn")
            ask = input("Enter nothing to roll; enter anything to hold. ")

            while ask == "":
                dice = random.randint(1,6)
                print("Roll:", dice)
                if dice != 1 and playerOneTotal < 20:
                    ask = input("Enter nothing to roll; enter anything to hold. ")
                    playerOneTotal += dice
                else:
                    playerOneTotal = 0
                    break
            print("Turn total:", playerOneTotal)
            playerOneScore += playerOneTotal
            print("New score:", playerOneScore)

            #COMPUTER
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
            print("Turn total:", playerTwoTotal)
            playerTwoScore += playerTwoTotal
            print("New score:", playerTwoScore)

    else:
        print("You will be player 2.")
        while playerOneScore < 100 and playerTwoScore < 100:
            if playerOneScore >= 100 or playerTwoScore >= 100:
                break
            dice = 0
            playerOneTotal = 0
            playerTwoTotal = 0
            #YOU
            print("It is player 1's turn")
            while dice != 1 and playerOneTotal < 20:
                dice = random.randint(1,6)
                print("Roll:", dice)
                if dice != 1:
                    playerOneTotal += dice
                else:
                    playerOneTotal = 0
                    break
            print("Turn total:", playerOneTotal)
            playerOneScore += playerOneTotal
            print("New score:", playerOneScore)

            #COMPUTER
            dice = 0
            print("It is player 2's turn")
            ask = input("Enter nothing to roll; enter anything to hold. ")

            while ask == "":
                dice = random.randint(1,6)
                print("Roll:", dice)
                if dice != 1 and playerTwoTotal < 20:
                    ask = input("Enter nothing to roll; enter anything to hold. ")
                    playerTwoTotal += dice
                else:
                    playerTwoTotal = 0
                    break
            print("Turn total:", playerTwoTotal)
            playerTwoScore += playerTwoTotal
            print("New score:", playerTwoScore)

game()
