# List of tuples that contain each 16 primitive pythagorean triplets
pythagoreanTriplets = [(3, 4, 5) , (5, 12, 13) , (8, 15, 17) , (7, 24, 25), (20, 21, 29) , (12, 35, 37) , (9, 40, 41) , (28, 45, 53) , (11, 60, 61) ,	(16, 63, 65) ,	(33, 56, 65) ,	(48, 55, 73) , (13, 84, 85) ,	(36, 77, 85) ,	(39, 80, 89) ,	(65, 72, 97) ]


i = 1
isFound = False
while not isFound:
    # All non-primitive pythagorean triplets are a multiple of a set of triplets,
    # therefore i is incremented in case of a triplet with a sum bigger than 1000
    for eachTuple in pythagoreanTriplets:
        numA = eachTuple[0] * i
        numB = eachTuple[1] * i
        numC = eachTuple[2] * i
        if(numA + numB + numC) > 1000:
            break
        elif (numA + numB + numC) == 1000:
            print(numA * numB * numC)
            isFound = True
    i += 1