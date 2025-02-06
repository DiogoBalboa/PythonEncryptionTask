from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

print("What message do you want to encrypt ?")
message = input()
# message_bytes = message.encode()

ciphertext = fernet.encrypt(b'message')
print(ciphertext)


