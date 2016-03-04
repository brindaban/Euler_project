def getLengthOfTheChain(number):
    count = 1
    while number!=1:
        if number%2==0:
            number = number/2
        else:
            number = 3*number + 1
        count = count+1
    return count

def getTheNumberWhoHasHeighestChain(limit):
    heighstLengthCount = 0
    leadingNumber = 0
    chechUpTo = limit/2;
    while limit>chechUpTo:
        currentCount = getLengthOfTheChain(limit)
        if currentCount>heighstLengthCount:
            heighstLengthCount,leadingNumber = currentCount,limit
        limit = limit - 1
    return leadingNumber


# print getTheNumberWhoHasHeighestChain(1000000)
storeNumberWithTheLength = {1:1}
def storeAllNumber(number):
    global storeNumberWithTheLength
    if storeNumberWithTheLength.has_key(number)==False:
        if number%2 == 0:
            storeNumberWithTheLength[number] = storeAllNumber(number/2) + 1
        else:
            storeNumberWithTheLength[number] = storeAllNumber(3*number + 1) + 1
    return storeNumberWithTheLength[number]

for number in range(2,1000000):
    storeAllNumber(number)

print storeNumberWithTheLength.values().index(max(storeNumberWithTheLength.values()))
