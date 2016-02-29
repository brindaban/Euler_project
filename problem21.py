def getAllFactorsSum(number):
    storage = 0
    maxCheck = round(number ** 0.5)
    count = maxCheck
    while count>1:
        if number%count == 0:
            storage = storage + count + number/count;
        count = count - 1
    return storage + 1

def isAmicableNo(number):
    return number != getAllFactorsSum(number) and getAllFactorsSum(getAllFactorsSum(number)) == number 

def getTheResult(limit):
    total = 0
    count = 2
    while count < limit:
        if isAmicableNo(count):
            print count
            total = total + count
        count = count + 1
    return total

print getTheResult(10000)
