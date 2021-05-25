import string
import random
import hashlib
from hashlib import sha256

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )

    print(k) #Check to see what K number if
    #Collision finding code goes here
    hash_letters = string.ascii_letters + string.digits + string.punctuation
    print(hash_letters)

    x = ''.join(random.choice(hash_letters) for i in range(12)).encode('utf-8')

    y = ''.join(random.choice(hash_letters) for i in range(12)).encode('utf-8')

    while True:
        #Define X and Y
        sha256X = sha256(x).hexdigest()
        sha256Y = sha256(y).hexdigest()
        #Convert to bin int
        sha256X = bin(int(sha256X, 16))[2:].zfill(256)
        sha256Y = bin(int(sha256Y, 16))[2:].zfill(256)

        if sha256X[256-k:256] == sha256Y[256-k:256]:
            #if condition is true BREAK and exit
            break
        #Random X
        x = ''.join(random.choice(hash_letters) for i in range(12)).encode('utf-8')
        #Random Y
        y = ''.join(random.choice(hash_letters) for i in range(12)).encode('utf-8')

    print(x, y) #check output

    return( x, y )
