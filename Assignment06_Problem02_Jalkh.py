# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:12:38 2024

@author: marcj
Problem 02
"""
# base class computes area and perimiter of one of the most basic shapes,
# which is not mentioned in prompt, a 1x1 square
class shape:
    def __init__(self,side): # side arg will be used as arg for later shapes
        self.side=side
    def area(self):
        area=self.side**2
    def perimiter(self):
        perimiter=self.side*4

# respective classes and methods for each shape

class circle(shape):
    def area(self):
        area=3.14*self.side**2 #here side arg inherited and used as radius
        print(f"Area of circle of radius {self.side} >>> {area}")
    def perimiter(self):
        perimiter=3.14*self.side*2
        print(f"Perimiter of circle of radius {self.side} >>> {perimiter}")

class rectangle(shape):
    def area(self,side2):
        area=self.side*side2 #here side arg inherited and used as either width or length
        print(f"Area of rectangle of sides {self.side}, {side2} >>> {area}")
    def perimiter(self,side2):
        perimiter=2*self.side+2*side2
        print(f"Perimiter of rectangle of sides {self.side}, {side2} >>> {perimiter}")

class triangle(shape):
    def area(self,height):
        area=(self.side*height)/2 #here side arg inherited and used as base of height of triangle
        print(f"Area of triangle of side {self.side} and height from base to summit {height} >>> {area}")
    def perimiter(self,side2,side3):
        perimiter=self.side+side2+side3 #here side arg inherited and used as triangle side
        print(f"Perimiter of triangle of sides {self.side}, {side2}, {side3} >>> {perimiter}")
        
def main():
    # circle demo
    shape1=circle(3)
    shape1.area()
    shape1.perimiter()
    # rectangle demo
    shape2=rectangle(3)
    shape2.area(2)
    shape2.perimiter(2)
    # triangle demo
    shape3=triangle(5)
    shape3.area(2)
    shape3.perimiter(5,5)
    #NOTE FOR TRIANGLE: 
    # the triangle whose area is computed in the area method 
    # is not the same as the one whose perimeter is computed in the perimiter method
    # the height from base affects the sides and would not correlate

main()
       