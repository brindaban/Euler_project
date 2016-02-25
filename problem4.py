def isPalindrome(number):
    return number == int(str(number)[::-1])

def isMultiplyOfTwoThreeDigitNo(number):
    counter = 999
    while counter>900:
        if number%counter == 0 and number/counter<1000:
            return True
        counter = counter - 1
    return False

def findLargestPalindrome(number):
    while number>9801:
        if isPalindrome(number)==True:
            if isMultiplyOfTwoThreeDigitNo(number) == True:
                return number;
        number = number-1;
print findLargestPalindrome(999*999)
