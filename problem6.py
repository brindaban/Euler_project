def differenceOfSqureOfSumAndSumOfSqure(limit):
    sumOfSqure = limit*(limit+1)*((2*limit)+1)/6
    sumOfNaturalNumber = limit*(limit+1)/2
    return pow(sumOfNaturalNumber,2) - sumOfSqure

print differenceOfSqureOfSumAndSumOfSqure(100)
