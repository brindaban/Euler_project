def getGcd(firstNumber,secondNumber):
    reminder = 1
    while reminder != 0:
        reminder = firstNumber % secondNumber
        firstNumber = secondNumber
        secondNumber = reminder
    return firstNumber
def getLcmOf(firstNumber, secondNumber):
    return firstNumber*secondNumber/getGcd(firstNumber,secondNumber)

def getResult(result,currentNo,uperlimit):
    if currentNo == 1:
        return result
    currentNo = currentNo - 1
    result = getLcmOf(result,currentNo)
    return getResult(result,currentNo,uperlimit)


def findLcmOfRange(uperlimit):
    return getResult(uperlimit,uperlimit,uperlimit)

print findLcmOfRange(20)
