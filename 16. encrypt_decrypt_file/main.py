import os
from cryptography.fernet import Fernet
from utils import create_path

# Generate a random symmetric key
key = Fernet.generate_key()


def encrypt_file(input_file, output_file, key):
    # Read plaintext data from input file
    with open(input_file, "rb") as f:
        plaintext = f.read()

    # Create a Fernet symmetric encryption object with the key
    cipher = Fernet(key)

    # Encrypt the plaintext
    encrypted_data = cipher.encrypt(plaintext)

    # Write the encrypted data to the output file
    with open(output_file, "wb") as f:
        f.write(encrypted_data)


def decrypt_file(input_file, output_file, key):
    # Read encrypted data from input file
    with open(input_file, "rb") as f:
        encrypted_data = f.read()

    # Create a Fernet symmetric encryption object with the key
    cipher = Fernet(key)

    # Decrypt the encrypted data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Write the decrypted data to the output file
    with open(output_file, "wb") as f:
        f.write(decrypted_data)


def export_key(key, output_file):
    with open(output_file, "wb") as f:
        f.write(key)


def import_key(input_file):
    with open(input_file, "rb") as f:
        key = f.read()
    return key


# current working directory
cwd = os.getcwd()

# Constuct the absolute path to plaintext.txt, encrypted.txt and other files
plaintext_path = os.path.join(cwd, "encrypt_decrypt_file", "plaintext.txt")
encrypted_path = create_path(plaintext_path, "encrypted.txt")
decrypted_path = create_path(plaintext_path, "decrypted.txt")
key_path = create_path(plaintext_path, "key.txt")


def main():
    encrypt_file(plaintext_path, encrypted_path, key)
    export_key(key, key_path)

    # decryption
    imported_key = import_key(key_path)
    decrypt_file(encrypted_path, decrypted_path, imported_key)


if __name__ == "__main__":
    main()


"""

1. Generate a Symmetric Key:
We need a special key to encrypt and decrypt our files. 
Think of it like a secret code that only you and the person you want 
to share files with know. This key is generated randomly and will be 
used for both encryption and decryption.

2. Encrypting Files:
- Imagine you have a message you want to keep secret, and you want 
to put it in a locked box before sending it. Here, the message is 
your file, and encryption is like putting it in a locked box. 
We use a special method called AES (Advanced Encryption Standard) 
to lock the box.
- First, we read the contents of your file (the message).
- Then, we use the AES method with the symmetric key (the lock) to 
encrypt the contents.
- Finally, we write the encrypted contents to a new file, which is 
like putting the locked box somewhere safe.

3. Decrypting Files:
- Now, imagine you receive the locked box and want to read the message 
inside. Decryption is like unlocking the box to read the message.
- First, we read the encrypted contents from the file (the locked box).
- Then, we use the same AES method and symmetric key (the same lock)
to decrypt the contents.
- Finally, we write the decrypted contents to a new file, which 
is like opening the locked box to read the message.

---------------------------------------------------

# In the line cipher = Fernet(key), we are creating a Fernet symmetric 
encryption object using the provided key. Let's break it down:

1. Fernet Encryption:
- Fernet is a symmetric encryption algorithm. Symmetric encryption means 
that the same key is used for both encryption and decryption.
- Fernet provides a simple and secure way to encrypt and decrypt data.
2. Creating a Fernet Object:
- To use Fernet for encryption and decryption, we need to create a 
Fernet object.
- This object will be responsible for performing encryption and decryption 
operations using the provided key.
3. Key Initialization:
- When creating the Fernet object, we pass the symmetric key (key) as an 
argument.
- This key is used internally by the Fernet algorithm to encrypt and 
decrypt data.
- It's essential to use the same key for both encryption and decryption 
operations. Otherwise, decryption won't be possible.
"""
