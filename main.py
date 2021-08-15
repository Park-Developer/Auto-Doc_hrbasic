import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont
import HTML_Generator as html_ge
import JobReader as job_re
import raw_func

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("AutoDoc")
        self.setGeometry(300,200,300,300)
        self.setWindowIcon(QIcon("autojob_logo.png"))

        # Intro Label Setting
        self.intro_label=QLabel("Comment Documentation Program")

        self.intro_layout = QHBoxLayout()
        self.intro_layout.addWidget(self.intro_label)

        # Progress Label Setting
        self.progress_label=QLabel("◼ Job Directory : ")
        myFont =QFont()
        myFont.setBold(True)
        self.progress_label.setFont(myFont)

        self.progress_label__address=QLabel("")
        self.progress_layout = QHBoxLayout()
        self.progress_layout.addWidget(self.progress_label)
        self.progress_layout.addWidget(self.progress_label__address)

        # Button Setting
        self.upload_Btn=QPushButton("Upload",self)
        self.upload_Btn.clicked.connect(self.upload_clicked)

        self.cancel_Btn=QPushButton("Cancel",self)
        self.cancel_Btn.clicked.connect(self.cancel_clicked)

        self.convert_Btn=QPushButton("Convert",self)
        self.convert_Btn.clicked.connect(self.convert_clicked)
        self.convert_Btn.setDisabled(True)

        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch(1)
        self.button_layout.addWidget(self.upload_Btn)
        self.button_layout.addWidget(self.cancel_Btn)
        self.button_layout.addWidget(self.convert_Btn)
        self.button_layout.addStretch(1)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.intro_layout)
        self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.progress_layout)
        self.main_layout.addStretch(3)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)

        self.show()

    def upload_clicked(self):
        self.job_directory= QFileDialog.getExistingDirectory(self)
        if (self.job_directory==""):
            pass
        else:
            QMessageBox.about(self,"message","Upload Complete!!")
            self.convert_Btn.setDisabled(False)
            self.progress_label__address.setText(self.job_directory)
            
    def cancel_clicked(self):
        self.close()

    def convert_clicked(self):
        self.make_docHTML(self.job_directory)
        QMessageBox.about(self, "message", "Conversion Complete!!")
        self.close()

    def make_docHTML(self,job_address):
        # [1]_ raw data 읽기
        job_reader = job_re.JobReader(job_address)
        job_reader.read_n_make_rawData()
        descrition_raw_data = job_reader.Job_description
        variable_raw_data = job_reader.Variable_raw_List
        function_raw_data = job_reader.Function_raw_List
        
        # [2]_ 데이터 가공
        descrition_processed_data = raw_func.extract_descripInfo(descrition_raw_data)
        variable_processed_data = raw_func.extract_varInfo(variable_raw_data)
        function_processed_data = raw_func.extract_functionInfo(function_raw_data)

        # [3]_ HTML 파일 생성
        html_generator = html_ge.HTML_Generator()
        html_generator.make_description_div(descrition_processed_data)
        html_generator.make_var_div(variable_processed_data)
        html_generator.make_function_div(function_processed_data)

        html_generator.merge_Allhtml()
        result_html = html_generator.returnHTML_file(html_generator.html_base)
        html_file = open('Job Specification.html', 'w')
        html_file.write(result_html)
        html_file.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())