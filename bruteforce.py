def isprime(n):
    n = abs(int(n))
    if n < 2:
    	return False
    if n == 2:
    	return True
    for x in range(3, int(n**0.5)+1, 2): 
        if n % x == 0:
            return False
    return True

def factors(l):
    n = int(l)
    for x in range(1,int(n**0.5+1)):
        if n%x == 0 and n%(n/x)==0 and isprime(x) == True and isprime(n/x) == True:
            return [x, n/x]

def bruteforce(modulus):
	return factors(modulus)
	
user_input_modulus = int(raw_input("\n What is the Modulus? \n"))
print(bruteforce(user_input_modulus))
