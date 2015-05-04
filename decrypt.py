#Decryption script, padding scheme is just the order in the alphabet, spaces are 27.
def decrypt(r_input, decryption_key, modulus_key):

	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
#uses modulus and decryption key to change encrypted numbers into numbers related to padding scheme
	n = []
	for x in r_input:
	    if type(x) == int:
	        long_converted = str((int(x)**decryption_key)%modulus_key)
	        n.append(int(long_converted[:-1])-2)
	        
#changes numbers to letters, it subtracts 2 to make account for adding 2 earlier in encryption.
	l = []
	text = ""
	for x in n:
	    l.append(alphabet[x])
#changes from a list to a string
	for x in l:
	    text += str(x)
	return text
#input and output
user_ciphertext_input = list(raw_input("\n Enter Ciphertext as List \n For example: [15, 41, 53] \n"))
user_decryption_key_input = int(raw_input("\n What is the Decryption Key \n"))
user_modulus_input = int(raw_input("\n What is the Modulus? \n"))
print(decrypt(user_ciphertext_input, user_decryption_key_input, user_modulus_input))
