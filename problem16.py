def getThenumber(to, thePower):
    powerResult = to ** thePower
    result = 0
    reminder = 0
    while powerResult != 0:
        reminder = powerResult%10
        powerResult = powerResult/10
        result += reminder
    return result

print getThenumber(2,1000)
