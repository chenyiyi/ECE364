import glob
import os, math

def find_median(fir, sec):
    length = len(fir)+len(sec)
    merlist = fir + sec
    merlist.sort()
    mednumber = math.floor((length-1)/2)
    return (merlist[mednumber], merlist)



def main():
    first = input('Enter the first list of numbers:')
    second = input('Enter the second list of numbers:')
    firlist = list(map(int,first.split()))
    seclist = list(map(int,second.split()))
    med, medlist = find_median(firlist, seclist)
    print('First list:',firlist)
    print('Second list:', seclist)
    print('Merged list:', medlist)
    print('Median:', med)

if __name__ == "__main__":
    main()
