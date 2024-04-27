import math

number = int(input("Write a number to check if it is prime: "))

if number > 1:
    prime = True
    for num in range(2, int(math.sqrt(number))+1):
        if number % num == 0:
            print("The number is not prime")
            prime = False
            break
        else:
            continue

    if prime == True:
        print("Number is prime")
else:
    print("The number should be a natural number greater than 1")