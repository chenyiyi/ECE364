import os, sys, re, math, operator
from pprint import pprint as pp

class Simulation:
    def __init__(self,simnNo,simDate, chipName,chipCount,chipCost):
        self.simulationNumber = simnNo
        self.simulationDate = simDate
        self.chipName = chipName
        self.chipCount = chipCount
        self.chipCost = chipCost
        self.simulationCost = chipCost * chipCount

    def __str__(self):
        strr = self.chipName + ': '+ str('%03d' %self.simulationNumber) + ', ' + self.simulationDate + ', '+'$'+ str('%06.2f' %self.simulationCost)
        return strr


class Employee:
    def __init__(self, employee, employeeID):
        self.employeeName = employee
        self.employeeID = employeeID
        self.simulationsDict = {}

    def addSimulation(self,s):
        self.simulationsDict.update({s.simulationNumber:s})

    def getSimulation(self, simNo):
        if simNo in self.simulationsDict.keys():
            return self.simulationsDict[simNo]
        else:
            return None

    def getWorkload(self):
        c = list(self.simulationsDict.keys())
        c.sort()
        slist = []
        a = 0
        for i in c:
            a += 1
        sss = self.employeeID + ', ' + self.employeeName + ': ' + str('%02d' %a) + ' Simulations\n'
        for i in c:
            slist.append(self.simulationsDict[i].chipName + ': ' + str('%03d' %self.simulationsDict[i].simulationNumber) + ', ' +self.simulationsDict[i].simulationDate + ', $' + str('%06.2f' %self.simulationsDict[i].simulationCost))
        slist.sort()
        for i in slist[:-1]:
            sss += i
            sss += '\n'
        sss +=slist[-1]
        return sss

    def addWorkload(self, fileName):
        f = open(fileName, 'r')
        lines = f.readlines()
        lines = lines[2:]
        for single in lines:
            ss=single.split()
            newsimul = Simulation(int(ss[0]), ss[1], ss[2], float(ss[3]), float(ss[4][1:]))
            self.simulationsDict.update({newsimul.simulationNumber: newsimul})


    def __str__(self):
        c = list(self.simulationsDict.keys())
        a = 0
        for i in c:
            a += 1
        sss = self.employeeID + ', ' + self.employeeName + ': ' + str('%02d' %a) + ' Simulations'
        return sss



class Facility:
    def __init__(self,facilityName):
        self.facilityName = facilityName
        self.employeesDict={}


    def addEmployee(self, employee):
        self.employeesDict.update({employee.employeeName:employee})

    def getEmployees(self, *args):
        returnlist = []
        for i in args:
            returnlist.append(self.employeesDict[i])
        return returnlist



    def __str__(self):
        a = list(self.employeesDict.keys())
        b = []
        sss = ''
        sss += self.facilityName + ': ' + str('%02d' %len(self.employeesDict)) + ' Employees\n'
        for i in a:
            b.append(self.employeesDict[i].employeeID + ', ' +self.employeesDict[i].employeeName + ': ' + str('%02d' %len(self.employeesDict[i].simulationsDict)) +' Simulations')
        b.sort()
        for ll in b[:-1]:
            sss += ll
            sss += '\n'
        sss += b[-1]

        return sss

    def getSimulation(self, simNo):
        for i in self.employeesDict.keys():
            if simNo in self.employeesDict[i].simulationsDict.keys():
                return self.employeesDict[i].simulationsDict[simNo]
        return None


