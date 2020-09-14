'''
Testing Functions
CIS 210 F18 Project 6-1

Author: Hans Prieto
Credits: [N/A]

Write a function to test the string reverse
functions from Project 5-2

Practice with
- software development - testing
- functions as parameters
'''

import p52_stringreverse as p5

def test_reverse(f):
    '''
    function -> None

    Calls parameter, f, a function
    (either strReverseR or strReverseI)
    repeatedly for a series of test cases,
    and compares the result returned by either
    strReverseR or strReverseI to the expected
    result.

    >>> test_reverse(p5.strReverseR)
    Checking strReverseR('')...its value '' is correct!
    Checking strReverseR('a')...its value 'a' is correct!
    Checking strReverseR('aaaa')...its value 'aaaa' is correct!
    Checking strReverseR('abc')...its value 'cba' is correct!
    Checking strReverseR('hello')...its value 'olleh' is correct!
    Checking strReverseR('racecar')...its value 'racecar' is correct!
    Checking strReverseR('testing123')...its value '321gnitset' is correct!
    Checking strReverseR('a')... Error has wrong value a, expected b.
    Checking strReverseR('#CIS 210')...its value '012 SIC#' is correct!

    >>> test_reverse(p5.strReverseI)
    Checking strReverseI('')...its value '' is correct!
    Checking strReverseI('a')...its value 'a' is correct!
    Checking strReverseI('aaaa')...its value 'aaaa' is correct!
    Checking strReverseI('abc')...its value 'cba' is correct!
    Checking strReverseI('hello')...its value 'olleh' is correct!
    Checking strReverseI('racecar')...its value 'racecar' is correct!
    Checking strReverseI('testing123')...its value '321gnitset' is correct!
    Checking strReverseI('a')... Error: has wrong value 'a', expected 'b'.
    Checking strReverseI('#CIS 210')...its value '012 SIC#' is correct!
    '''

    #test cases for test_reverse function
    testCases = (('', ''), ('a', 'a'),
         ('aaaa', 'aaaa'),('abc', 'cba'),('hello', 'olleh'),
         ('racecar', 'racecar'),('testing123', '321gnitset'),
         ('a', 'b'),('#CIS 210', '012 SIC#'))

    for case in testCases:
        #tests the reverse function for strReverseR
        if f == p5.strReverseR:
            if f(case[0]) == case[1]:
                #states that the test case is correct for strReverseR
                print("Checking strReverseR" + "('" + case[0] +
                "')...its value '" + case[1] + "' is correct!")
            else:
                #states that the test cass is incorrect for strReverseR
                print("Checking strReverseR" + "('" + case[0] +
                "')... Error has wrong value " + case[0] + ", expected "
                + case[1] + ".")
                
        #tests the reverse function for strReverseI
        elif f == p5.strReverseI:
            if f(case[0]) == case[1]:
                #states that the test case is correct for strReverseI
                print("Checking strReverseI" + "('" + case[0] +
                "')...its value '" + str(case[1]) + "' is correct!")
            else:
                #states that the test case is incorrect for strReverseI
                print("Checking strReverseI" + "('" + case[0] +
                "')... Error: has wrong value '" + case[0] + "', expected '"
                + case[1] + "'.")

def main():
    '''calls string reverse test func 2 times'''
    test_reverse(p5.strReverseR)
    print()
    test_reverse(p5.strReverseI)
    return None

main()
            
            
              
    
