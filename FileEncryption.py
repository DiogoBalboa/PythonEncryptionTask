import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os


def write_key():
    key = Fernet.generate_key()
    with open("key.file", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Key Generated", "A new encryption key has been saved as 'key.file'")


def load_key():
    if os.path.exists("key.file"):
        return open("key.file", "rb").read()
    else:
        messagebox.showerror("Error", "No key file found! Generate a key first.")
        return None


def encrypt_file():
    filename = filedialog.askopenfilename(title="Select a file to encrypt")
    if filename:
        key = load_key()
        if key:
            fernet = Fernet(key)
            with open(filename, "rb") as file:
                file_data = file.read()
            encrypted_data = fernet.encrypt(file_data)
            with open(filename, "wb") as file:
                file.write(encrypted_data)
            messagebox.showinfo("Success", "File encrypted successfully!")


def decrypt_file():
    filename = filedialog.askopenfilename(title="Select a file to decrypt")
    if filename:
        key = load_key()
        if key:
            fernet = Fernet(key)
            with open(filename, "rb") as file:
                encrypted_data = file.read()
            try:
                decrypted_data = fernet.decrypt(encrypted_data)
                with open(filename, "wb") as file:
                    file.write(decrypted_data)
                messagebox.showinfo("Success", "File decrypted successfully!")
            except Exception:
                messagebox.showerror("Error", "Invalid key or file is not encrypted!")


# GUI Setup
root = tk.Tk()
root.title("File Encryptor/Decryptor")
root.geometry("400x250")

tk.Label(root, text="File Encryption/Decryption Tool", font=("Arial", 12, "bold")).pack(pady=10)

tk.Button(root, text="Generate Key", command=write_key, width=20).pack(pady=5)
tk.Button(root, text="Encrypt File", command=encrypt_file, width=20).pack(pady=5)
tk.Button(root, text="Decrypt File", command=decrypt_file, width=20).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=5)

root.mainloop()
