import random
def isprime(n): 
    n = abs(int(n))
    if n == 2:
    	return True
    if n < 2:
    	return False
    for x in range(3, int(n**0.5)+1, 2): 
        if n % x == 0:
            return False
    return True
            
def initial(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = initial(b % a, a)
        return (g, x - (b // a) * y, y)
        
def inverse(a, m):
    gcd, x, y = initial(a, m)
    if gcd != 1:
        return None
    else:
        return x % m
        
def largeprime(n):
    c = []
    for z in range(n,n*2):
        if len(c) == 2:
		    return c
        elif isprime(z) == True:
            c.append(z)

def new_mod(upper): #find new modulus and new decryption key, encryption key is kept at 2**16+1  
    max_no = int(upper)
    largeprimelist = largeprime(random.randint(70000,max_no))
    prod = largeprimelist[0]*largeprimelist[1]
    return [prod, 65537, inverse(65537,prod)]
#returns (n, e, d)
