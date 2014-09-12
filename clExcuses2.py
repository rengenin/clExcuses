#!/usr/bin/python
from random import randint

#Read in excuse library
subject = [str(f) for f in file('subjects.lst').read().split("\n")]
verb = [str(f) for f in file('excuses.lst').read().split("\n")]
#excuses = [str(f) for f in file('excuseLibrary.lst').read().split("\n")]

#Draw a random excuse
randomExcuse = subject[randint(0,len(subject) - 1)] + " "  + verb[randint(0,len(verb) - 1)]

#Print random excuse
print randomExcuse
