from cryptography.fernet import Fernet

def encryptKeys():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as file:
        file.write(key)
        file.close()

    with open('key.key', 'rb') as fkey:
        key = fkey.read()
        fkey.close()

    with open('sas_keys.json', 'rb') as file:
        data = file.read()
        file.close()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open('sas_keys.json', 'wb') as file:
        file.write(encrypted)
        file.close()

def decryptKeys():
    with open('key.key', 'rb') as fkey:
        key = fkey.read()
        fkey.close()

    with open('sas_keys.json', 'rb') as file:
        encrypted_data = file.read()
        file.close()

    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()
