import key_generation #imports functions from key_generation
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

#if the remainder of a test number when divided by the modulus is 0, the modulus/number modular the modulus is 0, and both the numbers are prime, it finds the 2 factors that give the modulus.
def factors(l):
    n = int(l)
    for x in range(1,int(n**0.5+1)):
        if n%x == 0 and n%(n/x)==0 and isprime(x) == True and isprime(n/x) == True:
            return [x, n/x]

#brute force RSA.
#The entire security of RSA relies on the fact that it is difficult to factor the product of 2 large primes. The modulus, which is public, if it is able to be factored into its 2 prime components, you can use the totient function, and then the modular inverse to find the decryption key. If we are able to factor the modulus, we know everything.

#input, output, uses modulus and encryption key to brute force find decryption key.
user_input_encrpytion_key = int(raw_input("\n What is the encrpytion key? \n"))	
user_input_modulus = int(raw_input("\n What is the Modulus? \n"))
print("\n [p, q] \n")
print(factors(user_input_modulus))
print("\n Decryption key \n")
print(key_generation.inverse(user_input_encrpytion_key,user_input_modulus))
