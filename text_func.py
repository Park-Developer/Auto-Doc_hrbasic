def extract_var_name(raw_data:str):
    if '\t' in raw_data:
        raw_data.replace('\t','')

    if '\n' in raw_data:
        raw_data.replace('\n','')

    if "=" in raw_data:
        raw_data=raw_data.split('=')[0].strip()

    if "DIM" in raw_data:
        raw_data=raw_data.split('DIM')[1]
        raw_data=raw_data.split('AS')[0].strip()

    return raw_data

def extract_var_loc(raw_data:str):
    result=raw_data.split('_')[0].strip()
    return result

def extract_var__description(raw_data:str):
    result=raw_data.replace('var','').strip()
    return result

def extract_var__type(raw_data:str):
    result=raw_data.replace('type','').strip()
    return result

def extract_var__use(raw_data:str):
    result=raw_data.replace('use','').strip()
    if '(' in result:
        result=result.replace('(','').strip()
    if ')' in result:
        result=result.replace(')','').strip()
    if '\n' in result:
        result=result.replace('\n','').strip()
    if '\t' in result:
        result=result.replace('\t','').strip()

    return result