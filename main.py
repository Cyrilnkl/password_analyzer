from analyzer import *

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKCYAN = '\033[96m'

if __name__ == "__main__":
                                                                                   
    print(" _ __  __ _ _______ __ _____ _ _ __| |  ___   __ _ _ _  __ _| |_  _ ______ _ _ ")
    print("| '_ \/ _` (_-<_-< V  V / _ \ '_/ _` | |___| / _` | ' \/ _` | | || |_ / -_) '_|")
    print("| .__/\__,_/__/__/\_/\_/\___/_| \__,_|       \__,_|_||_\__,_|_|\_, /__\___|_|  ")
    print("|_|                                                            |__/            \n\n")

    print(bcolors.WARNING + "Welcome to the password analyzer...")
    print(bcolors.WARNING + "Let's see the level of security of your password\n")

    print(bcolors.OKBLUE + "Please enter your password : ", end="")
    password = input()

    score = 0;
    score = checkMain(password)

    score = int((score/60)*100)
    print("\n\nThere is the score of your password :", score, "%")
    print(bcolors.OKCYAN + "\n\nSecurity level :", end="");

    displayResult(score)
