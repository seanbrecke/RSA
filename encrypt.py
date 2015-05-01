def encrypt(rawtext, modulo, user_input_key):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
	rawtext = rawtext.lower()
	l = list(rawtext)
	n = []
	for x in l:
		n.append(alphabet.index(x)+1)

	if user_input_key == "None":
		e = 65537
	else:
	    e = user_input_key
	m = modulo
	c = []

	for x in n:
		c.append(str((x**e)%m))
	c = [ x[:-1] for x in c ]
	c = [ int(x) for x in c ]
	return c
