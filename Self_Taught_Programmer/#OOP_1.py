class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l
        
    def print_size(self):
        print('''{} by {} 
              '''.format(self.width,self.length)) 
        
my_shape = Shape(20,25)
#print(my_shape.print_size())     

class Square(Shape):
    def area(self):
        return self.length * self.width
    def print_size(self):
        print(''' I am {} by  {}
              '''.format(self.width,self.length))  

a_square = Square(20,20)
#print(a_square.print_size())      
#print(a_square.area())

class Dog():
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
            
class Person():
    def __init__(self,name):
        self.name = name
caleb = Person('Caleb Belay')        
keanu = Dog('Keanu', 'Pomaranian', caleb )
#print(keanu.owner.name)        

#Challenges

#Challenge 1



        
    
#rect_1 = Rectangle(15,15)
#sqr_1 = Square(15)
#print(sqr_1.calculate_perimeter())
#print(rect_1.calculate_perimeter())

class Shape():
   
    def what_am_i(self):
        print('I am a shape')    
           
class Rectangle(Shape):
    pass

class Square(Shape):
    pass

x_rect = '''    def __init__(self,l,w):
        self.length = l
        self.width = w
    def calculate_perimeter(self):
        return (self.length + self.width)*2
'''
    
x_sqr = '''     def __init__(self,s): 
        self.side = s
    def calculate_perimeter(self):
        return 4 * self.side
    def change_size(self,change):
        self.side += change
 '''   
         
class Horse():
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
class Rider():
    def __init__(self,name):
        self.name = name
        
GR = Rider('Ghost Rider')
Butter = Horse('ButterFly', 'Stallein' , GR)
print(Butter.owner.name)

                         