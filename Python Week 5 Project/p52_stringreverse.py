'''                         
String Reversal
CIS 210 F18 Project 5-2
Author: Hans Prieto

Credits: N/A

Write and implement iterative and
recursive algorithms to reverse a string.

'''

def strReverseR(s):
    '''
    (str) -> str

    Reverses a string using
    an recursive implementation

    >>> strReverseR('hello, world')
    'dlrow ,olleh'
    
    >>> strReverseR('python')
    ''nohtyp'
    '''
    
    if len(s) == 0:
        return s
    else:
        return strReverseR(s[1:]) + s[0]

def strReverseI(s):
    '''
    (str) -> str

    Reverses a string using
    an iterative implementation

    >>> strReverseI('hello, world')
    'dlrow ,olleh'
    
    >>> strReverseI('python')
    ''nohtyp'
    '''
    
    revS = ''
    index = len(s)
    while index > 0:
        revS += s[index -1]
        index = index - 1
    return revS

#def main():
    '''
    Uses the input function to
    get a string

    Calls strReverseR to reverse the
    string

    Prints the vaule returned by
    strReverseR

    Calls strReverseI to reverse
    the value returned by strTReverseR
    back to the original string

    prints the value returned by
    strReverseI
    '''
    #string = input("enter string: ")
    #reverseS = strReverseR(string)
    #print (reverseS)
    #originalS = strReverseI(reverseS)
    #print (originalS)

#main()
