# Function that checks if a number is prime number or not
def checkPrime(num):
    if num > 1:
        for eachNum in range(2 , num):
            if num % eachNum == 0:
                return False
        return True
    else:
        return False

isNotFound = True
index = 0
num = 0

# Loop that increases the index every time when a prime number is found and stops when index variable becomes 10001
while isNotFound:
    if checkPrime(num):
        index += 1
    if index == 10001:
        isNotFound = False
        primeNumToBeFound = num
    num += 1

print(primeNumToBeFound)