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

fernet = Fernet(b'iz0NUE35-853azws9eZ83J-DfmpSjrdl_b1-qZhFrHU=')

decodedmessage = fernet.decrypt(b'gAAAAABnpM7liP3iwwzFnztfzjhyBZKlQhvHA3dOzYq9cL1Zpd0K7Oqj7L0GAf767P39BUXJ7Iyz4pa2L1y54DP9oBHMbmN_9ypDzFCSJAAFoDNpuMb6twg=')
print("The hideen message is : " + str(decodedmessage.decode('utf-8')))



