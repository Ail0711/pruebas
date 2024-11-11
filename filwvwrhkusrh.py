from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Generar una clave secreta de 256 bits (32 bytes)
key = os.urandom(32)

# Generar un vector de inicialización (IV) de 128 bits (16 bytes)
iv = os.urandom(16)

# Crear un objeto Cipher utilizando AES y el modo CBC
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

# Crear el cifrador
encryptor = cipher.encryptor()

# Texto plano a cifrar
plaintext = b"Este es un mensaje secreto."

# Agregar padding para asegurar que sea múltiplo de 16 bytes (AES block size)
padder = padding.PKCS7(128).padder()
padded_data = padder.update(plaintext) + padder.finalize()

# Cifrar el texto
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# Mostrar el texto cifrado
print("Texto cifrado:", ciphertext)

# Crear el descifrador
decryptor = cipher.decryptor()

# Descifrar el texto cifrado
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

# Eliminar el padding
unpadder = padding.PKCS7(128).unpadder()
decrypted_text = unpadder.update(decrypted_padded) + unpadder.finalize()

# Mostrar el texto descifrado
print("Texto descifrado:", decrypted_text)
