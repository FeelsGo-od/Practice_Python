import math


prompt = int(input("Write a natural non-negative number to count a factorial: "))

def count_factorial(number):
    try:
        return math.factorial(number)
    except:
        return "Error. Uncorrect number"
    
print(count_factorial(prompt))