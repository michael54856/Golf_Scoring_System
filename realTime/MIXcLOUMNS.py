import sys
import os
def mixColumns(a, b, c, d):
    printHex(gmul(a, 2) ^ gmul(b, 3) ^ gmul(c, 1) ^ gmul(d, 1))
    printHex(gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1))
    printHex(gmul(a, 1) ^ gmul(b, 1) ^ gmul(c, 2) ^ gmul(d, 3))
    printHex(gmul(a, 3) ^ gmul(b, 1) ^ gmul(c, 1) ^ gmul(d, 2))
    print()

def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a

def printHex(val):
    return print('{:02x}'.format(val), end=' ')

# test vectors from https://en.wikipedia.org/wiki/Rijndael_MixColumns#Test_vectors_for_MixColumn()


# example from question
mixColumns(0xE0, 0xB4, 0x52, 0xAE) # 0x22 0x77 0x00 0x55 = 34 119 0 85
os.system("pause")