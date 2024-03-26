def leakCheck(password):
    f = open("pass.txt", "r")
    for line in f:

        if(line[:-1] == password):
            return 1

    return 0
        