def decrypt(raw_input, decryption_key, modulus_key):

	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

	c = raw_input
	d = decryption_key
	m = modulus_key

	n = []
	for x in c:
	    n.append(((x**d)%m)-1)

	l = []
	text = ""
	for x in n:
	    l.append(alphabet[x])

	for x in l:
	    text += str(x)
	    
	return text

user_ciphertext_input = list(raw_input("\n Enter Ciphertext as List \n For example: [15, 41, 53] \n"))
user_decryption_key_input = int(raw_input("\n What is the Decryption Key \n"))
user_modulus_input = int(raw_input("\n What is the Modulus? \n"))
print(decrypt(user_ciphertext_input, user_decryption_key_input, user_modulus_input))
