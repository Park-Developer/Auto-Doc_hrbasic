
import os
import codecs
import chardet

# 0330 은 utf-8인듯?
cnt=1
line_list=[]
folder_address=r"C:\Users\gnvid\.Nimi Places\HRC\GVO V3\ARRAY_PROG\6 AXIS"
def decide_encoding(file_path):
    try:
        print("UTF-8")
        f = open(file_path, 'r', encoding='utf-8') #ansi
        txtdata = f.readlines()
        return (True,"utf-9")
    except:
        try:
            print("ANSI")
            f = open(file_path, 'r', encoding='ansi')  # ansi
            txtdata = f.readlines()
            return (True, "ansi")
        except:
            try:
                print("cp949")
                f = open(file_path, 'r', encoding='cp949')  # ansi
                txtdata = f.readline()
                return (True, "cp949")
            except:
                return (True, None)



file_list = os.listdir(folder_address)
for file in file_list:  # job : job 파일 이름
    file_path = folder_address + "\\" + file
    print(decide_encoding(file_path))


