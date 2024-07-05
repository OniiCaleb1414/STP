import csv, math, os


with open('File_1', 'w+') as F:
     F.write('This must display')


my_list = list()

with open('File_1', 'r') as F1:
     my_list.append(F1.readline())

#print(my_list) 

with open('File_2.csv', 'w', newline='') as F:
     w = csv.writer(F, delimiter=',')
     w.writerow(['one', 'two', 'three'])
     w.writerow(['four', 'five', 'six'])

with open('File_2.csv', 'r') as F:
     r = csv.reader(F, delimiter=',')
     #for row in r:
         #print(' '.join(row))     
         
         
#Challenges

#1

#Challenges
#1
#with open('Text1', 'r') as t:
#    print(t.readline())

#2
#word = input('Whats the word???')
#with open('Text2', 'w+') as w:
#    w.write(word)

#3
import csv

shows = [['Top Gun', 'Risky Business', 'Minority Reports'],
         ['Titanic', 'The Revenant', 'Inception'],
         ['Training Day', 'Man on Fire ', 'Flight']]

with open('Shows.csv', 'w', newline='') as s:
    w = csv.writer(s, delimiter=',')
    for row in range(0,3):
     w.writerow(shows[row])