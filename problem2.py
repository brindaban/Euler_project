def checkAndAdd(first,second,result,limit):
    temp = first + second;
    if temp>limit:
        return result
    first = second
    second = temp
    if temp%2==0:
        result=result+temp
    return checkAndAdd(first,second,result,limit)


def countFibo(limit):
    return checkAndAdd(1,2,2,limit)
print countFibo(4000000)
