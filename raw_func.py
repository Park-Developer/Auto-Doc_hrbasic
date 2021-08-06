import text_func

def extract_varInfo(var_raw:list):
    # rawdata form : {'job_num': '5001_Glo_Var.JOB', 'rawdata': "gi_Search=1\t'@var Stage Search Method @type Integer @use(0 : No setting, 1:Manual Searching, 2 : Auto Searching)\n"}
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
                if ('(' not in result) and (')' not in result )and ('\n' not in result) and ('\t' not in result):
                    break

                if cnt>100:
                    break
                if '(' in result:
                    result = result.replace("(", '')
                if ')' not in result:
                    result = result.replace(")", '')
                if '\n' not in result:
                    result = result.replace("\n", '')
                if '\t' not in result:
                    result = result.replace("\t", '')

            return result.strip()

        for raw_data__data in raw_dataList:
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
        result[variable__name]=saveform
    return result

def extract_functionInfo(function_raw:list):
    processed_funcdata={} # return para

    def extract_property(raw_data:str,property:str):
        property_content=raw_data.split(property)[1]

        while True:
            if ("'" not in property_content) and ('"' not in property_content) and ('\t' not in property_content) and ('\n' not in property_content):
                break

            if "'" in property_content:
                property_content=property_content.replace("'",'')
            if '"' in property_content:
                property_content=property_content.replace('"', '')
            if '\t' in property_content:
                property_content=property_content.replace("\t", '')
            if '\n' in property_content:
                property_content=property_content.replace("\n", '')

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


if __name__=="__main__":
    test_func_raw=[ {'job_num': '5400_error.JOB', 'rawdata': ["' @func Error Handling\n", "' @ref 아직 덜 만듬 ㅋ\n", "' @param li_errCode, li_ProLoc\n"]}]
    print(extract_functionInfo(test_func_raw))
