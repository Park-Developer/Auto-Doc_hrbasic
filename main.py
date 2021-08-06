import HTML_Generator as html_ge
import JobReader as job_re
import raw_func

if __name__ == "__main__":
    # JOB 프로그램 읽기
    job_address=r"C:\Users\gnvid\.Nimi Places\Project\HRBASIC AutoDoc\Test code"
    job_reader=job_re.JobReader(job_address)

    job_reader.read_n_make_rawData()
    #print(job_reader.Variable_raw_List)
    #print(job_reader.Function_raw_List)
    #print(job_reader.Label_raw_List)
    #print(job_reader.Job_description)

    descrition_raw_data=job_reader.Job_description
    variable_raw_data=job_reader.Variable_raw_List

    descrition_processed_data = raw_func.extract_descripInfo(descrition_raw_data)
    variable_processed_data = raw_func.extract_varInfo(variable_raw_data)


    html_generator=html_ge.HTML_Generator()
    html_generator.make_description_div(  descrition_processed_data)
    html_generator.make_var_div( variable_processed_data)
    #print("debug")
    #print(html_generator.variable_div_list)
    html_generator.make_varTable_part(variable_processed_data)
    #print(html_generator.variable_TablePart_div_list)


    ## Function Tetst
    function_raw_data=job_reader.Function_raw_List
    function_processed_data=raw_func.extract_functionInfo(function_raw_data)
    print("function deug")
    print(function_processed_data)
    html_generator.make_function_div(function_processed_data)
    print(html_generator.function_div_list)
    html_generator.merge_Allhtml()
    result_html=html_generator.returnHTML_file(html_generator.html_base)
    html_file = open('main_file.html', 'w')
    html_file.write(result_html)
    html_file.close()

