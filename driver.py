import bruteforce
import decrypt
import encrypt
import key_generation

user_encryption_input = str(raw_input("What is the text? \n")).lower()
print("\n To generate a new modulus, leave blank. \n")
generated_modulus = int(raw_input("\nWhat is the Modulus? \n"))
if generated_modulus == "":
  upperlimit = int(raw_input("Upper Limmit for Modulus, Must be above 70,000"))
  key = key_generation.new_mod(upperlimit)
  generated_modulo = key[0]
  print("\n [Encrpytion Key, Decryption Key]  \n"),
  print(key)
  
print(encrypt.encrypt(user_encryption_input, generated_modulo))
