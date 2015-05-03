#imports functions
import encrypt
import key_generation

#This script asks the user for known information, and uses it to encrypt (or generate a new modulus and then) entered text
user_encryption_key = "None"
user_encryption_input = str(raw_input("What is the text? \n")).lower()
print("\n To generate a new modulus, leave blank. \n")
generated_modulus = (raw_input("\n What is the Modulus? \n"))
if generated_modulus == "" or generated_modulus == " ":
  upperlimit = int(raw_input("\n Upper Limit for Modulus, Must be above 70,000 \n"))
  new_key = key_generation.new_mod(upperlimit)
  generated_modulus = new_key[0]
  print("\n [Modulus, Encrpytion Key, Decryption Key]  \n")
  print(new_key)
else:
  user_encryption_key = int(raw_input("\n What is the encryption key? \n"))
  
print("\n Encrypted Message \n")
print(encrypt.encrypt(user_encryption_input, int(generated_modulus), user_encryption_key))
