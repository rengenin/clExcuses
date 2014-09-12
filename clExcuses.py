#!/usr/bin/python
from random import randint

#Read in excuse library
excuses = [str(f) for f in file('excuseLibrary.lst').read().split("\n")]

#Draw a random excuse
randomExcuse = excuses[randint(0,len(excuses) - 1)]

#Print random excuse
print randomExcuse
