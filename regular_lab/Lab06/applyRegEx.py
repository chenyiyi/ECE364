import re,os,sys,math
from pprint import pprint as pp

def getRejectedUsers():
    with open('SiteRegistration.txt', 'r') as openfile:
        lines = openfile.readlines()
        state=''
        rejected=[]
        for line in lines:
            num=re.search(r'\d\d\d..\d{1,}.\d{1,}', line)
            email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
            na_sa=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
            name=na_sa[0]
            switchname = re.search(r'[,]', name)
            #swith the last name and first name
            if switchname is not None:
                namechange = re.findall(r'\w+', name)
                name =  namechange[1] + ' ' + namechange[0]
            if len(na_sa) is 2:
                state=na_sa[1]
            if num is None and email is None and state is '':
                rejected.append(name)
            state =''
        rejected.sort()
    return rejected

def getUsersWithCompleteInfo():
    with open('SiteRegistration.txt','r') as openfile:
        lines = openfile.readlines()
        state = ''
        returndic = {}
        for single in lines:
            num = re.search(r'\d\d\d..\d{1,}.\d{1,}', single)
            if num is not None:
                first_num = re.findall(r'\d\d\d', num.group())
                last_num = re.findall(r'......*\d\d\d\d', num.group())
                num = '(' + first_num[0] + ') ' + first_num[1] + '-' + last_num[0][-4:]
            email=re.search(r'[A-Z0-9a-z._-]{1,}@purdue.com', single)
            na_sa=re.findall(r'[A-Z][a-z]{1,}..?[A-Za-z]{1,}', single)
            name=na_sa[0]
            switchname=re.search(r'[,]', name)
            if switchname is not None:
                namechange = re.findall(r'\w+', name)
                name= namechange[1] + ' ' + namechange[0]
            if len(na_sa) is 2:
                state = na_sa[1]
            if num is not None and email is not None and state is not '':
                returndic[name] = (email.group(), num, state)
            state = ''
    return returndic


def getUsersWithEmails():
    with open('SiteRegistration.txt', 'r') as openfile:
        lines = openfile.readlines()
        returndic={}
        for line in lines:
            email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
            na_sa=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
            name=na_sa[0]
            switchname = re.search(r'[,]', name)
            if switchname is not None:
                namechange = re.findall(r'\w+', name)
                name = namechange[1] + ' ' + namechange[0]
            if email is not None:
                returndic[name] = email.group()
    return returndic


def getUsersWithPhones():
    with open('SiteRegistration.txt','r') as openfile:
        lines = openfile.readlines()
        returndic = {}
        for single in lines:
            num = re.search(r'\d\d\d..\d{1,}.\d{1,}', single)
            if num is not None:
                first_num = re.findall(r'\d\d\d', num.group())
                last_num = re.findall(r'......*\d\d\d\d', num.group())
                num = '(' + first_num[0] + ') ' + first_num[1] + '-' + last_num[0][-4:]
            na_sa=re.findall(r'[A-Z][a-z]{1,}..?[A-Za-z]{1,}', single)
            name=na_sa[0]
            switchname=re.search(r'[,]', name)
            if switchname is not None:
                namechange = re.findall(r'\w+', name)
                name= namechange[1] + ' ' + namechange[0]
            if num is not None :
                returndic[name] = num
    return returndic

def getUsersWithStates():
    with open('SiteRegistration.txt','r') as openfile:
        lines = openfile.readlines()
        state = ''
        returndic = {}
        for single in lines:
            na_sa=re.findall(r'[A-Z][a-z]{1,}..?[A-Za-z]{1,}', single)
            name=na_sa[0]
            switchname=re.search(r'[,]', name)
            if switchname is not None:
                namechange = re.findall(r'\w+', name)
                name= namechange[1] + ' ' + namechange[0]
            if len(na_sa) is 2:
                state = na_sa[1]
            if state is not '':
                returndic[name] = state
            state = ''
    return returndic



def getUsersWithoutEmails():
    with open('SiteRegistration.txt', 'r') as openfile:
        lines = openfile.readlines()
        state=''
        rejected=[]
        for line in lines:
            num=re.search(r'\d\d\d..\d{1,}.\d{1,}', line)
            email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
            na_sa=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
            name=na_sa[0]
            switchname = re.search(r'[,]', name)
            #swith the last name and first name
            if switchname is not None:
                namechange = re.findall(r'\w+', name)
                name =  namechange[1] + ' ' + namechange[0]
            if len(na_sa) is 2:
                state=na_sa[1]
            if email is None and (num is not None or state is not ''):
                rejected.append(name)
            state =''
        rejected.sort()
    return rejected


def getUsersWithoutPhones():
    with open('SiteRegistration.txt', 'r') as openfile:
        lines = openfile.readlines()
        state=''
        rejected=[]
        for line in lines:
            num=re.search(r'\d\d\d..\d{1,}.\d{1,}', line)
            email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
            na_sa=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
            name=na_sa[0]
            switchname = re.search(r'[,]', name)
            #swith the last name and first name
            if switchname is not None:
                namechange = re.findall(r'\w+', name)
                name =  namechange[1] + ' ' + namechange[0]
            if len(na_sa) is 2:
                state=na_sa[1]
            if num is None and (email is not None or state is not ''):
                rejected.append(name)
            state =''
        rejected.sort()
    return rejected


def getUsersWithoutStates():
    with open('SiteRegistration.txt', 'r') as openfile:
        lines = openfile.readlines()
        state=''
        rejected=[]
        for line in lines:
            num=re.search(r'\d\d\d..\d{1,}.\d{1,}', line)
            email=re.search(r'[a-zA-Z0-9._-]{1,}@purdue.com', line)
            na_sa=re.findall(r'[A-Z][a-z]{1,}..?[a-zA-Z]{1,}',line)
            name=na_sa[0]
            switchname = re.search(r'[,]', name)
            #swith the last name and first name
            if switchname is not None:
                namechange = re.findall(r'\w+', name)
                name =  namechange[1] + ' ' + namechange[0]
            if len(na_sa) is 2:
                state=na_sa[1]
            if state is '' and (num is not None or email is not None):
                rejected.append(name)
            state =''
        rejected.sort()
    return rejected





















