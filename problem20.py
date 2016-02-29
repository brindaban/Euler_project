def factorial(number):
    result = 1
    count = 2
    while count <= number:
        result = result * count
        count = count + 1
    return result

def getTheResult(number):
    fact = factorial(number)
    total = 0
    while fact>0:
        reminder = fact%10
        total = total + reminder
        fact = fact/10
    return total

print getTheResult(100)
