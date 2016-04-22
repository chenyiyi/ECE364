import sys
from functools import partial
from os.path import splitext
from SteganographyGUI import *
from PySide.QtCore import *
from PySide.QtGui import *
from Steganography import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image

class SteganographyConsumer(QMainWindow, Ui_MainWindow):

    compression_level = -1
    carrier_tocheck = 0
    payload_tocheck = 0
    file_path_payload = ''
    file_path_carrier = ''
    file_path_extract = ''
    carrier_size = 0
    payload_size = 0
    payload_exist = 0
    payload_obj = ''
    carrier_obj = ''
    extract_obj = ''
    extract_already =0

    def __init__(self, parent=None):
        super(SteganographyConsumer, self).__init__(parent)
        self.setupUi(self)

        #connection of the function and signal
        self.chkApplyCompression.stateChanged.connect(self.applycompression)
        self.slideCompression.setTracking(False)
        self.slideCompression.valueChanged.connect(self.slidervalue)
        self.btnSave.clicked.connect(self.saveEmbed)
        self.btnClean.clicked.connect(self.carrier_clean)
        self.btnExtract.clicked.connect(self.carrier_extract)
        #self.chkOverride.stateChanged.connect(self.override_check)

        # Get the views that are required to have the drag-and-drop enabled.
        views = [self.viewPayload1, self.viewCarrier1, self.viewCarrier2]
        accept = lambda e: e.accept()

        for view in views:
            # We need to accept the drag event to be able to accept the drop.
            view.dragEnterEvent = accept
            view.dragMoveEvent = accept
            view.dragLeaveEvent = accept

            # Assign an event handler (a method,) to be invoked when a drop is performed.
            view.dropEvent = partial(self.processDrop, view)

        # NOTE: The line above links "all" views to the same function, and passes the view as a parameter in the
        # function. You could pass more than one widget to the function by adding more parameters to the signature,
        # in case you want to bind more than one widget together. you can even pass in another function, as a parameter,
        # which might significantly reduce the size of your code. Finally, if you prefer to have a separate function
        # for each view, where the view name is, say, "someView", you will need to:
        # 1- Create a function with a definition similar: funcName(self, e)
        # 2- Assign the function to be invoked as the event handler:
        #   self.someView.dropEvent = self.funcName

    def saveEmbed(self):
        root = tk.Tk()
        root.withdraw()
        f = filedialog.asksaveasfile(mode='w', defaultextension='png')
        if f is None:
            return
        else:
            if self.chkOverride.isChecked():
                embedimage = Carrier(self.file_path_carrier).embedPayload(self.payload_obj,True)
            else:
                embedimage = Carrier(self.file_path_carrier).embedPayload(self.payload_obj,False)
            imsave(f.name, embedimage)

    def processDrop(self, view, e):
        """
        Process a drop event when it occurs on the views.
        """
        mime = e.mimeData()

        # Guard against types of drops that are not pertinent to this app.
        if not mime.hasUrls():
            return

        # Obtain the file path using the OS format.
        filePath = mime.urls()[0].toLocalFile()
        _, ext = splitext(filePath)

        if not ext == ".png":
            return

        # Now the file path is ready to be processed.
        #
        # TODO: Remove the print statement and continue the implementation using the filePath.
        #
        #print(filePath)

        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(filePath))

        view.setScene(scene)
        view.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        view.show()


        #if view is payload
        if view is self.viewPayload1:
            #display the payload size
            self.setSize(self.txtPayloadSize, filePath)
            self.chkApplyCompression.setChecked(False)
            self.lblLevel.setEnabled(False)
            self.slideCompression.setEnabled(False)
            self.slideCompression.setValue(0)
            self.txtCompression.setEnabled(False)
            self.txtCompression.setText('0')
            self.payload_tocheck = 1
        elif view is self.viewCarrier1:
            #display the payload size
            self.carrier_tocheck = 1
            self.setSize(self.txtCarrierSize, filePath)
            if Carrier(self.file_path_carrier).payloadExists() is True:
                self.lblPayloadFound.setText('>>>Payload Found<<<')
                self.chkOverride.setEnabled(True)
                self.payload_exist = 1
            else:
                self.lblPayloadFound.setText('')
                self.chkOverride.setEnabled(False)
                self.payload_exist = 0
        self.checkforEmbed()


        #if view is for extraction
        if view is self.viewCarrier2:
            img = imread(filePath)
            extra_carrier = Carrier(img)
            self.extract_obj = extra_carrier
            self.file_path_extract = filePath
            if self.extract_already==1:
                self.viewPayload2.scene().clear()
                self.viewPayload2.update()
            if extra_carrier.payloadExists() is False:
                self.lblCarrierEmpty.setText('>>>>Carrier Empty<<<<')
                self.btnExtract.setEnabled(False)
                self.btnClean.setEnabled(False)
            else:
                self.lblCarrierEmpty.setText('')
                self.btnExtract.setEnabled(True)
                self.btnClean.setEnabled(True)


    def setSize(self, line, path):
        img = imread(path)
        if line is self.txtPayloadSize:
            self.file_path_payload = img
            self.payload_obj = Payload(img, self.compression_level)
            xmlstring = self.payload_obj.xml
            line.setText(str(len(xmlstring)))
            self.payload_size = len(xmlstring)
        elif line is self.txtCarrierSize:
            self.file_path_carrier = img
            if len(img.shape)==3:
                row_ca,column_ca,_= img.shape
                ca_total = int(row_ca)*int(column_ca)*3
            elif len(img.shape)==2:
                row_ca,column_ca= img.shape
                ca_total = int(row_ca)*int(column_ca)
            line.setText(str(int(ca_total/8)))
            self.carrier_size = int(ca_total/8)


    def applycompression(self):
        state = self.chkApplyCompression.isChecked()
        #compression is checked
        if state is True:
            self.compression_level=0
            self.slideCompression.setEnabled(True)
            self.lblLevel.setEnabled(True)
            self.txtCompression.setEnabled(True)
        else:
            self.compression_level=-1
            self.slideCompression.setEnabled(False)
            self.lblLevel.setEnabled(False)
            self.txtCompression.setEnabled(False)
        #self.checkforEmbed()
        self.payload_obj = Payload(self.file_path_payload, self.compression_level)
        xmlstring = self.payload_obj.xml
        self.txtPayloadSize.setText(str(len(xmlstring)))
        self.payload_size = len(xmlstring)


    #set the slider value to txt box and do the compression
    def slidervalue(self):
        self.txtCompression.setText(str(self.slideCompression.sliderPosition()))
        self.compression_level = int(self.slideCompression.sliderPosition())
        if self.payload_tocheck==1:
            self.payload_obj = Payload(self.file_path_payload, self.compression_level)
            xmlstring = self.payload_obj.xml
            self.txtPayloadSize.setText(str(len(xmlstring)))
            self.payload_size = len(xmlstring)
        self.checkforEmbed()


    def checkforEmbed(self):
        if self.carrier_tocheck==1 and self.payload_tocheck==1:
            if(self.payload_size <= self.carrier_size):
                if(self.payload_exist ==1):
                    if self.chkOverride.isChecked():
                        self.btnSave.setEnabled(True)
                    else:
                        self.btnSave.setEnabled(False)
                else:
                    self.btnSave.setEnabled(True)
            else:
                self.btnSave.setEnabled(False)




    #extract part !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def carrier_clean(self):
        clean_carrier = self.extract_obj.clean()
        #print(self.file_path_extract)
        imsave(self.file_path_extract, clean_carrier)
        #reset the view
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(self.file_path_extract))
        self.viewCarrier2.setScene(scene)
        self.viewCarrier2.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        self.viewCarrier2.show()
        self.lblCarrierEmpty.setText('>>>Carrier Empty<<<')
        self.btnExtract.setEnabled(False)
        self.btnClean.setEnabled(False)
        self.viewPayload2.scene().clear()
        self.viewPayload2.update()



    def carrier_extract(self):
        extract_payload = self.extract_obj.extractPayload()
        scene = QGraphicsScene()
        if len(extract_payload.img.shape)==2:
            image = QtGui.QImage(extract_payload.img,extract_payload.img.shape[1],extract_payload.img.shape[0],extract_payload.img.shape[1], QtGui.QImage.Format_Indexed8)
        elif len(extract_payload.img.shape)==3:
            image = QtGui.QImage(extract_payload.img,extract_payload.img.shape[1],extract_payload.img.shape[0],extract_payload.img.shape[1]*3, QtGui.QImage.Format_RGB888)
        scene.addPixmap(QPixmap(image))
        self.viewPayload2.setScene(scene)
        self.viewPayload2.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        self.viewPayload2.show()
        self.extract_already = 1



if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = SteganographyConsumer()
    currentForm.show()
    currentApp.exec_()
