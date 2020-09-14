'''                         
Binary Encoding and Decoding
CIS 210 F18 Project 4-2
Author: Hans Prieto

Credits: N/A

Encode and decode decimal to binary
representation of numbers
'''

def dtob(n):
    ''' (int) -> str
    converts a non-negative integer
    to its binary representation

    >>> dtob(27)
    '11011'

    >>> dtob(0)
    '0'

    >>> dtob(1)
    '1'
    '''
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    elif n % 2 == 1:
        return dtob(n // 2) + '1'
    else:
        return dtob(n // 2) + '0'
import doctest
print(doctest.testmod())
    
def btod(b):
    ''' (str) -> int
    converts a string of 0s and
    1s to a non-negative integer,
    which is the decimal representation
    of that string

    >>> btod('0000')
    0

    >>> btod('1101')
    13

    >>> btod('111111')
    63
    '''
    decimal = int(b, 2)
    print(decimal)
import doctest
print(doctest.testmod())
    
def main():
    ''' binary encoding and decoding program driver'''
    integer = int(input('Enter integer: '))
    binary = dtob(integer)
    print(binary)
    decimalValue = btod(binary)
    print(decimalValue)
main()
