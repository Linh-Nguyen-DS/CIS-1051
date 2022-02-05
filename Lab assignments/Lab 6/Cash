#CIS 1051
#Section 009
#Linh Nguyen

userput = input("Enter how much change is owed: ")

def isfloat(userput):
    try:
        float(userput)
    except ValueError:
        return False
    else:
        return True

    try:
        int(userput)
    except ValueError:
        return False
    else:
        return True

isfloat(userput)

while isfloat(userput) == False or float(userput) < 0:
    print("Please re-input ")
    userput = input("Enter how much change is owed: ")
    isfloat(userput)

while isfloat(userput) == True:
    change = round(float(userput) * 100)
    coin = 0
    set = [25, 10, 5, 1]
    for i in set:
        coin += change // i
        change %= i
    print(coin)
    break;
