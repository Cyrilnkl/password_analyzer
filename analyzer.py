# SE WE CAN CREATE A REGEX
import re

def checkSpecialCharacters(password):
    score = 0
    specialChar = "!@#$%^&*()-_=+{}[]|:;'\""

    for i in range (0, len(password)):
        if (password[i] in specialChar):
            print("oui : ", password[i])

            # IF ONE SPECIAL CHAR
            if (score == 0) : score+=5
            # IF TWO SPECIAL CHAR
            if (score == 5) : score+=15

            # IF MORE SEPARATE SPECIAL CHAR
            if (score == 10 and password[i-1] not in specialChar) : score+=10
            elif (score == 10): score+=5

    return score

def checkMinCharacters(password):
    score = 0
    minChar = [chr(i) for i in range(ord('a'), ord('z')+1)]

    print(minChar)

