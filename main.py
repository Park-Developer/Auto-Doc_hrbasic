import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont
import HTML_Generator as html_ge # Main HTML Generator
import Desc_Generator as desc_ge # Description HTML Generator
import Func_Generator as func_ge # Function HTML Generator
import Var_Generator as var_ge # Variable HTML Generator
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
        is_success=self.make_docHTML(self.job_directory)
        if is_success==True:
            QMessageBox.about(self, "message", "Conversion Complete!!")
            self.close()
        else:
            QMessageBox.about(self, "message", "Conversion is Impossible!!")
            self.close()

    def make_docHTML(self,job_address):
        '''
        :param job_address: job program이 위치한 디렉토리 
        :return: html문서 생성
        '''

        # [1]_ raw data 읽기
        job_reader = job_re.JobReader(job_address)
        job_reader.read_n_make_rawData()
        descrition_raw_data = job_reader.Job_description
        variable_raw_data = job_reader.Variable_raw_List
        function_raw_data = job_reader.Function_raw_List

        if ( descrition_raw_data=={} or variable_raw_data==[] or function_raw_data==[]):
            is_success = False
            return is_success
        else:
            # [2]_ 데이터 가공
            descrition_processed_data = raw_func.extract_descripInfo(descrition_raw_data)
            variable_processed_data = raw_func.extract_varInfo(variable_raw_data)
            function_processed_data = raw_func.extract_functionInfo(function_raw_data)

            # [3]_ HTML 내용물 생성
            html_generator = html_ge.HTML_Generator()

            html__desc_generator = desc_ge.Description_Generator(descrition_processed_data)  # description 객체 생성
            html__func_generator = func_ge.Function_Generator(function_processed_data)  # function 객체 생성
            html__var_generator = var_ge.Variable_Generator(variable_processed_data)  # variable 객체 생성

            html_generator.description_div_list = html__desc_generator.return_description_div()
            html_generator.variable_div_list = html__var_generator.return_variable_div()
            html_generator.function_div_list = html__func_generator.return_function_div()

            html_generator.merge_Allhtml()
            result_html = html_generator.returnHTML_file(html_generator.html_base)

            # [4]_ HTML 파일 생성
            file_path = job_address + '\\Job Specification.html'
            
            html_file = open(file_path, 'w')
            html_file.write(result_html)
            html_file.close()

            # [5]_ 함수 결과 반환
            is_success=True
            return is_success

if __name__ == "__main__":
    DEBUG_MODE=True  # debug 모드 세팅

    if DEBUG_MODE==True:
        # C:\Users\gnvid\.Nimi Places\Project\Auto Teaching\JOB Program
        # C:\Users\gnvid\.Nimi Places\Project\HRBASIC AutoDoc\Test code
        test_address = r"C:\Users\gnvid\.Nimi Places\Project\Auto Teaching\JOB Program"
        job_reader = job_re.JobReader(test_address)
        job_reader.read_n_make_rawData()
        descrition_raw_data = job_reader.Job_description
        variable_raw_data = job_reader.Variable_raw_List
        function_raw_data = job_reader.Function_raw_List
        code_raw_data=job_reader.Code_raw_List # debug 모드에만 반영함


        # [2]_ 데이터 가공
        descrition_processed_data = raw_func.extract_descripInfo(descrition_raw_data)
        variable_processed_data = raw_func.extract_varInfo(variable_raw_data)
        function_processed_data = raw_func.extract_functionInfo(function_raw_data)
        code_processed_data = raw_func.extract_codeInfo(code_raw_data)
        print( code_processed_data)

        # [3]_ HTML 파일 생성
        html_generator = html_ge.HTML_Generator()

        html__desc_generator = desc_ge.Description_Generator(descrition_processed_data)  # description 객체 생성
        html__func_generator = func_ge.Function_Generator(function_processed_data)  # function 객체 생성
        html__var_generator = var_ge.Variable_Generator(variable_processed_data)  # variable 객체 생성

        html_generator.description_div_list = html__desc_generator.return_description_div()
        html_generator.variable_div_list = html__var_generator.return_variable_div()
        html_generator.function_div_list = html__func_generator.return_function_div()

        html_generator.merge_Allhtml()
        result_html = html_generator.returnHTML_file(html_generator.html_base)

        file_path=test_address+'\\Job Specification.html'
        html_file = open(file_path, 'w')
        html_file.write(result_html)
        html_file.close()

    else:
        app = QApplication(sys.argv)
        ex = MyApp()
        sys.exit(app.exec_())