import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
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
            self.make_docHTML(self.job_directory);
            QMessageBox.about(self,"message","Complete!!")
            self.close()
            
    def cancel_clicked(self):
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