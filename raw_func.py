import text_func

def extract_varInfo(var_raw:list):
    # rawdata form : {'job_num': '5001_Glo_Var.JOB', 'rawdata': "gi_Search=1\t'@var Stage Search Method @type Integer @use(0 : No setting, 1:Manual Searching, 2 : Auto Searching)\n"}
    result={}

    for rawdata in var_raw:
        job_num=rawdata["job_num"]
        raw_data=rawdata["rawdata"]

        variable__loc=text_func.extract_var_loc(job_num)

        raw_dataList= raw_data.split('@')

        '''
        raw_dataList Form
        ["gi_Search=1\t'",
         'var Stage Search Method ',
         'type Integer ',
         'use(0 : No setting, 1:Manual Searching, 2 : Auto Searching)\n']
        '''
        variable__name = text_func.extract_var_name(raw_dataList[0]) # 필수항목


        for raw_data__data in raw_dataList:
            if 'var' in raw_data__data:
                variable__desc = text_func.extract_var__description(raw_data__data )  # 필수
                try:
                    saveform = { # 필수 항목
                        "variable__name": variable__name,
                        "variable__desc": variable__desc,
                        "variable__loc": variable__loc,
                    }
                except NameError:
                    print("well, it WASN'T defined after all!")
                else:
                    pass
                    
            if 'type' in raw_data__data:
                variable__type = text_func.extract_var__type(raw_data__data )  # 옵션
                try:
                    saveform["variable__type"]=variable__type
                except NameError:
                    pass
                else:
                    pass
            if 'use' in raw_data__data:
                variable__use = text_func.extract_var__use(raw_data__data )  # 옵션
                try:
                    saveform["variable__use"]= variable__use
                except NameError:
                    pass
                else:
                    pass

            if 'default' in raw_data__data:
                variable__default = text_func.extract_var__use(raw_data__data )  # 옵션
                try:
                    saveform["variable__default"]= variable__default
                except NameError:
                    pass
                else:
                    pass
        result[variable__name]=saveform
    return result

def extract_functionInfo(function_raw:list):
    pass

def extract_labelInfo(label_raw:list):
    pass

def extract_descripInfo(desc_raw:dict):
    result={}
    job_num=desc_raw['job_num']
    raw_data=desc_raw['rawdata']

    for data in raw_data:
        if ('@Description' in data):
            description =data.split(':')[1].strip()
        if ('@Version' in data):
            version =data.split(':')[1].strip()
        if ('@Developer' in data):
            developer =data.split(':')[1].strip()

    try:
        result={
            "description" : description,
            "version" : version,
            "developer":developer
        }

    except NameError:
        print("well, it WASN'T defined after all!")
    else:
        return result

def get_jobnum_list(variable_info:dict):
    '''
    프로그램에 존재하는 중복되지 않은 JOB번호 리스트 반환
    :param variable_info:
    :return:
    '''
    job_list=[]
    for var_name, var_info in variable_info.items():
        job_list.append( var_info['variable__loc'])


    result_list = list(set(job_list) )  # list로 변환
    return result_list


def make_optionList(raw_list: list)->list:
    '''
    raw_list를 option tag로 변환해서 return
    :param raw_list:
    :return: list
    '''
    def convert_htmlOpt(rawdata: str):
        if type(rawdata) == int:
            rawdata = str(rawdata)
        result = '\t\t\t<option>' + rawdata + '</option>\n'
        return result

    result = list(map(convert_htmlOpt, raw_list))
    return result

if __name__=="__main__":
    test_desc_raw={'job_num': '1472_job_description.JOB', 'rawdata': ["'@Description : Auto Teaching Job\n", "'@Version : v1.0 \n", "'@Developer : Park Wonho, park.wonho@hyundai-robotics.com, 010-8332-1697\n"]}
    #print(extract_descripInfo(test_desc_raw))

    testlist = [{'job_num': '5001_Glo_Var.JOB',
                 'rawdata': "gi_Search=1\t'@var Stage Search Method @type Integer @use(0 : No setting, 1:Manual Searching, 2 : Auto Searching)\n"},
                {'job_num': '5001_Glo_Var.JOB', 'rawdata': "gi_glsWidth=0\t'@var Glass Width Size @type Integer\n"},
                {'job_num': '5001_Glo_Var.JOB', 'rawdata': "gi_glsHeight=0\t'@var Glass Height Size @type Integer\n"},
                {'job_num': '5001_Glo_Var.JOB',
                 'rawdata': 'gt_locIP=""\t\'@var local IP Address @type String User-defined\n'},
                {'job_num': '5001_Glo_Var.JOB',
                 'rawdata': 'gt_RemoteIP=""\t\'@var Remote IP Address @type String User-defined\n'},
                {'job_num': '5002_Glo_Var.JOB',
                 'rawdata': 'gi_Lo_port=\t""\'@var Local Port Number @type String User-defined\n'},
                {'job_num': '5001_Glo_Var.JOB',
                 'rawdata': 'gi_Re_port=""\t\'@var Remote Port Number @type String User-defined\n'}]

    dD=extract_varInfo(testlist)

    print(dD)
    print( get_jobnum_list(dD))