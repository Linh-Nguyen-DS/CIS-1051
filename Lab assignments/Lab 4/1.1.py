#CIS1051
#Section009
#LinhNguyen

b = int(input("How many bottles of beer on the wall? "))

def bottles():
    for i in range(b, 0, -1):
        print(i, "bottles of beer on the wall,", i, "bottles of beer")
        print("Take one down, pass it around,", i - 1, "bottles of beer on the wall\n")
        
bottles()
