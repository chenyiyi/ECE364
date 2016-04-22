def getPairwiseDifference(ll):

    if (type(ll) is not  list):
        return None

    length = len(ll)
    if (length == 0):
        return None

    newlist=[]
    beforenum=0
    for item in ll:
        if (item == ll[0]):
            beforenum=item
        else:
            newlist.append(item-beforenum)
            beforenum=item

    return  newlist


def flatten(ll):

    if (type(ll) is not list):
        return None

    for i in ll:
        if(type(i) is not list):
            return  None

    newlist=[]
    for item in ll:
        newlist+=item

    return newlist



def partition(ll, num):
    if (type(ll) is not  list):
        return None

    length = len(ll)
    if (length == 0):
        return None


    newlist=[]
    length1=len(ll)-1
    for i in range(0,length1,num):
        newlist.append(ll[i:i+(num)])

    return newlist



def rectifySignal(ll):
    if (type(ll) is not  list):
        return None

    length = len(ll)
    if (length == 0):
        return None


    newlist=[]
    for item in ll:
        if (item<0) :
            newlist.append(0)
        else:
            newlist.append(item)

    return newlist


def floatRange(num1, num2, incre):
    if(num1 >= num2):
        return None

    newlist=[]
    num1_new = int(num1*10)
    num2_new = int(num2*10)
    incre_new = int(incre*10)
    for i in range(num1_new, num2_new, incre_new):
        newlist.append(i/10)
    newlist.append(float(num2))

    return newlist



def getLongestWord(ss):
    if (type(ss) is not str):
        return None

    ll=ss.split()
    length_ss=len(ll)
    if( length_ss <=1 ):
        return None

    length=0
    for item in ll:
        long = len(item)
        if long >= length:
            newstring=item
            length=long
    #s='"'+newstring+'"'
    return newstring


def decodeNumbers(ll):
    if (type(ll) is not list):
        return None

    for item in ll:
        if (type(item) is not int):
            return None

    newlist=[]
    for item in ll:
        ch = chr(item)
        newlist.append(ch)
    str = ''.join(newlist)

    return str


def getCreditCard(ss):
    length = len(ss)
    if (length == 0):
        return None

    ll=list(ss)
    newlist=[]
    for item in ll:
        if(item.isdigit()):
            newlist.append(int(item))

    return newlist
