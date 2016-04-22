import re,sys

def idIsAcceptable(ver_id):
    valid = re.search(r'[A-Za-z0-9_]', ver_id[0])
    if valid is None:
        return False
    else:
        a = re.search(r'[^A-Za-z0-9_]', ver_id)
        if a is None:
            return True
        else:
            return False

def processSingle(ver_assignment):
    a= re.search(r'\.\w+\(\w+\)', ver_assignment)
    if a is None:
        raise ValueError
    else:
        b = re.findall(r'\w+', a.group())
        return tuple(b)


def processLine(ver_line):
    a1 = re.search(r'\)\)', ver_line)
    a2 = re.search(r'\) \)', ver_line)
    if a1 is None and a2 is None:
        raise ValueError
    a3 = re.search(r'\(\(', ver_line)
    a4 = re.search(r'\)\)\)', ver_line)
    a5 = re.search(r'\?', ver_line)
    a6 = re.search(r'%', ver_line)
    a7 = re.search(r'\) \)\)', ver_line)
    if a3 is not None or a4 is not None or a5 is not None or a6 is not None or a7 is not None:
        raise  ValueError

    b = ver_line.split(',')
    c= []
    for single in b:
        c.append(processSingle(single))
    d = re.findall(r'\w+', ver_line)
    if len(d) != (len(c)*2 +2):
        raise ValueError
    else:
        return d[0],d[1],tuple(c)