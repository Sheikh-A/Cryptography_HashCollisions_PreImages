# import hashlib
# import random
# import string

# def hash_collision(k):
#     if not isinstance(k, int):
#         print("hash_collision expects an integer")
#         return (b'\x00', b'\x00')
#     if k < 0:
#         print("Specify a positive number of bits")
#         return (b'\x00', b'\x00')
#     # Collision finding code goes here

#     last_k_in_X = "1"
#     last_k_in_Y = "0"
#     while last_k_in_X != last_k_in_Y:
#         # create string
#         str1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
#         str2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

#         encoded1, encrypted1 = encode_and_encrypt(str1)
#         encoded2, encrypted2 = encode_and_encrypt(str2)

#         # convert to binary
#         x = hex_to_binary(encrypted1, 16)
#         y = hex_to_binary(encrypted2, 16)

#         # cut and keep only the last k digits binary
#         last_k_in_X = x[-k:]
#         last_k_in_Y = y[-k:]

#     return encoded1, encoded2


# def encrypt_string(hash_string):
#     sha_signature = \
#         hashlib.sha256(hash_string.encode()).hexdigest()
#     return sha_signature


# def hex_to_binary(hex_number: str, num_digits: int = 8) -> str:
#     return str(bin(int(hex_number, 16)))[2:].zfill(num_digits)


# def main():
#     print(hash_collision(8))


# def encode_and_encrypt(string):
#     encoded = string.encode()
#     result = hashlib.sha256(encoded)
#     result_hex = result.hexdigest()
#     return encoded, result_hex


# if __name__ == "__main__":
#     main()

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

import hashlib
import os
import math

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )

    #Collision finding code goes here
    while True:
        size = int(math.log(pow(2, k), 255)) + 1
        x = os.urandom(size)
        y = os.urandom(size)

        bi_hash1 = bin(int(hashlib.sha256(x).hexdigest(), 16))
        bi_hash2 = bin(int(hashlib.sha256(y).hexdigest(), 16))
        if bi_hash1[-k:] == bi_hash2[-k:]:
            return (x, y)
