# Encrypt a single string
# Import Libraries
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

write_key()

key = load_key()

#In here we insert the key to decrypt the message
fernet = Fernet(b'3t3gzh8v0_IqcxB7rF-Hic3VaGp_3m-JBMNT8zOgO4s=')

#In here we insert the encrypted message to be decrypted
decodedmessage = fernet.decrypt(b'gAAAAABnpOzQ7Q8EPJKUrj05Lqtn73m7l8H5d3LbL2nKOd6zq9bRfVd8HTRysZ8KKecwPXYghSlQVK8iq1SSEnym5ghG5McWag===')
print("The hideen message is : " + str(decodedmessage.decode('utf-8')))



