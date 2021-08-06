import os

class JobReader:
    def __init__(self,job_address):
        self.Job_description={}
        self.Variable_raw_List=[]
        self.Function_raw_List=[]
        self.Label_raw_List=[]

        self.user_error_List=[] # User-Error

        self.job_address=job_address
        self.job_list=os.listdir(self.job_address)

    def read_n_make_rawData(self):
        for job in self.job_list: # job : job 파일 이름
            job_loc=self.job_address+"\\"+job
            func_tmp = []
            with open( job_loc, 'r') as file:
                for i, line in enumerate(file):
                    if "@Description" in line:
                        desc_tmp=[]
                        desc_tmp.append(line)
                    elif "@Version" in line:
                        desc_tmp.append(line)
                    elif "@Developer" in line:
                        desc_tmp.append(line)
                        temp_dic = {
                            "job_num": job,
                            "rawdata": desc_tmp
                        }
                        self.Job_description=temp_dic

                    if "@var" in line: # var -> Variable
                        temp_dic={
                            "job_num" : job,
                            "rawdata" : line
                        }
                        self.Variable_raw_List.append(temp_dic)

                    if "@func" in line: # func -> function
                        func_tmp.append(line)
                    elif "@param" in line: # param -> function
                        func_tmp.append(line)
                    elif "@result" in line: # param -> function
                        func_tmp.append(line)
                    elif "@ref" in line:
                        func_tmp.append(line)

                    if "@label" in line: # label -> label
                        temp_dic = {
                            "job_num": job,
                            "rawdata": line
                        }
                        self.Label_raw_List.append(temp_dic)

                # 한개의 파일에서 순환 종류후 데이터 검사
                if (func_tmp!=[]):
                    temp_dic = {
                        "job_num": job,
                        "rawdata": func_tmp
                    }
                    self.Function_raw_List.append(temp_dic)


    def save_DocData(self):
        pass


if __name__=="__main__":

    test_address=r"C:\Users\gnvid\.Nimi Places\Project\HRBASIC AutoDoc\Test code"
    test_jobReader = JobReader(test_address)

    test_jobReader.read_n_make_rawData()
    print(test_jobReader.Variable_raw_List)
    print(test_jobReader.Function_raw_List)
    print(test_jobReader.Label_raw_List)
    print(test_jobReader.Job_description)