'''                         
Fizzbuzz
CIS 210 F18 Project 3-1
Author: Hans Prieto

Credits: N/A

Implements fizzbuzz: starts at 1, and counts up to
some number, n. Prints either the number, prints "fizz",
prints "buzz", or prints "fizzbuzz."
'''

def fb(n):                  
    '''(int) -> <for loop>

    Starts at 1, and counts up to some
    number, n.

    If the number is divisible by
    3, it prints "fizz".

    If the number is
    divisible by 5, it prints "buzz".

    If them number is divisible by both 3 and 5, it
    prints "fizzbuzz".

    prints "Game Over!" at the end.

    None value is returned.
    
    >>> fb(15)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    Game Over!

    >>> fb(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    Game Over!
    '''
    
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0: #Prints "fizzbuzz" if number is divisible by both 3 and 5. 
            print("fizzbuzz") 
        elif i % 3 == 0: #Prints "fizz" if number is divisible by 3 only.    
            print("fizz")  
        elif i % 5 == 0: #Prints "buzz" if number is divisible by 5 only.
            print("buzz")
        else: #Just prints the number if the number is not divisible by 3 or 5.      
            print(i)
            
    print("Game Over!") #Prints "Game Over!" after the for loop is executed.

    return None #None value is returned.                
                
fb(15)
        
