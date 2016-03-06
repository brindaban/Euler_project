def getTheRecurringDigits(dinomarator):
    resultDecimalePart = str(1/(dinomarator*1.0)).split('.')[1]
    myStr = ''
    count=0
    while count<len(resultDecimalePart)-1:
        if myStr.find(resultDecimalePart[count])>=0:
            if resultDecimalePart[count] == resultDecimalePart[count-1] or myStr[myStr.find(resultDecimalePart[count])+1]==resultDecimalePart[count+1]:
                return len(myStr) - myStr.find(resultDecimalePart[count])
        myStr = myStr + resultDecimalePart[count]
        count = count+1
    print resultDecimalePart

# count = 1
# heighst = 1
# stand = 1
# while count<1000:
#     if getTheRecurringDigits(count)>stand:
#         stand = getTheRecurringDigits(count)
#         heighst = count
#     count = count + 1

print heighst
