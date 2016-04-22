import glob
import os

def getDetails():
    dic_de = {}
    dic_s =  getNameandId()
    files = glob.glob('./files/*')
    files.remove('./files/students.txt')
    for fi in files:
        with open(fi, 'r') as myFile:
            course_num = fi[12:15]
            all_line = myFile.readlines()
            all_need = all_line[2:]
            for line in all_need:
                line=line.split()
                course_grade = (course_num, float(line[1]))
                if dic_s[line[0]] in dic_de:
                    dic_de[dic_s[line[0]]].add(course_grade)
                else:
                    dic_de[dic_s[line[0]]]={(course_grade)}
    return dic_de




    return dic

def getNameandId():
    dic_stu = {}
    with open('./files/students.txt', 'r') as studentlist:
        all_line = studentlist.readlines()
        student_line = all_line[2:]
        for line in student_line:
            line=line.split('|')
            stu_name=line[0]
            stu_id = line[1]
            stu_name = stu_name.rstrip()
            stu_id = stu_id.lstrip()
            stu_id = stu_id.strip()
            dic_stu[stu_id]=stu_name
    return dic_stu


def getStudentList(num):
    dic_s =  getNameandId()
    list_stu =[]
    file_name = './files/' + 'EECS'+str(num) +'.txt'
    if not (os.path.exists(file_name)):
        return list_stu
    with open(file_name, 'r') as myFile:
        all_line = myFile.readlines()
        all_need = all_line[2:]
        for line in all_need:
            line=line.split()
            list_stu.append(dic_s[line[0]])
            list_stu.sort()
    return list_stu


    return dic

def searchForName(name):
    dic_s =  getNameandId()
    dic_sea = {}
    id_need = ''
    for key in dic_s.keys():
        if (dic_s[key] == name):
            id_need = key
    files = glob.glob('./files/*')
    files.remove('./files/students.txt')
    for fi in files:
        with open(fi, 'r') as myFile:
            course_num = fi[12:15]
            all_line = myFile.readlines()
            all_need = all_line[2:]
            for line in all_need:
                line=line.split()
                if (line[0] == id_need):
                    dic_sea[course_num] = float(line[1])
    return dic_sea



def searchForID(id):
    dic_sea = {}
    files = glob.glob('./files/*')
    files.remove('./files/students.txt')
    for fi in files:
        with open(fi, 'r') as myFile:
            course_num = fi[12:15]
            all_line = myFile.readlines()
            all_need = all_line[2:]
            for line in all_need:
                line=line.split()
                if (line[0] == id):
                    dic_sea[course_num] = float(line[1])
    return dic_sea

def findScore(stu,classnum):
    grade = 0
    found = 0
    dic_s =  getNameandId()
    id_need = ''
    for key in dic_s.keys():
        if (dic_s[key] == stu):
            id_need = key
    file_name = './files/' + 'EECS'+str(classnum) +'.txt'
    if not (os.path.exists(file_name)):
        return None
    with open(file_name, 'r') as myFile:
        all_line = myFile.readlines()
        all_need = all_line[2:]
        for line in all_need:
            line=line.split()
            if(line[0] == id_need):
                grade = float(line[1])
                found =1
    if(found ==1 ):
        return grade
    else:
        return None

    return dic

def getHighest(num):
    file_name = './files/' + 'EECS'+str(num) +'.txt'
    max_score = 0
    highest_stu = ''
    if not (os.path.exists(file_name)):
        stu = ()
        return stu
    dic_s =  getNameandId()
    with open(file_name, 'r') as myFile:
        all_line = myFile.readlines()
        all_need = all_line[2:]
        for line in all_need:
            line=line.split()
            if (int(line[1]) > max_score):
                max_score =  float(line[1])
                highest_stu = line[0]
    stu = (dic_s[highest_stu], max_score)
    return stu

def getLowest(num):
    file_name = './files/' + 'EECS'+str(num) +'.txt'
    max_score = 100
    highest_stu = ''
    if not (os.path.exists(file_name)):
        stu = ()
        return stu
    dic_s =  getNameandId()
    with open(file_name, 'r') as myFile:
        all_line = myFile.readlines()
        all_need = all_line[2:]
        for line in all_need:
            line=line.split()
            if (int(line[1]) < max_score):
                max_score =  float(line[1])
                highest_stu = line[0]
    stu = (dic_s[highest_stu], max_score)
    return stu

    return dic

def getAverageScore(name):
    dic_s =  getNameandId()
    id_need = ''
    avg = 0
    num_cour = 0
    for key in dic_s.keys():
        if (dic_s[key] == name):
            id_need = key
    files = glob.glob('./files/*')
    files.remove('./files/students.txt')
    for fi in files:
        with open(fi, 'r') as myFile:
            all_line = myFile.readlines()
            all_need = all_line[2:]
            for line in all_need:
                line=line.split()
                if (line[0] == id_need):
                    avg += float(line[1])
                    num_cour += 1
    if(num_cour==0):
        return None
    else:
        avg = avg/num_cour

    return avg

