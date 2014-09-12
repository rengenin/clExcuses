#!/usr/bin/python
from random import randint

#Read in subject and excuses library and put stripped line into list
subject = [line.strip() for line in open('subjects.lst')]
verb = [line.strip() for line in open('excuses.lst')]

#Seperate random Variables for Debugging
randSubject = randint(0, len(subject) - 1)
randExcuse = randint(0, len(verb) - 1) 

#Draw a random excuse
randomExcuse = subject[randSubject] + " "  + verb[randExcuse]

#Debugging Outputs
#print "Subject #: " + str(randSubject) +"; Excuse #: " + str(randExcuse) + "\n"

#Print random excuse
print randomExcuse

#todo:
#figure out why it's printing a blank subject
