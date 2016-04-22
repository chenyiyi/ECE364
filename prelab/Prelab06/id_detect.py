import re

def main():
    with open('addys.in', 'r') as open_file:
        lines=open_file.readlines()
        for ll in lines:
            h = re.match(r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])){3}:(\d+.*)',ll)
            if(h):
                if not h.group(4).isdigit():
                    print(h.group() + ' -Invalid Port Number')
                elif not int(h.group(4)) <= 32767:
                    print(h.group() + ' -Invalid Port Number')
                else:
                    if((int(h.group(4))) < 1024):
                        print(h.group() + ' - Valid(root privileges required)')
                    else:
                        print(h.group() + ' - Valid')
            else:
                 print(ll + ' - Invalid IP Address')


if __name__== "__main__":
    main()
