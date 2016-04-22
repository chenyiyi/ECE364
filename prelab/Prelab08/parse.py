import glob
import os, math,sys

def main():

    try:
        f= open(sys.argv[1])
        ll = f.readlines()
        sum = 0
        count = 0
        ss = ''
        for single in ll:
            for value in single.split():
                try :
                    fv = float(value)
                    sum += fv
                    count +=1
                except ValueError:
                    ss += value + ' '
            if(count!=0):
                print(str('%.3f' %(sum/count))+ ' ' + ss)
            else:
                print(ss)
            count = 0
            sum = 0
            ss = ''
        f.close()

    except IndexError:
        print('Usage: parse.py [filename]')
    except IOError:
        print(sys.argv[1], 'is not a readable file.')
    else:
        pass


if __name__ == '__main__':
    main()
