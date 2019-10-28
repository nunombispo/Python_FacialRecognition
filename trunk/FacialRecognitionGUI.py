from typing import List, Any

import face_recognition
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QMessageBox, QLabel
import sys


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.sourceFilename = ''
        self.compareFilename = ''

        self.setGeometry(300, 300, 350, 400)
        self.setWindowTitle('Facial Recognition')
        self.sourceButton = QPushButton('Select Source File', self)
        self.sourceButton.move(10, 10)
        self.sourceButton.clicked.connect(self.select_source_file)
        self.sourceLabel = QLabel(self)
        self.sourceLabel.resize(100, 100)
        self.sourceLabel.move(200, 10)
        self.compareButton = QPushButton('Select Compare File', self)
        self.compareButton.move(10, 150)
        self.compareButton.clicked.connect(self.select_compare_file)
        self.compareLabel = QLabel(self)
        self.compareLabel.resize(100, 100)
        self.compareLabel.move(200, 150)
        self.runButton = QPushButton('Run Compare', self)
        self.runButton.move(10, 300)
        self.runButton.clicked.connect(self.compare_images)
        self.resultLabel = QLabel(self)
        self.resultLabel.move(200, 300)
        self.show()

    def select_source_file(self):
        self.sourceFilename, _ = QFileDialog.getOpenFileName(self, "Select Source File", "",
                                                             "All Files (*);;Image Files (*.jpg)")
        pixmap = self.sourceLabel.pixmap()
        if not pixmap:
            pixmap = QPixmap(self.sourceFilename)
        else:
            pixmap.load(self.sourceFilename)
        self.sourceLabel.setPixmap(pixmap.scaled(self.sourceLabel.size()))
        self.resultLabel.setText("")
        self.resultLabel.adjustSize()
        self.show()

    def select_compare_file(self):
        self.compareFilename, _ = QFileDialog.getOpenFileName(self, "Select Compare File", "",
                                                              "All Files (*);;Image Files (*.jpg)")
        pixmap = self.compareLabel.pixmap()
        if not pixmap:
            pixmap = QPixmap(self.compareFilename)
        else:
            pixmap.load(self.compareFilename)
        self.compareLabel.setPixmap(pixmap.scaled(self.sourceLabel.size()))
        self.resultLabel.setText("")
        self.resultLabel.adjustSize()
        self.show()

    def compare_images(self):
        if not self.sourceFilename or not self.compareFilename:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select both files to compare")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            known_image = face_recognition.load_image_file(self.sourceFilename)
            unknown_image = face_recognition.load_image_file(self.compareFilename)
            know_encoding = face_recognition.face_encodings(known_image)[0]
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            results = face_recognition.compare_faces([know_encoding], unknown_encoding)
            strText = str(results.pop())
            self.resultLabel.setText(strText)
            self.resultLabel.adjustSize()
            self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
