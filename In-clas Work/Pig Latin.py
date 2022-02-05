#CIS 1051
#Section 009
#Linh Nguyen

def findFirstVowel(word):
    for index, letter in enumerate(word):
        #print("Checking:", index, letter, sep = "\t")
        if letter in "aeiou":
            return index
    return len(word) - 1

def convertToPigLatin(word):
    index = findFirstVowel(word)
    if index == 0:
        return word[1:] + word[0] + "way"
    else:
        return word[index:] + word[:index] + "ay"

def reverse(word):
    rev = word.split()
    rev = list(reversed(word))
    print("".join(rev))
    
def main():
    finished = False
    while not finished:
        word = input()
        word = word.lower()
        if word == "done":
            finished = True
        else:
            pig = convertToPigLatin(word)
            print(pig)
            reverse(word)
        
main()
