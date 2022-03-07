from cryptography.fernet import Fernet

def encrypt_keys():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as file:
        file.write(key)
        file.close()

    with open('key.key', 'rb') as fkey:
        key = fkey.read()
        fkey.close()

    with open('sas_keys.json', 'rb') as f:
        data = f.read()
        f.close()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open('sas_keys.json', 'wb') as f:
        f.write(encrypted)
        f.close()

def decrypt_keys():
    with open('key.key', 'rb') as fkey:
        key = fkey.read()
        fkey.close()

    with open('sas_keys.json', 'rb') as file:
        encrypted_data = file.read()
        file.close()

    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()
