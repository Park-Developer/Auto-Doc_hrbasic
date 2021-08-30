def extract_varInfo(var_raw:list):
    # rawdata form : {'job_num': '5001_Glo_Var.JOB', 'rawdata': "gi_Search=1\t'@var Stage Search Method @type Integer @use(0 : No setting, 1:Manual Searching, 2 : Auto Searching)\n"}
    class varData(): # 중복 키 생성을 위한 Class
        def __init__(self,name):
            self.name = name
        def __repr__(self):
            return self.name

    result={}

    def extract_var_name(raw_data: str) -> str:
        if '\t' in raw_data:
            raw_data.replace('\t', '')

        if '\n' in raw_data:
            raw_data.replace('\n', '')

        if "=" in raw_data:
            raw_data = raw_data.split('=')[0].strip()

        if "DIM" in raw_data:
            raw_data = raw_data.split('DIM')[1]
            raw_data = raw_data.split('AS')[0].strip()

        return  raw_data

    def extract_var_loc(raw_data: str):
        result = raw_data.split('_')[0].strip()
        return result

    for rawdata in var_raw:
        job_num=rawdata["job_num"]
        raw_data=rawdata["rawdata"]

        variable__loc=extract_var_loc(job_num)

        raw_dataList= raw_data.split('@')

        '''
        raw_dataList Form
        ["gi_Search=1\t'",
         'var Stage Search Method ',
         'type Integer ',
         'use(0 : No setting, 1:Manual Searching, 2 : Auto Searching)\n']
        '''

        variable__name = extract_var_name(raw_dataList[0]) # 필수항목

        def extract_var_property(raw_data,property):
            result=raw_data.replace(property,'')

            cnt=0
            while True:
                cnt+=1
                if ('(' not in result) and (')' not in result )and ('\n' not in result) and ('\t' not in result) and (':' not in result):
                    break

                if cnt>100:
                    break
                if '(' in result:
                    result = result.replace("(", '')
                if ')' in result:
                    result = result.replace(")", '')
                if '\n' in result:
                    result = result.replace("\n", '')
                if '\t' in result:
                    result = result.replace("\t", '')
                if ':' in result:
                    result = result.replace(":", '')
            return result.strip()

        for raw_data__data in raw_dataList[1:]:
            if 'var' in raw_data__data:
                variable__desc = extract_var_property(raw_data__data,'var')  # 필수
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
                variable__type =  extract_var_property(raw_data__data,'type')  # 옵션
                try:
                    saveform["variable__type"]=variable__type
                except NameError:
                    pass
                else:
                    pass
            if 'use' in raw_data__data:
                variable__use =  extract_var_property(raw_data__data,'use')  # 옵션
                try:
                    saveform["variable__use"]= variable__use
                except NameError:
                    pass
                else:
                    pass

            if 'default' in raw_data__data:
                variable__default =  extract_var_property(raw_data__data,'default')  # 옵션
                try:
                    saveform["variable__default"]= variable__default
                except NameError:
                    pass
                else:
                    pass
        result[varData(variable__name)]=saveform
    return result

def extract_functionInfo(function_raw:list):
    processed_funcdata={} # return para

    def extract_property(raw_data:str,property:str):
        property_content=raw_data.split(property)[1]

        while True:
            if (":" not in property_content) and ("'" not in property_content) and ('"' not in property_content) and ('\t' not in property_content) and ('\n' not in property_content):
                break

            if "'" in property_content:
                property_content=property_content.replace("'",'')
            if '"' in property_content:
                property_content=property_content.replace('"', '')
            if '\t' in property_content:
                property_content=property_content.replace("\t", '')
            if '\n' in property_content:
                property_content=property_content.replace("\n", '')
            if ':' in property_content:
                property_content=property_content.replace(":", '')
        return property_content.strip()

    for func_data in function_raw:
        jobfile_name=func_data["job_num"]
        job_info=func_data["rawdata"]
        func_obj = {}

        func_obj["function__name"]= jobfile_name
        for property_data in job_info:
            if "@func" in property_data:
                func_obj["function__desc"]= extract_property(property_data,"@func")
            if "@ref" in property_data:
                func_obj["function__ref"]= extract_property(property_data,"@ref")
            if "@param" in property_data:
               func_obj["function__param"]= extract_property(property_data,"@param")
            if "@result" in property_data:
                func_obj["function__result"]= extract_property(property_data,"@result")

        processed_funcdata[jobfile_name]=func_obj

    return processed_funcdata

