import math
from sympy import totient as eulerFunction
import random
import egcd

# returns Coprime integer to eulerFuncOfn, the only integer that shares a divisor of 1 with eulerFuncOfn
def generateE(eulerFuncOfn):
    e = random.randint(1,eulerFuncOfn) #Return a random int in the range(1,eulerFuncOfn)
    while math.gcd(e, eulerFuncOfn) != 1:
        e = random.randint(1,eulerFuncOfn)
    return e
#
def encrypt(message): 
    return math.pow(message,publicKey[1]) % publicKey[0] 

#
def decrypt(encryptedMessage): 
    return math.pow(encryptedMessage,d) % publicKey[0] 



if __name__ == '__main__': 
    message = str(input("Enter the message to be encrypted: "))
    #step 1:
    p = 11
    q = 7
    #step 2:
    n = p*q
    #step 3:
    En = eulerFunction((p-1)*(q-1))
    #step 4:
    e = generateE(En)

    global publicKey #this is what transmitted and public so accordingly I make it public in the program
    publicKey = [n,e]
    #d = egcd()
    # for each letter I get ascii value encrypt it then convert back to ascii and add to a list  
    encryptedMessage = list([chr(int(encrypt((ord(letter))))) for letter in message])
    print(encryptedMessage)