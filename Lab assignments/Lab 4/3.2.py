#CIS1051
#Section009
#LinhNguyen

def slash(n):
    x = 4 * (n - 1) + 2
    print("!" * x)
    for i in range(1, n):
        x -= 4
        print("\\" * (2 * i), "!" * x, "/" * (2 * i), sep="")

slash(4)
