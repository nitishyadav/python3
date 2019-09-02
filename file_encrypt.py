#'pyAesCrypt' module of python is a file encryption module that uses AES256-CBC to encrypt/decrypt files and binary streams

from os import stat, remove
import pyAesCrypt

#encryption/decryption buffer size - 64k
bufferSize = 64 * 1024
password = "#Training"
with open("analysis.txt", "rb") as fIn:
	with open("sample.txt.aes", "wb") as fOut:
		pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
	#get encrypted file size
encFileSize = stat("sample.txt.aes").st_size
