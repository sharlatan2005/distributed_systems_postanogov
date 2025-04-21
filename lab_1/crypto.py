from cryptography.fernet import Fernet
import json
import os

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

# Пример использования
# key = load_key()
# encrypt_token("your_access_token_here", key)
# decrypted_token = decrypt_token(key)