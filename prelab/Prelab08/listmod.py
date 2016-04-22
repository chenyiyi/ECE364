from lists import find_median

first = input('Enter the first list of numbers:')
second = input('Enter the second list of numbers:')
firlist = list(map(int,first.split()))
seclist = list(map(int,second.split()))
med, medlist = find_median(firlist, seclist)
print('First list:',firlist)
print('Second list:', seclist)
print('Merged list:', medlist)
print('Median:', med)