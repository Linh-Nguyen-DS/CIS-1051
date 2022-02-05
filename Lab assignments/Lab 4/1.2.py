#CIS1051
#Section009
#LinhNguyen

n = int(input("Enter your multiplication table: "))

def tables():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i*j, "\t", end= ' ')
        print()

tables()
