def factorial(number):
    result = 1
    count = 2
    while count <= number:
        result = result * count
        count = count + 1

    return result

def getNumberOfPath(row,column):
    return factorial(row+column)/(factorial(row) * factorial(column))

print getNumberOfPath(20,20)
