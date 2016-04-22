from os.path import join
import unittest
from numpy import ndarray as nmat
import numpy
from scipy.misc import *
from scipy import misc
import zlib
import base64
import xml.etree.ElementTree as ET


if __name__ == '__main__':
    compressionLevel = -1
    face = misc.imread('payload2.png')
    redlist =[]
    greenlist = []
    bluelist =[]
    fa=numpy.concatenate(face)
    print(face)
    print((fa[0]).shape == (3,))
    for single in fa:
        redlist.append(single[0])
        greenlist.append(single[1])
        bluelist.append(single[2])
    wholelist = numpy.asarray(redlist+greenlist+bluelist)

    xmlstring = '<xml version="1.0" encoding="UTF-8"?>\n'
    columns = int(len(face[1]))
    rows = int(len(fa)/columns)
    print(fa[1])
    if(len(fa[1]) == 3):
        xmlstring += '<payload type="Color" size="'+str(rows)+','+str(columns)+'" compressed='
        if(compressionLevel==-1):
            xmlstring+='"False">\n'
        else:
            xmlstring+='"True">\n'
    afterzip = zlib.compress(fa,6)
    afterbase = base64.b64encode(afterzip)
    print(type(afterzip))
    xmlstring += str(afterbase)
    xmlstring += '\n</payload>'
    #print(xmlstring)

    #YY = ET.parse('payload1_0.xml')
    #print(type(YY))