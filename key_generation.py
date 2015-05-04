import random #imports module that includes functions pertaining randomness
def isprime(n): #function that tests if a number is prime, by recursively testing if a number n can be divided through a list. If it returns 0, that means it has a factor, and is not prime 
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2): #list from 3 to the square root of the number + 1; a numbers factors are always less than its square root.
        if n % x == 0:
            return False
    return True
#these two functions find the modular multiplicative inverse for 'e mod phi(n)', using modular and binary arithmetic. 
def initial(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = initial(b % a, a)
        return (g, x - (b // a) * y, y)
def inverse(a, m):
    gcd, x, y = initial(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
        
#finds prime number between entered number n and 2n.
def largeprime(n):
    c = []
    for z in range(n,n*2): #We know there is a prime between n and 2n because of bertrand's postulate
        if len(c) == 2: #stops if it finds 2 primes
		    return c
        elif isprime(z) == True:
            c.append(z) #finds primes

def new_mod(upper): #find new modulus and new decryption key, encryption key is kept at 2^16+1  
    max_no = int(upper)
    largeprimelist = largeprime(random.randint(70000,max_no)) #finds p and q
    phi = largeprimelist[0]*largeprimelist[1] #calculates modulus
    return [phi, 65537, inverse(65537,phi)] #returns modulus, encryption key, decryption key
