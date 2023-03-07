import math
import random

# returns Co-prime integer to fn, the only integer that shares a divisor of 1 with fn, which


def generateE(fn):
    e = random.randint(2, fn - 1)  # Return a random int in the range(1,fn)
    # TODO: more efficient
    while math.gcd(e, fn) != 1:  # while the numbers have a common divider
        e = random.randint(2, fn - 1)
    return e

# generate a private key using q and p in the form of fn.
# thus only the one how has q and p can generate


def generateD(fn, e):
    k = 2
    d = round((k * fn + 1) / e)  # deviation in python returns a double
    while (((k * fn + 1) % e) != 0 or d == e):
        k = k + 1
        d = round((k * fn + 1) / e)
    return d


# takes letter,e,mod which are part of the public key and encrypts according to rsa formula
def encrypt(plainLetter, e, mod):
    return pow(plainLetter, e) % mod

# takes letter mod (public key) and private key and decrypts according to rsa formula
def decrypt(encryptedLetter, privateKey, mod):
    return pow(encryptedLetter, privateKey) % mod

if __name__ == '__main__':
    message = str(input("Enter the message to be encrypted: "))
    
    # in the real world p and q are 2 large prime numbers, to save resources and time I used smaller ones
    p = 5
    q = 7
    # preparing the public key:
    n = p*q
    Fn = (p-1)*(q-1)
    e = generateE(Fn)
    # that how a public key may look like
    global publicKey
    publicKey = [e, n]
    d = generateD(Fn, e)
    # to get e the attacker needs to get p and q and that is impossible, thus d is the private key
    privateKey = d

    # original message in decimal
    print(list([ord(letter) - 96 for letter in message]))
    # for each letter I get ascii value encrypt it and add to a list
    encryptedMessage = list([(int(encrypt((ord(letter) - 96), e, n))) for letter in message])
    print(encryptedMessage)
    # for each letter I decrypt it using the private key and add to a list
    decryptedMessage = list([int(decrypt(letter, privateKey, n)) for letter in encryptedMessage])
    print(decryptedMessage)
