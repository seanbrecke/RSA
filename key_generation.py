from functions import *

def new_mod(upper):

  largeprimelist = largeprime(random.randint(70000,upper))
  p = largeprimelist[0]*largeprimelist[1] #we do number**e mod p to encrypt
#phip = (largeprimelist[0]-1)*(largeprimelist[1]-1)
#e = 65537
#d = inverse(e,phip)
  return int(p)
# print("Encrypt with c = m^65537 mod " + str(p))
# print("Decrypt with m = c^"+str(d)+" mod "+str(p))
