#CIS1051
#Section009
#LinhNguyen

n = int(input("How many summation of squares? "))

def sum():
    sum = 0
    for i in range(1, n+1, 1):
        sum = sum + i**2
        print(sum)

sum()
