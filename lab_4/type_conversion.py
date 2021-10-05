#!/usr/bin/env python3

from typing import Text

key='0f351c71c7654ff251de056ea68920cf2d7d49e53ff9174bd303fc04d74e7e69ad9cb9bf56160c2aea960d002b139b6b8f25982fe2e6e9f158a2451944c3f623d19dc425648beceb621f38768abb4f47ad46176b7b04b3c069a0c4da3b0dd3bea96a54b7e4453989f86b55ba8b635b90f944'
keyhex=hex(int(key,16))

def string2Int(message):
    return int(message.encode().hex(),16)

def int2string(int_message):
    return bytes.fromhex(hex(int_message)[2:]).decode()

def string2Hex(message):
     return message.encode().hex()

def hex2String(hex_message):
    return bytes.fromhex(hex_message).decode()

def string2ascii(message):
    return [ord(character) for character in message]

msg='thank you'

print('key----',type(key),key)
print()
print('key en hex----',type(keyhex), keyhex)
print()
result1=string2Int(keyhex)
print('string2Int----',type(result1),result1)
print()
result2=int2string(result1)
print('int2string----',type(result2),result2)
print()
result3=string2Hex(result2)
print('string2Hex----',type(result3),result3)
print()
result4=hex2String(result3)
print('hex2String----',type(result4),result4)
print()
result5=  string2ascii(result4)
print('string2ascii----', type(result5),result5)
print()



Text2='hello world'

def XORStrings(a,b):
    # convert to integers and xor them
    result = int(a, 16) ^ int(b, 16)
    # return result in hex format
    return '{:x}'.format(result)


def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return '%x' % (int(a[:len(b)],16)^int(b,16))
    else:
        return '%x' % (int(a,16)^int(b[:len(a)],16))


print('-----valores para xor ---')
print('key--------',type(result2),result2)
print('Text2------',type(Text2),string2Hex(Text2))
result6=XORStrings(result2,string2Hex(Text2))
print()
print('XORStrings-----',type(result6),result6)
print()
##--------no se puede hacer xor sin convertir a integer
#result8=XORStrings(key,Text2)
#print('XORStrings-----',result8)
#print()
result7=strxor(result2,string2Hex(Text2))
print('strxor-----',type(result7),result7)

def cmp(x, y):
    """
    Replacement for built-in function cmp that was removed in Python 3

    Compare the two objects x and y and return an integer according to
    the outcome. The return value is negative if x < y, zero if x == y
    and strictly positive if x > y.
    """

    return (x > y) - (x < y)
"""
for a in result5:
    compare= cmp (a, 52)
    print(a, 52, '----'),
    print(compare)
"""


