# Loops
#Caleb = 'Caleb'
#for character in Caleb:
#    print(character)
import math, random
# lowwercase all of the list items
Shop = ['EGGS', 'MILK','BREAD']
k = 0
for k,  Man in enumerate(Shop):
    Swap = Shop[k]
    Swap = Swap.lower()
    Shop[k] = Swap
   
#print(Shop)
#i = 0
#i = random.randint(1,10)

Names_1 = ['Caleb' , 'Timmy','Simon' , 'MK']
Surnames_1 = [' Belay' , ' Ojo' , ' Issa' , ' Lebese']
Full_Names = []

for i in Names_1:
    for j in Surnames_1:
        Full_Names.append(i + j)
#print(Full_Names)        
     
#Challenges

 #Challenge #1
List1 = ['The Walking Dead', 'Entourage' ,'The Sopranos' , 'The Vampire Diares'] 
#for show in List1:
    #print(show)

 #Challenge #2
#for i in range(25,51):
    #print(i) 
    
 #Challenge #3
#o = 0 
#for i in List1:
    #print(i, str(o))
    #o += 1 
    
 #Challenge #4   
#while True:
#    a = (input('Geuss a number!'))
#    if a == '1':
#        print('You got the number!')
#    if a != '1':
#        print('You geussed wrong!')    
#    if a == 'q':
#     break 
 
 #Challenge #5
#First_List = [8,19,148,4]
#Secind_List = [9,1,33,83]
#mul = []




