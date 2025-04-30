# Function that check whether a number is palindrome or not
def checkPalindrome(num):
    isPalindrome = True
    i = 0
    indexCount = len(str(num))
    for digit in range(indexCount // 2 ):
        if str(num)[i] != str(num)[indexCount - i - 1]:
            isPalindrome = False
            break
        i += 1
    return isPalindrome

# Variable that'll keep the max palindrome value
max = -1

# For loop that check each product of every two 3-digit number combination
for num1 in range(100 , 1000):
    for num2 in range (100 , 1000):
        product = num1 * num2
        if checkPalindrome(product):
            if product > max:
                max = product

print(max)