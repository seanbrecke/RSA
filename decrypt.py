#for this example, the padding scheme is just the order in the alphabet, ' ' is 25.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

c = raw_input("List of ciphertext?")
d = int(raw_input("Decryption Key?"))
m = int(raw_input("Modulus?"))

n = []
for x in c:
    n.append(((x**d)%m)-1)

l = []
text = ""
for x in n:
    l.append(alphabet[x])

for x in l:
    text += str(x)
    
print(text)
