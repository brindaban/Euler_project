def getTheResult(arg):
    firstNumber = 1
    seconNumber = 1
    count = 1
    while len(str(seconNumber)) < arg:
        seconNumber, firstNumber = seconNumber+firstNumber, seconNumber
        count += 1
    print count + 1
getTheResult(1000)
