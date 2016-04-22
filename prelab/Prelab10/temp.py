# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

class CalculatorConsumer(QMainWindow, Ui_Calculator):

    total = 0 #usesd when operator pressed
    tempnum = 0 #the number press each time
    overtemp = 0 #used when priority is set

    lastoperator = "" #last operator pressed
    curroperator = "" #operator being pressed
    overoperator = "" #used when priority is set

    operator = 0 #check if operator is pressed
    numdit = 0 #check if the digit no greater than 12
    clear = 0 #flag when C is pressed
    numdecimal = 0 #number of decimal number
    priority = 0 #used to detect priority operation
    displaytext = ""
    dot = 0
    dotcal = 10 #used for when there is dot
    separator_state = 0

    def __init__(self, parent=None):
        super(CalculatorConsumer, self).__init__(parent)
        self.setupUi(self)
        self.btn0.clicked.connect(self.clicked_slot)
        self.btn1.clicked.connect(self.clicked_slot)
        self.btn2.clicked.connect(self.clicked_slot)
        self.btn3.clicked.connect(self.clicked_slot)
        self.btn4.clicked.connect(self.clicked_slot)
        self.btn5.clicked.connect(self.clicked_slot)
        self.btn6.clicked.connect(self.clicked_slot)
        self.btn7.clicked.connect(self.clicked_slot)
        self.btn8.clicked.connect(self.clicked_slot)
        self.btn9.clicked.connect(self.clicked_slot)
        self.btnPlus.clicked.connect(self.operator_click)
        self.btnMultiply.clicked.connect(self.operator_click)
        self.btnMinus.clicked.connect(self.operator_click)
        self.btnDivide.clicked.connect(self.operator_click)
        self.btnEqual.clicked.connect(self.equaloperation)
        self.btnClear.clicked.connect(self.clearall)
        self.btnDot.clicked.connect(self.dotpressed)
        self.cboDecimal.activated.connect(self.getdecimal)
        self.numdecimal = int(self.cboDecimal.currentText())
        self.chkSeparator.stateChanged.connect(self.separator_fun)
        self.separator_state = self.chkSeparator.isChecked()

    def separator_fun(self):
        self.separator_state = self.chkSeparator.isChecked()

    def getdecimal(self):
        self.numdecimal = int(self.sender().currentText())


    def clearall(self):
        if(self.clear ==0):
            self.tempnum = 0
            self.txtDisplay.setText(str(self.tempnum))
            self.clear += 1
        elif(self.clear == 1):
            self.tempnum = 0
            self.total = 0
            self.operator = 0
            self.lastoperator = ""
            self.clear = 0


    def dotpressed(self):
        if(self.dot==0):
            self.txtDisplay.setText(str(self.tempnum)+'.')
            self.dot = 1


    def clicked_slot(self):
        if(self.dot ==0):
            nownum = self.tempnum * 10 + int(self.sender().text())
        else:
            nownum = self.tempnum  + (int(self.sender().text()) / (self.dotcal))
            self.dotcal *=10
        self.displaytext = str(nownum)
        self.dislist = self.displaytext.split('.')
        if(len(self.dislist)==2):
            if(len(self.dislist[1])>self.numdecimal):
                #have decimal places and it larger than precision we set
                if(self.separator_state):
                    sepa_text_final =''
                    divide_left = int(self.dislist[0])
                    while(int(divide_left/1000) !=0 ):
                        if(sepa_text_final != ''):
                            sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                        else:
                            sepa_text_final = sepa_text_final + str(divide_left%1000)
                        divide_left = int(divide_left /1000)
                    if(sepa_text_final != ''):
                        sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                    else:
                        sepa_text_final = str(divide_left) + sepa_text_final
                    decimaltext = str("%.*f" % (self.numdecimal,round(nownum, self.numdecimal)))
                    decimaltext_list = decimaltext.split('.')
                    self.txtDisplay.setText(sepa_text_final +'.' + decimaltext_list[1])
                else:
                    self.txtDisplay.setText(str("%.*f" % (self.numdecimal,round(nownum, self.numdecimal))))
            else:
                #it have decimal places but smaller than precision we set
                if(self.separator_state):
                    sepa_text_final =''
                    divide_left = int(self.dislist[0])
                    while(int(divide_left/1000) !=0 ):
                        if(sepa_text_final != ''):
                            sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                        else:
                            sepa_text_final = sepa_text_final + str(divide_left%1000)
                        divide_left = int(divide_left /1000)
                    if(sepa_text_final != ''):
                        sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                    else:
                        sepa_text_final = str(divide_left) + sepa_text_final
                    self.txtDisplay.setText(sepa_text_final +'.' + self.dislist[1])
                else:
                    self.txtDisplay.setText(str(nownum))
        else:
            #it do not have the decimal places
            if(self.separator_state):
                sepa_text_final =''
                divide_left = nownum
                while(int(divide_left/1000) !=0 ):
                    if(sepa_text_final != ''):
                        sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                    else:
                        sepa_text_final = sepa_text_final + str(divide_left%1000)
                    divide_left = int(divide_left /1000)
                if(sepa_text_final != ''):
                    sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                else:
                    sepa_text_final = str(divide_left) + sepa_text_final
                self.txtDisplay.setText(sepa_text_final)
            else:
                self.txtDisplay.setText(str(nownum))
        self.tempnum = nownum


    def equaloperation(self):
        if(self.operator == 1):
            if(self.priority ==0):
                if(self.lastoperator == '+'):
                    self.total += self.tempnum
                if(self.lastoperator == '-'):
                    self.total -= self.tempnum
                if(self.lastoperator == 'x'):
                    self.total *= self.tempnum
                if(self.lastoperator == '/'):
                    self.total /= self.tempnum
                self.tempnum = self.total
                self.displaytext = str(self.total)
                self.dislist = self.displaytext.split('.')
                if(len(self.dislist)==2):
                    if(len(self.dislist[1])>self.numdecimal):
                        #have decimal places and it larger than precision we set
                        if(self.separator_state):
                            sepa_text_final =''
                            divide_left = int(self.dislist[0])
                            while(int(divide_left/1000) !=0 ):
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                else:
                                    sepa_text_final = sepa_text_final + str(divide_left%1000)
                                divide_left = int(divide_left /1000)
                            if(sepa_text_final != ''):
                                sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                            else:
                                sepa_text_final = str(divide_left) + sepa_text_final
                            decimaltext = str("%.*f" % (self.numdecimal,round(self.total, self.numdecimal)))
                            decimaltext_list = decimaltext.split('.')
                            self.txtDisplay.setText(sepa_text_final +'.' + decimaltext_list[1])
                        else:
                            self.txtDisplay.setText(str("%.*f" % (self.numdecimal,round(self.total, self.numdecimal))))
                    else:
                        #it have decimal places but smaller than precision we set
                        if(self.separator_state):
                            sepa_text_final =''
                            divide_left = int(self.dislist[0])
                            while(int(divide_left/1000) !=0 ):
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                else:
                                    sepa_text_final = sepa_text_final + str(divide_left%1000)
                                divide_left = int(divide_left /1000)
                            if(sepa_text_final != ''):
                                sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                            else:
                                sepa_text_final = str(divide_left) + sepa_text_final
                            self.txtDisplay.setText(sepa_text_final +'.' + self.dislist[1])
                        else:
                            self.txtDisplay.setText(str(self.total))
                #until here
                else:
                    if(self.separator_state):
                        sepa_text_final =''
                        divide_left = self.total
                        while(int(divide_left/1000) !=0 ):
                            if(sepa_text_final != ''):
                                sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                            else:
                                sepa_text_final = sepa_text_final + str(divide_left%1000)
                            divide_left = int(divide_left /1000)
                        if(sepa_text_final != ''):
                            sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                        else:
                            sepa_text_final = str(divide_left) + sepa_text_final
                        self.txtDisplay.setText(sepa_text_final)
                    else:
                        self.txtDisplay.setText(str(self.total))
                    #self.txtDisplay.setText(str(self.total))
            else:
                if(self.lastoperator == '+'):
                    if(self.overoperator == 'x'):
                        self.overtemp *= self.tempnum
                    elif(self.overoperator == '/'):
                        self.overtemp /= self.tempnum
                    self.total += self.overtemp
                elif(self.lastoperator == '-'):
                    if(self.overoperator == 'x'):
                        self.overtemp *= self.tempnum
                    elif(self.overoperator == '/'):
                        self.overtemp /= self.tempnum
                    self.total += self.overtemp
                self.tempnum = self.total
                self.displaytext = str(self.total)
                self.dislist = self.displaytext.split('.')
                if(len(self.dislist)==2):
                    if(len(self.dislist[1])>self.numdecimal):
                        #have decimal places and it larger than precision we set
                        if(self.separator_state):
                            sepa_text_final =''
                            divide_left = int(self.dislist[0])
                            while(int(divide_left/1000) !=0 ):
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                else:
                                    sepa_text_final = sepa_text_final + str(divide_left%1000)
                                divide_left = int(divide_left /1000)
                            if(sepa_text_final != ''):
                                sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                            else:
                                sepa_text_final = str(divide_left) + sepa_text_final
                            decimaltext = str("%.*f" % (self.numdecimal,round(self.total, self.numdecimal)))
                            decimaltext_list = decimaltext.split('.')
                            self.txtDisplay.setText(sepa_text_final +'.' + decimaltext_list[1])
                        else:
                            self.txtDisplay.setText(str("%.*f" % (self.numdecimal,round(self.total, self.numdecimal))))
                    else:
                        #it have decimal places but smaller than precision we set
                        if(self.separator_state):
                            sepa_text_final =''
                            divide_left = int(self.dislist[0])
                            while(int(divide_left/1000) !=0 ):
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                else:
                                    sepa_text_final = sepa_text_final + str(divide_left%1000)
                                divide_left = int(divide_left /1000)
                            if(sepa_text_final != ''):
                                sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                            else:
                                sepa_text_final = str(divide_left) + sepa_text_final
                            self.txtDisplay.setText(sepa_text_final +'.' + self.dislist[1])
                        else:
                            self.txtDisplay.setText(str(self.total))
                #until here
                else:
                    if(self.separator_state):
                        sepa_text_final =''
                        divide_left = self.total
                        while(int(divide_left/1000) !=0 ):
                            if(sepa_text_final != ''):
                                sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                            else:
                                sepa_text_final = sepa_text_final + str(divide_left%1000)
                            divide_left = int(divide_left /1000)
                        if(sepa_text_final != ''):
                            sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                        else:
                            sepa_text_final = str(divide_left) + sepa_text_final
                        self.txtDisplay.setText(sepa_text_final)
                    else:
                        self.txtDisplay.setText(str(self.total))
            self.lastoperator = self.sender().text()
            self.clear = 0
            self.priority = 0
            self.operator = 0
            self.dot = 0
            self.dotcal = 10

    def operator_click(self):
        self.curroperator = self.sender().text()
        if(self.operator ==0):
            self.total = self.tempnum
            self.tempnum = 0
            self.lastoperator = self.sender().text()
        else:
            if(self.curroperator == '+' or self.curroperator == '-' or self.curroperator == '=' or self.lastoperator == 'x' or self.lastoperator =='/'):
                if(self.priority ==0):
                    if(self.lastoperator == '+'):
                        self.total += self.tempnum
                        self.tempnum = 0
                    elif(self.lastoperator == '-'):
                        self.total -= self.tempnum
                        self.tempnum = 0
                    elif(self.lastoperator == 'x'):
                        self.total *= self.tempnum
                        self.tempnum = 0
                    elif(self.lastoperator == '/'):
                        self.total /= self.tempnum
                        self.tempnum = 0
                    self.displaytext = str(self.total)
                    self.dislist = self.displaytext.split('.')
                    if(len(self.dislist)==2):
                        if(len(self.dislist[1])>self.numdecimal):
                            #have decimal places and it larger than precision we set
                            if(self.separator_state):
                                sepa_text_final =''
                                divide_left = int(self.dislist[0])
                                while(int(divide_left/1000) !=0 ):
                                    if(sepa_text_final != ''):
                                        sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                    else:
                                        sepa_text_final = sepa_text_final + str(divide_left%1000)
                                        divide_left = int(divide_left /1000)
                                        if(sepa_text_final != ''):
                                            sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                                        else:
                                            sepa_text_final = str(divide_left) + sepa_text_final
                                        decimaltext = str("%.*f" % (self.numdecimal,round(self.total, self.numdecimal)))
                                        decimaltext_list = decimaltext.split('.')
                                        self.txtDisplay.setText(sepa_text_final +'.' + decimaltext_list[1])
                            else:
                                self.txtDisplay.setText(str("%.*f" % (self.numdecimal,round(self.total, self.numdecimal))))
                        else:
                            #it have decimal places but smaller than precision we set
                            if(self.separator_state):
                                sepa_text_final =''
                                divide_left = int(self.dislist[0])
                                while(int(divide_left/1000) !=0 ):
                                    if(sepa_text_final != ''):
                                        sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                    else:
                                        sepa_text_final = sepa_text_final + str(divide_left%1000)
                                    divide_left = int(divide_left /1000)
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                                else:
                                    sepa_text_final = str(divide_left) + sepa_text_final
                                self.txtDisplay.setText(sepa_text_final +'.' + self.dislist[1])
                            else:
                                self.txtDisplay.setText(str(self.total))
                    else:
                        if(self.separator_state):
                            sepa_text_final =''
                            divide_left = self.total
                            while(int(divide_left/1000) !=0 ):
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                else:
                                    sepa_text_final = sepa_text_final + str(divide_left%1000)
                                divide_left = int(divide_left /1000)
                            if(sepa_text_final != ''):
                                sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                            else:
                                sepa_text_final = str(divide_left) + sepa_text_final
                            self.txtDisplay.setText(sepa_text_final)
                        else:
                            self.txtDisplay.setText(str(self.total))
                    self.lastoperator = self.sender().text()
                else:
                    if(self.lastoperator == '+'):
                        if(self.overoperator == 'x'):
                            self.overtemp *= self.tempnum
                        elif(self.overoperator == '/'):
                            self.overtemp /= self.tempnum
                        self.total += self.overtemp
                    elif(self.lastoperator == '-'):
                        if(self.overoperator == 'x'):
                            self.overtemp *= self.tempnum
                        elif(self.overoperator == '/'):
                            self.overtemp /= self.tempnum
                        self.total += self.overtemp
                    self.tempnum = 0
                    self.displaytext = str(self.total)
                    self.dislist = self.displaytext.split('.')
                    if(len(self.dislist)==2):
                        if(len(self.dislist[1])>self.numdecimal):
                            #have decimal places and it larger than precision we set
                            if(self.separator_state):
                                sepa_text_final =''
                                divide_left = int(self.dislist[0])
                                while(int(divide_left/1000) !=0 ):
                                    if(sepa_text_final != ''):
                                        sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                    else:
                                        sepa_text_final = sepa_text_final + str(divide_left%1000)
                                    divide_left = int(divide_left /1000)
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                                else:
                                    sepa_text_final = str(divide_left) + sepa_text_final
                                decimaltext = str("%.*f" % (self.numdecimal,round(self.total, self.numdecimal)))
                                decimaltext_list = decimaltext.split('.')
                                self.txtDisplay.setText(sepa_text_final +'.' + decimaltext_list[1])
                            else:
                                self.txtDisplay.setText(str("%.*f" % (self.numdecimal,round(self.total, self.numdecimal))))
                        else:
                            #it have decimal places but smaller than precision we set
                            if(self.separator_state):
                                sepa_text_final =''
                                divide_left = int(self.dislist[0])
                                while(int(divide_left/1000) !=0 ):
                                    if(sepa_text_final != ''):
                                        sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                    else:
                                        sepa_text_final = sepa_text_final + str(divide_left%1000)
                                    divide_left = int(divide_left /1000)
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                                else:
                                    sepa_text_final = str(divide_left) + sepa_text_final
                                self.txtDisplay.setText(sepa_text_final +'.' + self.dislist[1])
                            else:
                                self.txtDisplay.setText(str(self.total))
                    else:
                        if(self.separator_state):
                            sepa_text_final =''
                            divide_left = self.total
                            while(int(divide_left/1000) !=0 ):
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                else:
                                    sepa_text_final = sepa_text_final + str(divide_left%1000)
                                divide_left = int(divide_left /1000)
                            if(sepa_text_final != ''):
                                sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                            else:
                                sepa_text_final = str(divide_left) + sepa_text_final
                            self.txtDisplay.setText(sepa_text_final)
                        else:
                            self.txtDisplay.setText(str(self.total))
                self.priority = 0
            else:
                if(self.priority == 1):
                    if(self.overoperator == 'x'):
                        self.overtemp *= self.tempnum
                        self.displaytext = str(self.overtemp)
                        self.dislist = self.displaytext.split('.')
                    elif(self.overoperator == '/'):
                        self.overtemp /= self.tempnum
                        self.displaytext = str(self.overtemp)
                        self.dislist = self.displaytext.split('.')
                    if(len(self.dislist)==2):
                        if(len(self.dislist[1])>self.numdecimal):
                            #have decimal places and it larger than precision we set
                            if(self.separator_state):
                                sepa_text_final =''
                                divide_left = int(self.dislist[0])
                                while(int(divide_left/1000) !=0 ):
                                    if(sepa_text_final != ''):
                                        sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                    else:
                                        sepa_text_final = sepa_text_final + str(divide_left%1000)
                                    divide_left = int(divide_left /1000)
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                                else:
                                    sepa_text_final = str(divide_left) + sepa_text_final
                                decimaltext = str("%.*f" % (self.numdecimal,round(self.total, self.numdecimal)))
                                decimaltext_list = decimaltext.split('.')
                                self.txtDisplay.setText(sepa_text_final +'.' + decimaltext_list[1])
                            else:
                                self.txtDisplay.setText(str("%.*f" % (self.numdecimal,round(self.total, self.numdecimal))))
                        else:
                            #it have decimal places but smaller than precision we set
                            if(self.separator_state):
                                sepa_text_final =''
                                divide_left = int(self.dislist[0])
                                while(int(divide_left/1000) !=0 ):
                                    if(sepa_text_final != ''):
                                        sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                    else:
                                        sepa_text_final = sepa_text_final + str(divide_left%1000)
                                    divide_left = int(divide_left /1000)
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                                else:
                                    sepa_text_final = str(divide_left) + sepa_text_final
                                self.txtDisplay.setText(sepa_text_final +'.' + self.dislist[1])
                            else:
                                self.txtDisplay.setText(str(self.total))
                    else:
                        if(self.separator_state):
                            sepa_text_final =''
                            divide_left = self.total
                            while(int(divide_left/1000) !=0 ):
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                else:
                                    sepa_text_final = sepa_text_final + str(divide_left%1000)
                                divide_left = int(divide_left /1000)
                            if(sepa_text_final != ''):
                                sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                            else:
                                sepa_text_final = str(divide_left) + sepa_text_final
                            self.txtDisplay.setText(sepa_text_final)
                        else:
                            self.txtDisplay.setText(str(self.total))
                    self.overoperator = self.sender().text()
                else:
                    self.priority = 1
                    self.overtemp = self.tempnum
                    self.overoperator = self.sender().text()
                    self.displaytext = str(self.tempnum)
                    self.dislist = self.displaytext.split('.')
                    if(len(self.dislist)==2):
                        if(len(self.dislist[1])>self.numdecimal):
                            #have decimal places and it larger than precision we set
                            if(self.separator_state):
                                sepa_text_final =''
                                divide_left = int(self.dislist[0])
                                while(int(divide_left/1000) !=0 ):
                                    if(sepa_text_final != ''):
                                        sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                    else:
                                        sepa_text_final = sepa_text_final + str(divide_left%1000)
                                    divide_left = int(divide_left /1000)
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                                else:
                                    sepa_text_final = str(divide_left) + sepa_text_final
                                decimaltext = str("%.*f" % (self.numdecimal,round(self.total, self.numdecimal)))
                                decimaltext_list = decimaltext.split('.')
                                self.txtDisplay.setText(sepa_text_final +'.' + decimaltext_list[1])
                            else:
                                self.txtDisplay.setText(str("%.*f" % (self.numdecimal,round(self.total, self.numdecimal))))
                        else:
                            #it have decimal places but smaller than precision we set
                            if(self.separator_state):
                                sepa_text_final =''
                                divide_left = int(self.dislist[0])
                                while(int(divide_left/1000) !=0 ):
                                    if(sepa_text_final != ''):
                                        sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                    else:
                                        sepa_text_final = sepa_text_final + str(divide_left%1000)
                                    divide_left = int(divide_left /1000)
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                                else:
                                    sepa_text_final = str(divide_left) + sepa_text_final
                                self.txtDisplay.setText(sepa_text_final +'.' + self.dislist[1])
                            else:
                                self.txtDisplay.setText(str(self.total))
                    else:
                        if(self.separator_state):
                            sepa_text_final =''
                            divide_left = self.total
                            while(int(divide_left/1000) !=0 ):
                                if(sepa_text_final != ''):
                                    sepa_text_final =  str(divide_left%1000) + ',' +sepa_text_final
                                else:
                                    sepa_text_final = sepa_text_final + str(divide_left%1000)
                                divide_left = int(divide_left /1000)
                            if(sepa_text_final != ''):
                                sepa_text_final =  str(divide_left) + ',' + sepa_text_final
                            else:
                                sepa_text_final = str(divide_left) + sepa_text_final
                            self.txtDisplay.setText(sepa_text_final)
                        else:
                            self.txtDisplay.setText(str(self.total))
                    self.tempnum = 0
                    self.overoperator = self.sender().text()

        self.dot = 0
        self.dotcal = 10
        self.operator = 1
        self.clear = 0


currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()


currentForm.show()
currentApp.exec_()
