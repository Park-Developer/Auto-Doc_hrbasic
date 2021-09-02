import os

class JobReader:
    def __init__(self,job_address):
        self.Job_description={}
        self.Variable_raw_List=[]
        self.Function_raw_List=[]
        self.Code_raw_List = []
        self.Label_raw_List=[]

        self.user_error_List=[] # User-Error

        self.file_address=job_address
        self.file_list=os.listdir( self.file_address)

    def is_desc(self,line,readme_flag):
        is_desc=False
        if (readme_flag==True) or ("@Description" in line) or ("@Version" in line) or ("@Revdate" in line) or ("@name" in line) or ("@email" in line) or ("@phone" in line) or ("@read/" in line) or ("/@read" in line):
            is_desc=True

            if  ("@read/" in line):
                readme_flag=True
            elif  ("/@read" in line):
                readme_flag=False

        return is_desc,readme_flag

    def is_func(self,line):
        if ("@func" in line) or ("@param" in line) or ("@result" in line) or ("@ref" in line):
            return True
        else:
            return False

    def check_encoding(self,file_path):
        try:
            f = open(file_path, 'r', encoding='utf-8')  # ansi
            txtdata = f.readlines()
            return (True, "utf-8")
        except:
            try:
                f = open(file_path, 'r', encoding='ansi')  # ansi
                txtdata = f.readlines()
                return (True, "ansi")
            except:
                try:
                    f = open(file_path, 'r', encoding='cp949')  # ansi
                    txtdata = f.readline()
                    return (True, "cp949")
                except:
                    return (True, None)

    def read_n_make_rawData(self):
        is_readingSuccess=True
        readme_flag =False
        readme = []  # read raw데이터 저장
        desc_tmp = []
        # Flag
        readme_flag=False
        code_flag=False
        code_number=0
        for file in self.file_list: # job : job 파일 이름
            file_path=self.file_address+"\\"+file
            is_enable,encoding_type=self.check_encoding(file_path) # encoding type check
            if is_enable==True:
                func_tmp = []
                path,ext=os.path.splitext(file_path)
                if(ext==".JOB" or ext==".job"):
                    job=file  # 파일명 저장 -> .JOB 확장자인 경우에만 실행
                    with open(file_path, 'r',encoding=encoding_type) as file:
                        for i, line in enumerate(file):
                            # [1] Description Data 확인
                            is_desc,readme_flag=self.is_desc(line,readme_flag)
                            if is_desc==True:
                                if readme_flag==True:
                                    readme.append(line)
                                else:
                                    desc_jobName = job
                                    desc_tmp.append(line)

                            # [2] Variable Data 확인
                            if "@var" in line: # var -> Variable
                                temp_dic={
                                    "job_num" : job,
                                    "rawdata" : line,
                                }
                                self.Variable_raw_List.append(temp_dic)

                            # [3] Function Data 확인
                            if self.is_func(line)==True:
                                func_tmp.append(line)

                            # [4] Code Data 확인
                            if "@code/" in line:
                                code_flag = True
                                code_rawdata=[]
                                code_number+=1
                                code_tempdic={
                                    "job_num": job,
                                    "code_num":code_number,
                                }
                            elif "/@code" in line:
                                code_flag = False
                                code_tempdic["rawdata"]=code_rawdata
                                self.Code_raw_List.append(code_tempdic)

                            if code_flag==True:
                                code_rawdata.append(line)

                        # 한개의 파일에서 순환 종류후 데이터 검사
                        # Function Data 저장
                        if (func_tmp!=[]):
                            temp_dic = {
                                "job_num": job,
                                "rawdata": func_tmp
                            }
                            self.Function_raw_List.append(temp_dic)

                        # Description Data 저장
                        if desc_tmp!=[]:
                            self.Job_description = {
                                "job_num": desc_jobName,
                                "rawdata": desc_tmp
                            }

                        if readme!=[]:
                            self.Job_description["readme"]=readme
            else:
                is_readingSuccess = False
                break

        return is_readingSuccess

if __name__=="__main__":

    test_address=r"C:\Users\gnvid\.Nimi Places\Project\Auto Teaching\JOB Program"
    test_jobReader = JobReader(test_address)

    test_jobReader.read_n_make_rawData()
    #print(test_jobReader.Variable_raw_List)
    #print(test_jobReader.Function_raw_List)
    #print(test_jobReader.Job_description)
    print(test_jobReader.Code_raw_List)