import math
from sympy import totient as eulerFunction
import random
import string


# returns Co-prime integer to fn, the only integer that shares a divisor of 1 with fn
def generateE(fn):
    e = random.randint(2,fn - 1) #Return a random int in the range(1,fn)
    #TODO: more efficient 
    while math.gcd(e, fn) != 1: #while the numbers have a common divider
        e = random.randint(2,fn - 1)
    return e
#
def generateD(fn, e):
    k = 2
    d = round((k * fn + 1) / e)
    while (((k * fn + 1) % e) != 0 or d == e) :
        k = k + 1
        d = round((k * fn + 1) / e)
    return d


#
def encrypt(plainLetter,e,mod): 
    return math.pow(plainLetter,e) % mod 

#
def decrypt(encryptedLetter,privateKey,publicMod): 
    return math.pow(encryptedLetter,privateKey) % publicMod



if __name__ == '__main__': 
    message = str(input("Enter the message to be encrypted: "))
    #step 1:
    p = 2
    q = 7
    #step 2:
    n = p*q
    #step 3:
    Fn = (p-1)*(q-1)
    #step 4:
    e = 5 
    #generateE(Fn) #
    d = generateD(Fn,e) # to get e the attacker needs to get p and q and that is impossible 
    
    publicKey = [Fn,n]
    privateKey = d

    print(list([ord(letter) - 96 for letter in message]))
    # for each letter I get ascii value encrypt it then convert back to ascii and add to a list  
    encryptedMessage = list([(int(encrypt((ord(letter) - 96), e, n))) for letter in message])
    print(encryptedMessage)
    decryptedMessage = list([int(decrypt(letter,privateKey,n)) for letter in encryptedMessage])
    print(decryptedMessage)

    temp  = list([(int(encrypt((ord(letter) - 96), e, n))) for letter in string.ascii_lowercase])
    print(list([(ord(letter) - 96) for letter in string.ascii_lowercase]))
    print(temp)
    print(list([(int(decrypt(letter,privateKey,n))) for letter in temp]))