def checkTypes(list):
    num_int=0
    num_float=0
    num_str=0
    for item in list:
        if (type(item) == int):
            num_int += 1
        elif (type(item) == float):
            num_float +=1
        elif (type(item) == str):
            num_str += 1
    numlist=[]
    numlist.append(num_int)
    numlist.append(num_float)
    numlist.append(num_str)

    return numlist


def normalizeVector(list):

    sum=0
    newlist=[]
    for item in list:
        sum = sum+item

    for item in list:
        newlist.append(item/sum)

    return newlist



def findMedian(list):

    length=len(list)
    list.sort()
    if (length%2==0):
        index1=int(length/2-1)
        index2=int(length/2)
        median=(list[index1]+list[index2])/2
    else:
        index=round(length/2)
        median=list[index]

    return median

def rectifySignal(list):
    newlist=[]
    for item in list:
        if (item<0) :
            newlist.append(0)
        else:
            newlist.append(item)

    return newlist


def convertToBoolean(num):

    return num


def convertToInteger(num):

    return num

def switchNames(list):
    import re
    newlist=[]
    i=0
    for item in list:
        ll = re.split(r'[, +]', item)
        newlist.append(ll[2]+' '+ll[0])


    return newlist


def getWeightAverage(list):
    sum=0
    for item in list:
        weight = item.split()
        sum = sum + float(weight[2])
    avg = sum/len(list)

    return avg



#if __name__ == '__main__':
