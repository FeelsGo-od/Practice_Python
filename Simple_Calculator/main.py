def addition (value1, value2):
    print(f"Result: {value1 + value2}")

def subtraction (value1, value2):
    print(f"Result: {value1 - value2}")

def multiplication (value1, value2):
    print(f"Result: {value1 * value2}")

def division (value1, value2):
    print(f"Result: {value1 / value2}")


def calculate (option, value1, value2):
    if option == "+":
        addition(value1, value2)
    elif option == "-":
        subtraction(value1, value2)
    elif option == "*":
        multiplication(value1, value2)
    elif option == "/":
        division(value1, value2)
    else:
        print("Wrong option, choose the correct one from the list \n")
        option = input("Choose an option: + - * : ")
        calculate(option, value1, value2)

def is_int (string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    
def is_float (string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def set_type (item):
    if is_int(item):
        return int(item)
    elif is_float(item):
        return float(item)


while True:
    value1 = input("Input first number(E.g. - 12.0, 12): ")
    print(is_int(value1), is_float(value1))
    while is_int(value1) == False and is_float(value1) == False:
        value1 = input("Please, write a correct number (e.g. - 12.0, 12): ")

    value2 = input("Input second number(E.g. - 12.0, 12): ")
    while is_int(value2) == False and is_float(value2) == False:
        value2 = input("Please, write a correct number (e.g. - 12.0, 12): ")

    option = input("Choose an option: + - * / ")


    calculate(option, set_type(value1), set_type(value2))

    prompt = input("Write 'Q' if you want to quit. If not, you can just push 'Enter': ")
    if prompt.lower() == "q":
        break
