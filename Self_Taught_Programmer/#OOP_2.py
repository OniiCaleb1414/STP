class Fill():
    def __init__(self, l , m):
        self.cream = l
        self.lemon = m
    def __repr__(self):
        return self.cream     


f_1 = Fill('Caleb', 'lime')
print(f_1)

class Always():
    def __init__(self, number):
        self.n = number
    def __add__ (self,other):
        return abs(self.n + other.n)
    def __sub__(self,other):
        return abs(self.n - other.n)
try:
  x = Always(-20)
  y = Always(10)
  print(x + y)
  print(x - y)
except: print(Exception)


class Presidents():
    def __init__(self, name):
        self.n = name
        
def Check_Pres(ob1,ob2):
    return ob1 is ob2
        
Obama = Presidents('Barack Obama')
Trump = Presidents('Donald Trump')
Pres_2016 = Obama

print(Obama is Pres_2016)
print(Obama  is Trump)    

def Check(num):
    if num is None:
        print(str(num)  + ' is Empty :( ')
    else: 
        print('The Number is not empty!')
try:
   x = 10
   y = None

   print(Check(x))
   print(Check(y))   
except:
    print(Exception)
            
#Challenges 

#Challenge 1

class Sqaure1():
    sqaure_list = []
    def __init__(self, l, w):
        self.length = l
        self.width = w
        self.sqaure_list.append((self.length,self.width))

#Challenge 2
class Sqaure():
    def __init__(self,l):
        self.length = l
    def __repr__(self):
        return '''{} by {} 
    '''.format(self.length,self.length)
            
#Challenge 3

      
              