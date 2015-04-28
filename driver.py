import bruteforce
import decrypt
import encrypt
import key_generation

user_encryption_input = str(raw_input("What is the text? \n")).lower()
print("\n To generate a new modulus, leave blank. \n")
generated_modulus = int(raw_input("\nWhat is the Modulus? \n"))
if generated_modulus == "":
  generated_modulo = key_generation.new_mod()
print(encrypt.encrypt(user_encryption_input, generated_modulo))
