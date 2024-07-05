#Challenges

#Challenge 1
import math
class Apple:
    def __init__(self, a,b,c,d):
        self.name = a
        self.size = b
        self.color = c
        self.som = d
        
#Challenge 2        
class Circle:
    def __init__(self, a):
        self.radius = a
    
    def area(self,a):
        self.radius = a
        return math.pi * math.pow(self.radius,2)         
            
#c_1 = Circle(23)
#print(c_1.area(23))        

#Challenge 3

class Triangle:
    def __init__(self,h,b):
        self.height = h
        self.base = b
    
    def area(self):
        return 0.5 * self.height * self.base
    
#tri = Triangle(5,7)
#print(tri.area())             

#Challenge 4

class Hexagon:
    def __init__(self, s):
        self.side = s
        
    def calculate_perimter(self):
        return self.side * 6
    
hex_1 = Hexagon(6)
print(hex_1.calculate_perimter())        