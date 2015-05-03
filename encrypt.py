#padding scheme is just the order in the alphabet, spaces are 27
def encrypt(rawtext, modulo, user_input_key):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
	rawtext = rawtext.lower() #lowers all capital letters
	l = list(rawtext) #creates a list to 
	n = []
	for x in l:
		n.append(alphabet.index(x)+2)
#it adds 2 to make sure no input letters are 1, because 1^N is still 1, encryption would not work.
	if user_input_key == "None": #uses logic from driver to choose e value.
		e = 65537
	else:
	    e = user_input_key
	m = modulo
	ciphertext = []

	for x in n:
		ciphertext.append(str((x**e)%m)) #uses m^e mod n, to encrpyt.
	ciphertext = [ x[:-1] for x in ciphertext ] 
	ciphertext = [ int(x) for x in ciphertext ] #fixes problems based on using python
	return ciphertext
