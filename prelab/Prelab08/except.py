import glob
import os, math


inputvalue = input('Please enter some values:')
inputll = inputvalue.split()
summ = 0
for a in inputll:
    try:
        summ += float(a)
    except (ValueError):
        pass

print('The sum is:', summ)

