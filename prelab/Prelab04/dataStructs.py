import glob

def getWordFrequency():
    dictionary = {}
    files = glob.glob('./files/*')
    for fi in files:
        with open(fi,'r') as myFile:
            all_line = myFile.readlines()
            for line in all_line:
                for word in line.split():
                    length = len(word)
                    cha = word[length - 1]
                    if cha < 'A' or (cha>'Z' and cha <'a') or cha > 'z':
                        word_add = word[0:length-2]
                    else:
                        word_add = word
                    if word_add not in dictionary:
                        dictionary[word_add] = 1
                    else:
                        dictionary[word_add] +=1

    return dictionary


def getDuplicates():
    dictionary = {}
    files = glob.glob('./files/*')
    find=0
    for fi in files:
        with open(fi,'r') as myFile:
            data=myFile.read().replace('n', '')
            for key_val_n in dictionary.keys():
                key_val = './files/' + key_val_n +'.txt'
                with open(key_val, 'r') as compare:
                    dd = compare.read().replace('n', '')
                    if(dd==data):
                        tuple_key = dictionary[key_val_n]
                        _, list_group = tuple_key
                        list_group.append(fi[8:11])
                        list.sort(list_group)
                        tuple_key = (_, list_group)
                        dictionary[key_val_n]= tuple_key
                        find=1
            if(find==0):
                count=wordcount(fi)
                list_new = [fi[8:11]]
                tuple_key_new = (count, list_new)
                dictionary[fi[8:11]] = tuple_key_new
            find=0


    return dictionary

def wordcount(str):
    count=0
    with open(str, 'r') as readFile:
        data = readFile.read().replace(',','').replace('.','').split()
        ss = set(data)
        print(ss)
        count = len(ss)
    return count



def getPurchaseReport():
    dic_item = {}
    with open('purchases/Item List.txt', 'r') as Item:
        allline_item = Item.readlines()
        item_line = allline_item[2:]
        for item_single in item_line:
            item_sep = item_single.split()
            dic_item[item_sep[0]]=item_sep[1].replace('$','')

    dic_id = {}
    sum_cost=0
    id_files = glob.glob('./purchases/*')
    id_files.remove('./purchases/Item List.txt')
    for tt in id_files:
        with open(tt,'r') as trans:
            allline_id = trans.readlines()
            id_single = allline_id[2:]
            for id_single_item in id_single:
                id_item_sep = id_single_item.split()
                item_cost = float(dic_item[id_item_sep[0]])*int(id_item_sep[1])
                sum_cost += item_cost
                dic_id[int(tt[23])]=round(sum_cost,2)
        sum_cost=0


    return dic_id



def getTotalSold():
    dic_item = {}
    with open('purchases/Item List.txt', 'r') as Item:
        allline_item = Item.readlines()
        item_line = allline_item[2:]
        for item_single in item_line:
            item_sep = item_single.split()
            dic_item[item_sep[0]]=0


    id_files = glob.glob('./purchases/*')
    id_files.remove('./purchases/Item List.txt')
    for tt in id_files:
        with open(tt,'r') as trans:
            allline_id = trans.readlines()
            id_single = allline_id[2:]
            for item_quan_sin in id_single:
                item_quan_sep = item_quan_sin.split()
                dic_item[item_quan_sep[0]]+=int(item_quan_sep[1])

    return dic_item


