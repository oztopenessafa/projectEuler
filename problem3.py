#Function that checks if a number is a prime number or not
def isPrime(num):
    numOfFactors = 0
    for each in range (1 , num + 1):
        if num % each == 0:
            numOfFactors += 1
    if numOfFactors != 2:
        return False
    else:
        return True

largeNum = 600851475143
checkedNumber = 1
largestPrimeFactor = -1

while largeNum != 1:
    if isPrime(checkedNumber):
            #Divide the large number as much as it can be divided with no remainders
            while largeNum % checkedNumber == 0:
                largeNum /= checkedNumber
            #Assign the most recent prime factor to the largestPrimeFactor variable
            if largestPrimeFactor < checkedNumber:
                largestPrimeFactor = checkedNumber

    checkedNumber += 1
print(largestPrimeFactor)