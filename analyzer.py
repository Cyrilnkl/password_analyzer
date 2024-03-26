def checkSpecialCharacters(password, score):
    specialChar = "!@#$%^&*()-_=+{}[]|:;'\"";

    for i in range (0, len(password)):
        if (password[i] in specialChar) : 
            print("oui : ", password[i])
    return 0

