import bruteforce
import decrypt
import encrypt
import key_generation

print("yo")
print("this is a CLI")
print("Welcom to Seany Wonny's RSA Suite")

var user_encryption_input = str(raw_input("How about we encrypt some text?")).lower()
var user_encryption_modulo = int(raw_input("With some modulo?"))

print(encrypt.encrypt(user_encryption_input, user_encryption_modulo))