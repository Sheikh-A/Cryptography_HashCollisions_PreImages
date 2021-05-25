

# import hashlib
# import os
# from hashlib import sha256
# import random

# def hash_collision(k):

#     if not isinstance(k,int):
#         print( "hash_collision expects an integer" )
#         return( b'\x00',b'\x00' )
#     if k < 0:
#         print( "Specify a positive number of bits" )
#         return( b'\x00',b'\x00' )

#     #Collision finding code goes here
#     x = b'\x00'
#     y = b'\x00'
#     x = str(random.random()).encode('utf-8')
#     x_bits = bin(int(sha256(x).hexdigest(),16))
#     i = 500
#     while (True):
#         y = str(i).encode('utf-8')
#         y_bits = bin(int(sha256(y).hexdigest(),16))
#         if x_bits[-k:] == y_bits[-k:]:
#             break
#         i+=1
#     return( x, y)

# a = int(input ("input an integer: "))
# print (hash_collision(a))

# import hashlib
# import os
# import math

# def hash_collision(k):
#     if not isinstance(k,int):
#         print( "hash_collision expects an integer" )
#         return( b'\x00',b'\x00' )
#     if k < 0:
#         print( "Specify a positive number of bits" )
#         return( b'\x00',b'\x00' )

#     #Collision finding code goes here
#     while True:
#         size = int(math.log(pow(2, k), 255)) + 1
#         x = os.urandom(size)
#         y = os.urandom(size)

#         bi_hash1 = bin(int(hashlib.sha256(x).hexdigest(), 16))
#         bi_hash2 = bin(int(hashlib.sha256(y).hexdigest(), 16))
#         if bi_hash1[-k:] == bi_hash2[-k:]:
#             return (x, y)

import hashlib
import os
from random import random

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )

    #Collision finding code goes here
    x = str(random()).encode('utf-8')
    y = str(random()).encode('utf-8')

    x_hash_binary = bin(int(hashlib.sha256(x).hexdigest(), 16))
    y_hash_binary = bin(int(hashlib.sha256(y).hexdigest(), 16))

    while y_hash_binary.endswith(x_hash_binary[len(x_hash_binary)-k:]) == False:
        x = str(random()).encode('utf-8')
        y = str(random()).encode('utf-8')

        x_hash_binary = bin(int(hashlib.sha256(x).hexdigest(), 16))
        y_hash_binary = bin(int(hashlib.sha256(y).hexdigest(), 16))

    return( x, y )
