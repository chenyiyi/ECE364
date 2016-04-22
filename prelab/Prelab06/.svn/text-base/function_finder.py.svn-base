import re
import sys
import os

def main():
    if not len(sys.argv) == 2:
        print('Usage: function_finder.py')
    else:
        filename = sys.argv[1]
        if os.path.exists(filename) and os.R_OK:
            with open(filename, 'r') as file_open:
                lines=file_open.readlines()
            for single in lines:
                single = single.strip('\n')
                find = re.match(r'def\s+(\w+)\(([\w=+,:\s]*)', single)
                if(find):
                    print(find.groups()[0])
                    args = re.split(',| ',find.groups()[1])
                    i = 1
                    for a in args:
                        if(a):
                            print('Arg' + str(i) + ': ' + a)
                            i +=1

        else:
            print('Error: Could not read' + filename)


if __name__== "__main__":
    main()