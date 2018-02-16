
#Python Chapter 9 Exercise 5
#Armando Crews
#Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from 
#(i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

file = input('Enter file name: ')



if len(file) < 1 : file = 'mbox-short.txt'

try :
    hand = open(file)
except :
    print ('Could not open',file)
    exit()



school = dict()




for line in hand :
    if not line.startswith('From ') : continue
    words = line.split()
    words = words[1].split('@')
    addr = words[1]
    school[addr] = school.get(addr, 0) + 1




print (school)
