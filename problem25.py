def getTheNumber(first,second,limit,count):
    if second/(10 ** (limit-1))>1:
        return [first,second,count]
    count = count + 1
    temp = first + second;
    first = second
    second = temp
    return getTheNumber(first,second,limit,count)


def getTheResult():
    twoHundredDigitNo = getTheNumber(1,1,200,0);
    # print twoHundredDigitNo[2]
    fourHundredDigitNo = getTheNumber(twoHundredDigitNo[0],twoHundredDigitNo[1],400,twoHundredDigitNo[2])
    # print fourHundredDigitNo[2]
    sixHundredDigitNo = getTheNumber(fourHundredDigitNo[0],fourHundredDigitNo[1],600,fourHundredDigitNo[2])
    # print sixHundredDigitNo[2]
    eightHundredDigitNo = getTheNumber(sixHundredDigitNo[0],sixHundredDigitNo[1],800,sixHundredDigitNo[2])
    # print eightHundredDigitNo[2]
    oneThousandDigitNo = getTheNumber(eightHundredDigitNo[0],eightHundredDigitNo[1],1000,eightHundredDigitNo[2])
    # print oneThousandDigitNo[2]
    print len(str(oneThousandDigitNo[1]))
    print oneThousandDigitNo[2]

getTheResult()
