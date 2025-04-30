# In order for us to be able to find the minimum number that can be divided to any number in the range of 1-20,
# We must simply list all of the prime numbers in that range
primeNumDictionary = {2:0 , 3:0 , 5:0 , 7:0 , 11:0 , 13:0 , 17:0 , 19:0}

# This for loop calculates the minimal power value for each prime number in our list
for num in range (2 , 21):
    for each in primeNumDictionary:
        temp = 0
        while num % each == 0:
            num /= each
            temp += 1
        if temp > primeNumDictionary[each]:
            primeNumDictionary[each] = temp

# Then we multiply each prime number with their needed power values
wantedNumber = 1
for each in primeNumDictionary:
    wantedNumber *= each ** primeNumDictionary[each]

print(wantedNumber)
