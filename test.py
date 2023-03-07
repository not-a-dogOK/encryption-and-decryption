from RSA import encrypt
from RSA import decrypt
from RSA import generateD
from RSA import generateE
import string

# in the real world p and q are 2 large prime numbers, to save resources and time I used smaller ones
p = 17
q = 47
# preparing the public key:
n = p*q
Fn = (p-1)*(q-1)
e = generateE(Fn)
d = generateD(Fn, e)
# to get e the attacker needs to get p and q and that is impossible, thus d is the private key
privateKey = d

temp  = list([(int(encrypt((ord(letter) - 96), e, n))) for letter in string.ascii_lowercase])
print(list([(ord(letter) - 96) for letter in string.ascii_lowercase]))
print(temp)
print(list([(int(decrypt(letter,privateKey,n))) for letter in temp]))