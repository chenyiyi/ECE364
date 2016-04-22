import glob
import os

def rowSumIsValid(ll):
    row_sum = 0
    row_sum_before = 0
    for small_ll in ll:
        for item in small_ll:
            row_sum = row_sum+item
        if(row_sum_before !=0):
            if(row_sum != row_sum_before):
                return False
        row_sum_before = row_sum
        row_sum = 0

    return True


def columnSumIsValid(ll):
    col_sum = 0
    col_sum_before = 0
    len_col = len(ll)
    i=0
    while i<len_col:
        for small_ll in ll:
            col_sum = col_sum+small_ll[i]
        if(col_sum_before != 0):
            if(col_sum_before != col_sum):
                return False
        col_sum_before = col_sum
        col_sum =0
        i += 1

    return True




def magicSquareIsValid(filePath):
    input_ll=[]
    output_ll=[]
    with open (filePath, 'r') as magic_read:
        all_line = magic_read.readlines()
        for line in all_line:
            line = line.strip()
            input_ll.append(line)
        for ll in input_ll:
            ll = list(ll)
            output_ll.append(ll)
        print(output_ll)

    return input_ll

def getTotalCost(input_set):
    return_map ={}
    cost = 0
    files = glob.glob('./Stores/*')
    for fi in files:
        with open(fi, 'r') as myFile:
            market_name = fi[9:]
            market_name = market_name[:-4]
            all_line = myFile.readlines()
            all_need = all_line[3:]
            for brand,number in input_set:
                for line in all_need:
                    line = line.split(',')
                    item_name = line[0]
                    item_pr = line[1]
                    item_name = item_name.strip()
                    item_pr = item_pr.strip()
                    item_pr = item_pr[1:]
                    if (item_name == brand):
                        cost = cost + (number*float(item_pr))
            return_map[market_name]=round(cost,2)
            cost = 0

    return return_map

def getBestPrices(input_set):
    return_map={}
    lowest=9999
    lowest_market = ""
    for brand in input_set:
        files = glob.glob('./Stores/*')
        for fi in files:
            with open(fi, 'r') as myFile:
                market_name = fi[9:]
                market_name = market_name[:-4]
                all_line = myFile.readlines()
                all_need = all_line[3:]
                for line in all_need:
                    line = line.split(',')
                    item_name = line[0]
                    item_pr = line[1]
                    item_name = item_name.strip()
                    item_pr = item_pr.strip()
                    item_pr = item_pr[1:]
                    item_pr = float(item_pr)
                    if (item_name == brand):
                        if(item_pr < lowest):
                            lowest = item_pr
                            lowest_market = market_name
        return_map[brand] = (round(lowest,2), lowest_market)
        lowest=9999

    return return_map

def getMissingItems():
    return_map={}
    all_item=set()
    files = glob.glob('./Stores/*')
    for fi in files:
        with open(fi, 'r') as myFile:
            all_line = myFile.readlines()
            all_need = all_line[3:]
            for line in all_need:
                line = line.split(',')
                item_name = line[0]
                item_name = item_name.strip()
                all_item.add(item_name)
    file_open = glob.glob('./Stores/*')
    for fi in file_open:
        for item_c in all_item:
            with open(fi, 'r') as file_che:
                market_name = fi[9:]
                market_name = market_name[:-4]
                all_line = file_che.readlines()
                all_need = all_line[3:]
                found =0
                for line in all_need:
                    line = line.split(',')
                    item_name = line[0]
                    item_name = item_name.strip()
                    if(item_name == item_c):
                        found = 1
                if(found == 0):
                    if(market_name not in return_map.keys()):
                        return_map[market_name]={item_c}
                    else:
                        return_map[market_name].add(item_c)

    return return_map