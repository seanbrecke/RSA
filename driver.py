import bruteforce
import decrypt
import encrypt
import key_generation

user_encryption_input = str(raw_input("What is the text? \n")).lower()
user_encryption_modulo = int(raw_input("\nWhat is the Modulus? \n"))

print(encrypt.encrypt(user_encryption_input, user_encryption_modulo))
