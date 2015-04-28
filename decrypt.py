#for this example, the padding scheme is just the order in the alphabet, ' ' is 25.

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
