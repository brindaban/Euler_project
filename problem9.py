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


def isAdjancyMultiply(number):
    firstNumber = round(number ** 0.5)
    return number == firstNumber * (firstNumber+1)


def findThatParticularFactorWhichIsMultiplyOfTwoAdjacencyNumber(number):
    factorsOfTheNumber = getAllFactors(number)
    for number in factorsOfTheNumber:
        if isAdjancyMultiply(number):
            return number

def getTheExpectedRoot(a,b,c):
    derivation = ((b ** 2)-4*a*c) ** 0.5
    root1 = (-b - derivation)/(2*a)
    root2 = (-b + derivation)/(2*a)
    if root1<0:
        return root2
    return root1

def getThreeTriplet(number):
    specialNo = findThatParticularFactorWhichIsMultiplyOfTwoAdjacencyNumber(number);
    a = getTheExpectedRoot(1,1,-specialNo)*(number/specialNo)
    b = (((number-a) ** 2) - (a ** 2))/(2*(number-a))
    c = number-a-b
    return [a,b,c]


def getThreeMultiply(numbers):
    return numbers[0]*numbers[1]*numbers[2]

def getFinalResult(number):
    return getThreeMultiply(getThreeTriplet(number))

print getFinalResult(1000)
