#Initial starting points of the fibonacci sequence
num1 = 1
num2 = 2

sum = 0

#num1 must be the limiter as it's bound to be smaller than num2
while num1 < 4000000:
    #Only num1 is added in order to prevent sum of duplicate numbers
    if num1 % 2 == 0:
       sum += num1
    #Store num2 as temp in order for num1 to assign as the former num2 after num2 is assigned as num1+num2
    temp = num2
    num2 += num1
    num1 = temp

print(sum)