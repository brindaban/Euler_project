def isPrime(number):
    maxFactor = round(pow(number,0.5));
    counter = 2
    while counter <= maxFactor:
        if number % counter == 0:
                return False
        counter = counter+1
    return True

def findTotal(limit):
    count = 2
    total = 0
    while count<=limit:
        if isPrime(count):
            total = total + count
        count = count + 1
    return total

print findTotal(2000000)
