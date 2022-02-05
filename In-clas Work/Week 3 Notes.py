for value in range(10)
    print("Printing:")
    print(value)
    print("done with this value\n") # create new  line

for value in range(5,10) # 5 - 9

for value in range(5,100,5) # from 5 up to but not include 100 and hơn kém nhau 5 đơn vị

word = "hello"

for letter in word:
    print(letter) # print each letter in each line

for value in range(100,90,-1):
    print(value) # 100 - 91 not include 90

#reversed(range(value))

import math

print(math.pi/4)
print(math.e)

total = 0
for i in range(5):
    print("total is", total, "\t i is", i, end="") # \t tab seperation
    total = total + i
    print("\t after adding, total is ", total)
print(total)

import math

print("target:\t", math.pi/4)

total = 0
iterations = 5 #how many times this runs, how many term you wanna add
sign = 1

# 1 -2 +3 -4 +5...
for value in range(1, iterations+1):
    print(value, sign, sign*value, sep="\t") # sep="\t" tab after each output
    total = total + sign*value
    sign = -1 * sign
print(total)

print("i", "1+2i", "sign", "sign*value", sep='\t')
for i in range(iterations):
    value = 1/(1 + 2*i)
    print(i, value, sign, sign*value, sep='\t')
    total = total + sign*value
    sign = -1 * sign
print(total)
print("value:\t",total*4)
