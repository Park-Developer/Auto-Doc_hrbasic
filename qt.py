import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("AutoDoc")
        self.setGeometry(800,200,300,300)

        # Intro Label Setting
        intro_label=QLabel("Comment Documentation Program")
        # Button Setting
        upload_Btn=QPushButton("Upload",self)
        upload_Btn.clicked.connect(self.upload_clicked)

        cancel_Btn=QPushButton("Cancel",self)
        cancel_Btn.clicked.connect(self.cancel_clicked)



        # Layour Setting
        main_layout=QVBoxLayout()


        upper_layout=QHBoxLayout()
        upper_layout.addWidget( intro_label)

        lower_layout = QHBoxLayout()
        lower_layout.addWidget(upload_Btn)
        #lower_layout.addWidget(cancel_Btn)

        main_layout.addLayout(upper_layout)
        main_layout.addLayout(lower_layout)
        self.setLayout(main_layout)



    def upload_clicked(self):
        ds= QFileDialog.getExistingDirectory(self)
        QMessageBox.about(self,"message",ds)

    def cancel_clicked(self):
        pass

if __name__=="__main__":
    app=QApplication(sys.argv)
    mywindow=MyWindow()
    mywindow.show()
    app.exec_()