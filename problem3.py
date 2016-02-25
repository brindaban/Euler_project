def isPrime(number):
    maxFactor = round(pow(number,0.5));
    counter = 2
    while counter <= maxFactor:
        if number % counter == 0:
                return False
        counter = counter+1
    return True

def findLargestPrimeFactor(number):
    counter = 2
    limit = number/2
    while counter < limit:
        if number % counter == 0:
            boolean = isPrime(number/counter)
            if boolean == True:
                return number/counter
        counter = counter+1




print findLargestPrimeFactor(600851475143)
