'''
CIS 210 STYLE
CIS 210 F18 PROJECT 1-2

Author: Hans Prieto

Credits: [N/A]
'''


def convert(i, j, k):
    '''
    Combines 3 digits to create one number.
                    "EXAMPLES OF USE
    >>> convert(1, 2, 3)
    123
    >>> convert(3, 6, 5)
    365
    >>> convert(6, 7 9)
    679
    '''
    if(i >= 0) and (k <= 9):
        number = int(str(i) + str(j) + str(k))
    return number

def add_digits(n):
    '''str -> int
    Returns the sum of digits in a 3 digit number.
                #EXAMPLES OF USE
    >>> add_digits(123)
    6
    >>> add_digits(369)
    18
    >>> add_digits(987)
    24
    '''
    number = str(n)
    sum = 0
    for i in range(0, len(number)):
        sum += int(number[i])
    return sum

    
    
    
    
    
        
    
    