def extract_labelInfo(label_raw:list):
    pass

def extract_descripInfo(desc_raw:dict):
    result={}
    job_num=desc_raw['job_num']
    raw_data=desc_raw['rawdata']

    if 'readme' in desc_raw:
        processed_readme = []
        for readme_line in desc_raw['readme']:

            while True:
                if ("\t" not in readme_line) and ("'" not in readme_line) and ("\n" not in readme_line) \
                        and ("/@read" not in readme_line) and ("@read/" not in readme_line):
                    break

                if "\t" in readme_line:
                    readme_line = readme_line.replace("\t", "").strip()
                if "'" in readme_line:
                    readme_line = readme_line.replace("'", "").strip()
                if "\n" in readme_line:
                    readme_line = readme_line.replace("\n", "").strip()

                if "@read/" in readme_line:
                    readme_line = readme_line.replace("@read/", "")

                if "/@read" in readme_line:
                    readme_line = readme_line.replace("/@read", "")

            processed_readme.append(readme_line)

        result["readme"] = processed_readme

    for data in raw_data:
        if ('@Description' in data):
            description =data.split(':')[1].strip()
            result["description"]=description

        if ('@Version' in data):
            version =data.split(':')[1].strip()
            result["version"] = version

        if ('@Revdate' in data):
            revdate = data.split(':')[1].strip()
            result["revdate"] = revdate

        if ('@name' in data):
            name = data.split(':')[1].strip()
            result["name"] = name

        if ('@email' in data):
            email = data.split(':')[1].strip()
            result["email"] = email

        if ('phone' in data):
            phone = data.split(':')[1].strip()
            result["phone"] = phone

    return result

def extract_code_property(code_raw:dict)->dict:
    raw_data=code_raw['rawdata']

    pure_comment_part=[] # 주석만 있는 부분
    mixed_comment_part=[] # 주석이랑 코드가 섞여있는 부분
    for line in raw_data:
        if "'" in line:
            temp=line.split("'")
            code_part=temp[0]
            comment_part=temp[1]
            if (code_part.strip()==""):
                pure_comment_part.append(line)
            else:
                mixed_comment_part.append(line)
        else:
            # 주석이 아이에 없는 부분
            mixed_comment_part.append(line)

    result={
    "job_num":code_raw['job_num'].split('_')[0].strip(),
    "code_num":code_raw['code_num'],
    "raw_data":raw_data,
    "pureComment_part":pure_comment_part,
    "mixedComment_part":mixed_comment_part,
    }
    return result

def extract_codeInfo(code_list:list)->dict:
    processed_codedata = {}  # return para
    for idx,value in enumerate(code_list):
        code_num=value["code_num"]
        reference_name="code_#"+str(code_num)
        code_property=extract_code_property(value)
        processed_codedata[reference_name]=code_property

    return processed_codedata


if __name__=="__main__":
    test_func_raw=[{'job_num': '5000_Main.JOB', 'rawdata': 'DIM lt_userIn AS String \'@var User Input @type : String @use "Y","N" @default "none"\n'}, {'job_num': '5005_UDPSetting.JOB', 'rawdata': 'DIM lt_userIn AS String \'@var User Input @type : String2 @use "Y2","N2" @default "test"\n'}]
    print(extract_varInfo(test_func_raw))
