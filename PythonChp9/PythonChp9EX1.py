
#Python Chapter 9 Exercise 1
#Armando Crews 
#Exercise 1: Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
#It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary


ndict = dict()
count = 0
fhand = open('words.txt')

inp = fhand.read()
inp = inp.split() 

for word in inp :
    count = count + 1
    ndict[word] = [count]



print ('cat') in ndict
print ('and') in ndict
print ('dog') in ndict


