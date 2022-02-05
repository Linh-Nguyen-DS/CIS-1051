#CIS1051
#Section009
#LinhNguyen

#Upper
def top(n):
    print('|""""""""""|')
    x = n
    for i in range(n):
        print(" " * (i + 1), "\\", ":" * x, "/", " " * (i + 1), sep="")
        x -= 2
        if x == 0:
            print(" " * n, "||", " " * n)

top(10)

#Lower
def bot(n):
    x = 2
    for i in range(n, 0, -1):
        print(" " * i, "/", ":" * x, "\\", " " * i, sep="")
        x += 2
    print('|""""""""""|')

bot(10)
