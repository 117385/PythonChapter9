
#Python Chapter 9 Exercise 4
#Armando Crews 
#Exercise 4: Add code to the above program to figure out who has the most messages in the file.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
text = handle.read()


senders = dict()
for line in handle:
    if not line.startswith("From:"):continue
    line = line.split()
    line = line[1]
    senders[line] = senders.get(line, 0) +1

bigcount = None
bigword = None
for word,sender in senders.items():
    if bigcount == None or sender > bigcount:
        bigword = word 
        bigcount = sender 

print (bigword, bigcount)