from os.path import join
import unittest
from numpy import ndarray as nmat
from scipy.misc import *
from scipy import misc
import numpy
import numpy
import zlib
import base64


class Payload:
    def __init__(self, img=None, compressionLevel=-1, xml=None):
        self.img = img
        self.xml = xml
        self.compressionLevel = compressionLevel

        if self.img is None and self.xml is None or compressionLevel>9 or compressionLevel<-1:
            raise ValueError("First Value error")

        if self.img is not None and isinstance(self.img, numpy.ndarray):
            self.xml = self.getxml()
        elif self.xml is not None and isinstance(self.xml, str):
            self.img = self.getimage()

        if not isinstance(self.img, numpy.ndarray) or not isinstance(self.xml, str):
            raise TypeError



    def getxml(self):
        fa=numpy.concatenate(self.img)
        xmlstring = '<?xml version="1.0" encoding="UTF-8"?>\n'
        columns = int(len(self.img[1]))
        rows = int(len(fa)/columns)
        #check the type of image
        if(fa[0].shape == (3,)):
            xmlstring += '<payload type="Color" size="'+str(rows)+','+str(columns)+'" compressed='
            redlist =[]
            greenlist = []
            bluelist =[]
            for single in fa:
                redlist.append(single[0])
                greenlist.append(single[1])
                bluelist.append(single[2])
            fa = numpy.asarray(redlist+greenlist+bluelist)
        else:
            xmlstring += '<payload type="Gray" size="'+str(rows)+','+str(columns)+'" compressed='
        #check if we need to compress or not
        if(self.compressionLevel==-1):
            xmlstring+='"False">\n'
            afterzip = fa
        else:
            xmlstring+='"True">\n'
            afterzip = zlib.compress(fa,self.compressionLevel)
        #b64 encoding
        afterbase = base64.b64encode(afterzip)
        basestring = str(afterbase)
        basestring = basestring[2:]
        basestring = basestring[:-1]
        xmlstring = xmlstring + basestring + '\n'
        xmlstring += '</payload>'

        return xmlstring

    def getimage(self):
        f = self.xml.split('\n')
        info = f[1].split('"')
        imgtype = info[1]
        compression = info[-2]
        row,column = info[3].split(',')
        beforebase = base64.b64decode(f[2])
        if(compression == 'True'):
            beforezip = zlib.decompress(beforebase)
        else:
            beforezip = beforebase
        bb = numpy.fromstring(beforezip,dtype=numpy.uint8)
        if(imgtype == 'Color'):
            sum = int(row)*int(column)
            redlist=list(bb[0:sum])
            greenlist = list(bb[sum:sum*2])
            bluelist = list(bb[sum*2:sum*3])
            single = []
            ss =[]
            for i in range(0,sum):
                ss.append(redlist[i])
                ss.append(greenlist[i])
                ss.append(bluelist[i])
                single.append(ss)
                ss=[]
            fir = 0
            end = int(column)
            returnfa = []
            for i in range(0,int(row)):
                ha = list(single[fir:end])
                fir = end
                end = end+ int(column)
                returnfa.append(ha)
            returnfa = numpy.asarray(returnfa)
        else:
            single = list(bb)
            fir = 0
            end = int(column)
            returnfa = []
            for i in range(0,int(row)):
                ha = list(single[fir:end])
                fir = end
                end = end+ int(column)
                returnfa.append(ha)
            returnfa = numpy.asarray(returnfa)
        return returnfa


