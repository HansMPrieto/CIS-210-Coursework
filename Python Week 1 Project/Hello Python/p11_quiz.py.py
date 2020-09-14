
''' 
CIS 210 STYLE
CIS 210 F18 Project 1-1

Author: Hans Prieto

Credits: [acknowledgements or N/A]

Add docstrings to Python functions that implement quiz 1 pseudocode.
(See p11_cricket for examples of functions with docstrings.)
'''

def q1(onTime, absent):
    '''
    Return Hello based on whether onTime is true.
    Return 'Is anyone there?' based on absent is true
    Return 'Better late than never.' if onTime and absent
    are both false. 
                            #EXAMPLES OF USE
    >>> q1(True, False)
    Hello
    >>> q1(False, True)
    Is anyone there
    >>> q1(False, False)
    Better late than never
    '''
    if onTime:
        return('Hello!')
    elif absent:
        return('Is anyone there?')
    else:
        return('Better late than never.')

def q2(age, salary):
    '''
    Determines wheter or not someone is a dependent child.
    A dependent child is someone who is under the age of 18,
    and does not earn $10,000 or more a year.
        #Examples of Use
    >>> q2(17, 9000)
    True
    >>> q2(19, 11000)
    False
    '''
    return (age < 18) and (salary < 10000)

def q3():
    '''boolean -> int
    Determines a result based on the values
    of p and q
    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

def q4(balance, deposit):
    ''' 
    Return balance based on amount
    of deposit
                            #EXAMPLES OF USE
    >>> q4(200, 10)
    300
    >>> q4(150, 5)
    200
    >>> q4(160, 8)
    240
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

def q5(nums):
    '''
    Counts the non-negative numbers in a list of numbers.
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

def q6():
    '''
    docstring - type contract, brief description including
    returned value, side effects (if any), and examples of use -
    goes here

    You will need to fix the bug in the code, too!
    '''
    i = 0
    p = 1
    while i < 4:
        i = 1
        p = p * 2
        i += 1

    return p
