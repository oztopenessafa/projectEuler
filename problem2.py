num1 = 1
num2 = 2
sum = 0
while num1 < 4000000:
    if num1 % 2 == 0:
       sum += num1
    temp = num2
    num2 += num1
    num1 = temp
print(sum)