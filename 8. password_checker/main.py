SpecialSym = '$@!$%^&*~'
password = input("Write a password: ")

def check_length(password):
    if len(password) < 12:
        raise Exception("The password should be at least 12 characters long")
    else:
        pass

def check_cases(password):
    if not any(char.isupper() for char in password):
        raise Exception("Password should have at least one uppercase letter")
    elif not any(char.islower() for char in password):
        raise Exception("Password should have at least one lowercase letter")
    else:
        pass
    
def check_on_digit(password):
    if not any(char.isdigit() for char in password):
        raise Exception("Password should contain at least one numeral")
    else:
        pass

def check_on_symbol(password):
    if not any(char in SpecialSym for char in password):
        raise Exception("Password should contain at least one symbol")
    else:
        pass
    

if __name__ == '__main__':
    try:
        check_length(password)
        check_cases(password), 
        check_on_digit(password)
        check_on_symbol(password)
        print("The password is strong.")
    except Exception as ex:
        print(ex)
