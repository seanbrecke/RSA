#encrypts larger files quickly
#for this example, the padding scheme is just the order in the alphabet, ' ' is 25.


def encrypt(rawtext):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
	rawtext = rawtext.lower()
	l = list(rawtext)
	n = []
	for x in l:
    	n.append(alphabet.index(x)+1)

	e = 65537
	m = int(raw_input("Modulus?"))
	c = []

	for x in n:
	    c.append((x**e)%m)

	return c