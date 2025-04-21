from cryptography.fernet import Fernet
import json
import os

# key = Fernet.generate_key()
# with open('secret.key', 'wb') as key_file:
#     key_file.write(key)

def encrypt_token(token):
    key = open('secret.key', 'rb').read()
    f = Fernet(key)
    encrypted_token = f.encrypt(token.encode())
    with open('token.json', 'w') as file:
        json.dump(encrypted_token.decode(), file)

def decrypt_token():
    key = open('secret.key', 'rb').read()
    f = Fernet(key)
    with open('token.json', 'r') as file:
        encrypted_token = json.load(file).encode()
    return f.decrypt(encrypted_token).decode()