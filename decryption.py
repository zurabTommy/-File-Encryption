import pyAesCrypt
import os
password = input('Введите ключ :')
filename = input('Введите имя файла:')
def dencryption():
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(filename), str(os.path.basename(filename)[:filename.find('.', 2)]), password, buffer_size)

dencryption()
os.remove(filename)