# SE WE CAN CREATE A REGEX
import re

from readFile import *


def checkLength(password):
    if len(password)>7 : return 10
    return 0


def checkSpecialCharacters(password):
    score = -2
    specialChar = "!@#$%^&*()-_=+{}[]|:;'\""

    for i in range (0, len(password)):
        if (password[i] in specialChar):

            # IF ONE SPECIAL CHAR
            if (score == -2) : score+=7
            # IF TWO SPECIAL CHAR
            elif (score == 5) : score+=15

            # IF MORE SEPARATE SPECIAL CHAR
            elif (score == 10 and password[i-1] not in specialChar) : score+=10
            elif (score == 10): score+=5

    return score


def checkLowercase(password):
    score = -4
    counter = 0
    lowercase_alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

    for i in range (0, len(password)):
        if (password[i] in lowercase_alphabet):
            counter+=1

            if(score == -4): score+=4
            elif(score == 0): score+=5
            elif(score == 5): score+=5

    if(counter == len(password)):
        score = 0

    return score


def checkUppercase(password):
    score = -4
    counter = 0
    uppercase_alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]

    for i in range (0, len(password)):
        if (password[i] in uppercase_alphabet):
            counter+=1

            if(score == -4): score+=4
            elif(score == 0): score+=5
            elif(score == 5): score+=5

    if(counter == len(password)):
        score = 0

    return score


def checkNumbers(password):
    score = -3
    counter = 0
    numbers = [chr(i) for i in range(ord('0'), ord('9')+1)]

    for i in range (0, len(password)):
        if (password[i] in numbers):
            counter+=1

            if(score == -3): score+=3
            elif(score == 0): score+=5
            elif(score == 5): score+=5

    if(counter == len(password)):
        score = 0

    return score


def checkMain(password):
    score = 0

    if(leakCheck(password)):
        return 0

    score += checkLength(password)
    score += checkSpecialCharacters(password)
    score += checkLowercase(password)
    score += checkUppercase(password)
    
    return score


#def displayResult(score):
#    if(score < 20):
#        