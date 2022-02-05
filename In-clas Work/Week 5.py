#CIS 1051
#Linh Nguyen

#Check whether it is a leap year

def isLeapYear(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

entry = input("Please enter a date in MM/DD/YYYY format: ")

month = int(entry[:2])
day   = int(entry[3:5])
year  = int(entry[6:])

if month in [4,6,9,11]:
    if 1 <= day <= 30:
        print("day is valid")
    else:
        print("day is invalid")
        
elif month in [1,3,5,7,8,10,12]:
    if 1 <= day <= 31:
        print("day is valid")
    else:
        print("day is invalid")
        
elif month == 2:
    if 1 <= day <= 28:
        print("day is valid")
    elif day == 29 and isLeapYear(year):
        print("day is valid")
    elif day == 29 and not isLeapYear(year):
        print("year is not leap year")
    else:
        print("day is invalid")

else:
    print("Invalid month")

print(isLeapYear(2016))

print(isLeapYear(2015))

print(isLeapYear(2000))

print(isLeapYear(1900))
