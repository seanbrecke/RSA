import functions
#brute force RSA.
#The entire security of RSA relies on the fact that it is difficult to factor large primes. The modulus, which is public, if it is able to be factored into its 2 prime components, you can use the totient function, and then the modular inverse to find the decryption key. If we are able to factor the modulus, we know everything.

m = int(raw_input("Modulus?"))
print(factors(m))
