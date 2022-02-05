#CIS 1051 Section 2
#Linh Nguyen

def check(text):
    text = text.lower()
    for i in text:
        if i not in "aeioupkhlmnw":
            return False
        
def hawaiian(text):
    text = text.strip()
    text = text.lower()
    proString = ""
    dicVowels = {"a": "ah",
                 "e": "eh",
                 "i": "ee",
                 "o": "oh",
                 "u": "oo"
                 }
    dicDouble = {"ai": "eye",
                 "ae": "eye",
                 "ao": "ow",
                 "au": "ow",
                 "ei": "ay",
                 "eu": "eh",
                 "iu": "eh-oo",
                 "oi": "ew",
                 "ou": "oyo",
                 "ui": "ooey"
                 }
    for i in range(0, len(text), 1):
        if text[i] in dicVowels:
            if text[(i-1):(i+1)] in dicDouble:
                if text[(i-2):(i)] in dicDouble:
                    proString = proString + dicVowels[text[i]]
            elif text[i:i+2] in dicDouble:
                proString = proString + dicDouble[text[i:i+2]]
            elif text[i-1:i+1] not in dicDouble:
                proString = proString + dicVowels[text[i]]
        elif text[i] not in dicVowels:
            proString = proString + "-" + text[i]
    print(text + " is pronounced " + proString)

def main():
    enter = True
    while True:
        text = input("Enter a hawaiian word to pronounce: ")
        if check(text) == False:
            while check(text) == False:
                print(text + " is not a valid hawaiian character")
                text = input("Please re-enter: ")
                if check(text) != False:
                    hawaiian(text)
        else:
            hawaiian(text)
        last = input("Do you want to enter another word? Y/YES/N/NO ")
        last = last.lower()
        if last in ["yes", "y"]:
            enter = True
        else:
            break

main()
