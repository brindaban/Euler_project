# > 1000000-(2*fact(9)+6*fact(8)+6*fact(7)+2*fact(6)+5*fact(5)+1*fact(4)+2*fact(3)+fact(2)+fact(1))==1

def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)

digits = "0123456789"
sequence = ""
term = 999999
counterPosition = 1
while counterPosition<10:
    multiplier = 1
    factorial = fact(10 - counterPosition)
    while term>=multiplier*factorial:
        multiplier = multiplier+1
    term = term - (multiplier-1)*factorial
    currentIndex = 0
    count = 0
    while count<=multiplier-1:
        if sequence.find(digits[currentIndex])>=0:
            currentIndex = currentIndex+1
        else:
            currentIndex = currentIndex +1
            count = count+1
    sequence = sequence+digits[currentIndex-1]
    counterPosition = counterPosition+1
for x in range(0,9):
    if sequence.find(digits[x])==-1:
        sequence = sequence+digits[x]
        break

print sequence
