def getAllFactors(number):
    storage = []
    maxCheck = round(number ** 0.5)
    count = maxCheck
    indexCounter = 0
    while count>1:
        if number%count == 0:
            storage.insert(indexCounter,count)
            indexCounter = indexCounter + 1
            storage.insert(indexCounter,number/count)
            indexCounter = indexCounter + 1
        count = count - 1
    return storage


def findResult(necessaryFactor):
    count = 0
    toincrement = 2
    number = 1
    while count<necessaryFactor:
        number = number + toincrement
        toincrement = toincrement + 1
        print getAllFactors(number)
        count = len(getAllFactors(number))+2
    return number

print findResult(500)
