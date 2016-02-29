def getTheResult(first,second,limit):
    if second/(10 ** (limit-1))>1:
        return first
    temp = first + second;
    first = second
    second = temp
    return getTheResult(first,second,limit)

print getTheResult(1,1,1000)
