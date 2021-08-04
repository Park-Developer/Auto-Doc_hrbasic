# '@Description : Auto Teaching Job
# '@Version : v1.0
# '@Developer : Park Wonho, park.wonho@hyundai-robotics.com, 010-8332-1697

def extract_descripInfo(desc_raw):
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
    test_desc_raw={'job_num': '1472_job_description.JOB', 'rawdata': ["'@Description : Auto Teaching Job\n", "'@Version : v1.0 \n", "'@Developer : Park Wonho, park.wonho@hyundai-robotics.com, 010-8332-1697\n"]}
    print(extract_descripInfo(test_desc_raw))