from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.file", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.file", "rb").read()


write_key()

key = load_key()
print("Key is " + str(key.decode('utf-8')))

def encrypt(filename, key):

    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)
        print(encrypted_data)


def decrypt(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)
        print(decrypted_data)



encrypt("names.txt", key)
print("File encrypted!")
