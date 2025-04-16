sum = 0
for num in range(1000):
    if num % 3 == 0 or num % 5 == 0: #Add the numbers that can be divided to 3 either 5 to sum
       sum += num
print(sum)