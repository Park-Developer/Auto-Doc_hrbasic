
import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AutoDoc")
        self.setGeometry(300,200,300,300)

        # Intro Label Setting
        intro_label=QLabel("Comment Documentation Program")

        intro_layout = QHBoxLayout()
        intro_layout.addWidget(intro_label)

        # Button Setting
        upload_Btn=QPushButton("Upload",self)
        upload_Btn.clicked.connect(self.upload_clicked)

        cancel_Btn=QPushButton("Cancel",self)
        cancel_Btn.clicked.connect(self.cancel_clicked)


        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(upload_Btn)
        button_layout.addWidget(cancel_Btn)
        button_layout.addStretch(1)

        main_layout = QVBoxLayout()
        main_layout.addLayout(intro_layout)
        main_layout.addStretch(1)
        main_layout.addLayout(button_layout )


        self.setLayout(main_layout)

        self.show()

    def upload_clicked(self):
        self.job_directory= QFileDialog.getExistingDirectory(self)
        if (self.job_directory==""):
            pass
        else:
            pass
    def cancel_clicked(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
