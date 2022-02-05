#CIS 1051 Section 009
#Linh Nguyen

import re

file = open("words.txt", 'r')
data = file.read()

Q1 = "1. How many words contain the word 'cat' or 'dog' in them? "
A1 = re.findall(r"cat|dog", data, flags = re.IGNORECASE)
print(Q1, len(A1), sep='\n')
print()

Q2 = "2. How many four letter words are there? "
A2 = re.findall(r"\b\w{4}\b", data)
print(Q2, len(A2), sep='\n')
print()

Q3 = "3. How many words containing 'hun' in them? "
A3 = re.findall(r"hun", data, flags = re.IGNORECASE)
print(Q3, len(A3), sep='\n')
print()

Q4 = "4. Do more words end in 'ing' or 'ion'? "
A4_1 = re.findall(r"ing$", data)
A4_2 = re.findall(r"ion$", data)
print(Q4)
if len(A4_1) - len(A4_2) > 0:
    print("There are more words ending in 'ing' than 'ion'. ")
else:
    print("There are more words ending in 'ion' than 'ing'. ")
print()

Q5 = "5. How many words contain a 'q' not immediately followed by a 'u.'? "
A5 = re.findall(r"q[^u.]", data)
print(Q5, len(A5), sep='\n')
print()

Q6 = "6. How many words have no vowels? "
A6 = re.findall(r"\b[bcdfghjklmnpqrstvwxyz]+\b", data)
print(Q6, len(A6), sep='\n')
print()

Q7 = "7. How many words consist of only vowels? "
A7 = re.findall(r"[aeiou]", data, flags = re.IGNORECASE)
print(Q7, len(A7), sep='\n')
print()

Q8 = "8. How many words are contracted with 'not', meaning they end with 'nt? "
A8 = re.findall(r"'nt$", data)
print(Q8, len(A8), sep='\n')
print()

Q9 = "9. How many words with two vowels in a row are there? "
A9 = re.findall(r"[aeiou]{2}", data, flags = re.IGNORECASE)
print(Q9, len(A9), sep='\n')
print()

Q10 = "10. How many words with at least two vowels are there? "
A10 = re.findall(r'[aeiou].*[aeiou]', data, flags = re.IGNORECASE)
print(Q10, len(A10), sep='\n')
