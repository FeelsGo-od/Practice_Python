sequence = []
current_number = 0

def gen_fibon_sequence(number, current_number, sequence):
    sequence = [0, 1]
    for _ in range(2, number):
        sequence.append(sequence[-2] + sequence[-1])
    return sequence

try:
    number = int(input("Write the number of terms in the Fibonacci sequence: "))
    if number < 0:
        print("Number of terms should be a non-negative integer.")
    print(gen_fibon_sequence(number, current_number, sequence))
except ValueError:
    print("Please, provide a valid non-negative integer.")