class Carrier:
    def __init__(self, img):
        self.img = img

        if not isinstance(self.img, numpy.ndarray):
            raise TypeError


    def payloadExists(self):
        fa = numpy.concatenate(self.img)
        if (len(fa.shape))==2:
            new_fa =[]
            for h in range(0,104):
                r,g,b = fa[h]
                new_fa.append(r)
            fa = new_fa
        #get bytes compare to "<?xml version"
        checklist=[]
        check_8 = 7
        byte_read =0
        for i in range(0,104):
            if(check_8 == -1):
                check_8=7
                checklist.append(byte_read)
                byte_read =0
            bit_read = int(fa[i]) & 0x01
            bit_shift = bit_read << check_8
            byte_read += bit_shift
            check_8 -=1
            if(i == 103):
                checklist.append(byte_read)
        compare_str =''
        for i in checklist:
            compare_str += chr(i)

        if(compare_str=='<?xml version'):
            return True

        return False



    def clean(self):
        new_img_1 = numpy.copy(self.img)
        new_img_2 = numpy.copy(self.img)
        new_img_1.fill(254)
        return_img = numpy.bitwise_and(new_img_1,new_img_2)

        return return_img



    def embedPayload(self, payload, override=False):
        #check the type
        if not isinstance(payload, Payload):
            raise TypeError

        #check the size of carrier larger than paypload
        xml_list = payload.xml.split('\n')
        pay_info = xml_list[1].split('"')
        pay_type = pay_info[1]
        row,column = pay_info[3].split(',')
        if(pay_type =='Color'):
            pay_total = int(row)*int(column)*3
        else:
            pay_total = int(row)*int(column)
        #check size for carrier
        if(len(self.img.shape)==3):
            row_ca,column_ca,_= self.img.shape
            ca_total = int(row_ca)*int(column_ca)*3
        else:
            row_ca,column_ca = self.img.shape
            ca_total = int(row_ca)*int(column_ca)
        if(pay_total*8 > ca_total):
            raise ValueError

        if(override is False):
            if(self.payloadExists()):
                raise Exception


        #embed process
        #row , column are for payload, pay_type is for payload
        xml_toembed = [ord(c) for c in payload.xml]

        #carrier flat
        if(len(self.img.shape)==3):
            redlist = (self.img[:,:,0])
            greenlist = (self.img[:,:,1])
            bluelist = (self.img[:,:,2])
            whole_list = numpy.concatenate((redlist,greenlist,bluelist))
            whole_list.flatten()
            whole_list = numpy.concatenate(whole_list)
        else:
            whole_list = self.img.flatten()
        xml_toembed = numpy.asarray(xml_toembed, dtype=numpy.uint8)
        unpack = numpy.unpackbits(xml_toembed,axis=0)
        unpack = numpy.append(unpack, whole_list[len(unpack):])
        new_list = numpy.copy(whole_list)
        new_list.fill(~1)
        whole_list = numpy.bitwise_and(whole_list,new_list)
        whole_list = numpy.bitwise_or(whole_list[:len(unpack)], unpack)
        if(len(self.img.shape)==3):
            a,b,c = numpy.hsplit(whole_list,3)
            whole_list = numpy.dstack((a,b,c))
            d=numpy.hsplit(whole_list,row_ca)
            whole_list = numpy.vstack(d)
        else:
            d=numpy.hsplit(whole_list,row_ca)
            whole_list = numpy.vstack(d)
        return whole_list


    def extractPayload(self):
        if self.payloadExists() is False:
            raise Exception

        #img have the number
        if(len(self.img.shape)==3):
            redlist = (self.img[:,:,0])
            greenlist = (self.img[:,:,1])
            bluelist = (self.img[:,:,2])
            whole_list = numpy.concatenate((redlist,greenlist,bluelist))
            whole_list.flatten()
            whole_list = numpy.concatenate(whole_list)
        else:
            whole_list = self.img.flatten()

        new_list = numpy.copy(whole_list)
        new_list.fill(1)
        whole_list = numpy.bitwise_and(whole_list,new_list)
        least_bitlist = numpy.packbits(whole_list)

        least_bitlist = list(map(chr,least_bitlist))
        least_bitlist = ''.join(least_bitlist)
        least_bitlist = least_bitlist.split('</payl')
        least_bitlist = (least_bitlist[0])
        # compare_str = ''
        # pre_che =''
        # for h in least_bitlist:
        #     if(pre_che=='<' and h=='p'):
        #         break
        #     compare_str += chr(h)
        #     pre_che = h


        return_payload = Payload(xml=least_bitlist)
        return return_payload

