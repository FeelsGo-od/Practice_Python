import random
import string

def generate_password(length, complexity):
    if complexity == 'simple':
        characters = string.ascii_letters + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'strong':
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        raise ValueError("Invalid complexity level. Please choose 'simple', 'medium', or 'strong'.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator!")
    print("----------------------------------")

    while True:
        try:
            password_length = int(input("Enter the length of the password: "))
            if password_length <= 0:
                raise ValueError("Password length must be a positive integer.")
            break
        except ValueError as e:
            print(e)

    while True:
        password_complexity = input("Enter the complexity level of the password (simple, medium, strong): ").lower()
        if password_complexity not in ['simple', 'medium', 'strong']:
            print("Invalid complexity level. Please choose 'simple', 'medium', or 'strong'.")
        else:
            break

    password = generate_password(password_length, password_complexity)
    print("Generated password:", password)

if __name__ == "__main__":
    main()