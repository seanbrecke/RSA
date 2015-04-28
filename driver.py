import bruteforce
import decrypt
import encrypt
import key_generation

print("yo")
print("this is a CLI")
print("Welcom to Seany Wonny's RSA Suite")

user_encryption_input = str(raw_input("How about we encrypt some text? \n")).lower()
user_encryption_modulo = int(raw_input("\nWith some modulo? \n"))

print(encrypt.encrypt(user_encryption_input, user_encryption_modulo))