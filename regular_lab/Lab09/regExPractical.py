import re

def getAddress(sentence):
    final = re.search(r'[a-hA-H0-9]{1,2}[:-]{1}[a-hA-H0-9]{1,2}[:-]{1}[a-hA-H0-9]{1,2}[:-]{1}[a-hA-H0-9]{1,2}[:-]{1}[a-hA-H0-9]{1,2}[:-]{1}[a-hA-H0-9]{1,2}', sentence)
    if final is not None:
        return final.group()
    return None



def getElements(fullAddress):
    final = re.findall(r'[a-zA-Z0-9.]{1,}', fullAddress)
    if (final[0] == 'https' or final[0] == 'http') and (len(final) == 4) and ('.' not in final[2]) and ('.' not in final[3]):
        return final[1], final[2], final[3]
    return None



def getSwitches(commandline):
    a = re.findall(r'[+\\]{1}[a-z]{1,}\s{1,}[a-zA-Z0-9.:/]{1,}', commandline)
    final = []
    for element in a:
        c = re.findall(r'[a-zA-Z0-9.:/]{1,}', element)
        final.append((c[0], c[1]))
    final.sort()
    return final