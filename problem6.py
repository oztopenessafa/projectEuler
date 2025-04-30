def sumOfSquares(num):
    sum = 0
    # Added num + 1 because the number in the second parameter is not inclusive in range() function
    for each in range(1 , num + 1):
        # Sums each number's square
        sum += each ** 2
    return sum

def squareOfSum(num):
    sum = 0
    # Same deal as before
    for each in range(1 , num + 1):
        sum += each
    # Returns the square of the sum of each number
    return sum ** 2

print(squareOfSum(100) - sumOfSquares(100))