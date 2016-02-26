def isPrime(number):
    maxFactor = round(pow(number,0.5));
    counter = 2
    while counter <= maxFactor:
        if number % counter == 0:
                return False
        counter = counter+1
    return True

def findThePositionPrimeNO(position):
    counter = 2
    primeCounter = 0;
    while primeCounter<position:
        if isPrime(counter) == True:
            primeCounter = primeCounter + 1
        counter = counter + 1
    return counter-1

print findThePositionPrimeNO(10001)
