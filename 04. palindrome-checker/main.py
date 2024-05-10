import string

users_string = input("Write a string to check if it is a palindrome: ")

def remove_space(users_string):
    return users_string.replace(" ", "")

def remove_punctuation(users_string):
    return users_string.translate(str.maketrans('', '', string.punctuation))

def reverse_string(users_string):
    return users_string[::-1]

users_string = users_string.strip(" ").lower()
users_string = remove_space(users_string)
users_string = remove_punctuation(users_string)
reversed_string = reverse_string(users_string)

if(users_string == reversed_string):
    print(f"Yes, {users_string} is a palindrome ({reversed_string}).")
else:
    print(f"No, {users_string} is not a palindrome ({reversed_string}).")