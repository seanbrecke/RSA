import random

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
        
def largeprime(n):
#n is the length of the prime
    c = []
    for z in range(n,n*2):
        if len(c) == 2:
		    return c
        elif isprime(z) == True:
            c.append(z)

def factors(l):
    n = int(l)
    for x in range(1,int(n**0.5+1)):
        print(long(x/n*100))
        if n%x == 0 and n%(n/x)==0 and isprime(x) == True and isprime(n/x) == True:
            return [x, n/x]
