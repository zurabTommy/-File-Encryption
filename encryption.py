import pyAesCrypt
import os
password = input('Введите ключ :')
filename = input('Введите имя файла:')
def encryption():
    buffer_size = 512 * 1024
    pyAesCrypt.encryptFile(str(filename), str(filename)+'.aes', password, buffer_size)

encryption()
os.remove(filename)