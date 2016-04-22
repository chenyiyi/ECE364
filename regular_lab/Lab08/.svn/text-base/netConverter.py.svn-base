import re,sys

from HardwareTasks import *

def verilog2vhdl(ver_line):
    try:
        ll = list(processLine(ver_line))
        asslist = ll[2]
        ss = ll[1] + ': ' + ll[0] + ' PORT MAP('
        for single in asslist:
            sin = list(single)
            ss +=sin[0]+'=>'+sin[1]+', '
        ss= ss[:-2]
        ss+=');'
        return ss
    except:
        return 'Error: Bad Line.'
    finally:
        pass


def convertNetlist(sourceFile, targetFile):
    s = open(sourceFile, 'r')
    t = open(targetFile, 'w')
    ll = s.readlines()
    uu =[]
    for single in ll:
        uu.append(verilog2vhdl(single))
    res = '\n'.join(uu)
    t.write(res)