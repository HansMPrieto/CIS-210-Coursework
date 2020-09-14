'''                          # FILE HEADER
Draw Flower
CIS 210 F18 Project 2

Author: Hans Prieto

Credits: [N/A]

Use Python to draw a flower-like shape
'''

from turtle import *

def drawPolygon(sideLength, numSides):
    '''(int, int) -> <polygon graphic>

    draws a polygon with a certain number
    of sides.
    
    >>> drawPolygon(4, 4)
    <Square graphic>
    '''
    
    turnAngle = 360/numSides
    for i in range(numSides):
        forward(sideLength)
        right(turnAngle)

def drawFlower(numSquares):
    ''' int -> <flower graphic>

    draws a flower with a certain
    number of squares.

    >>> drawFlower(25) -> <Flower Graphic>
    '''
    
    for i in range(0, numSquares):
        drawPolygon(100, 4)
        left(360/numSquares)

def main():
    ''' function -> <flower graphic>

    Calls the function drawFlower to
    draw a flower with 25 squares. The speed
    in which the flower is drawn is set to 5, and
    the color of the flower is set to green. 

    >>> main() -> <Flower Graphic>
    '''

    speed(5)
    color('green')
    drawFlower(25)

main()

    




    
