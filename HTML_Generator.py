class HTML_Generator:
    def __init__(self):
         self.html_base=[ # Basic Form
            '<!DOCTYPE html>\n',
            '<html>\n',
            '<head>\n',
            '\t<title>Page Title</title>\n',
            '\t<style>\n', # CSS Setting
            '\t:root{', # CSS Variable Setting
            '\t\t--table_header_color:gray;',
            '\t}',

            '\tbody{\n',
            '\tbackground-color: lightblue;\n',
            '\t}\n',

            # Variable CSS Setting_______________________________
            '\t.variable_search_part{\n',
            '\tdisplay: flex;\n',
            '\t}\n',

            '\t.variable__selector{\n',
            '\t\tdisplay: flex;\n',
            '\t}\n',

            '\t.variable__table{\n',
            '\t\tborder: 1px solid black;\n',
            '\t\tborder-collapse: collapse;\n',
             '\t\ttable-layout:fixed;\n',

            '\t}\n',

            '\t.variable__table_header{\n',
            '\t\tbackground-color:var(--table_header_color)\n',
            '\t}\n',

            # TEST to solve bug
             '\t.header_index{\n',
             '\twidth:30px;\n'
             '\t}\n',

            # Function CSS Setting_______________________________
            '\t.function__table{\n',
            '\t\tborder: 1px solid black;\n'
            '\t\tborder-collapse: collapse;\n',
            '\t}\n',

            '\t.function__table_header{\n',
            '\t\tbackground-color:var(--table_header_color)\n',
            '\t}\n',

            '\t</style>\n', # CSS Setting
            '</head>\n',

            '<body>\n',
                '\t<div class="Status-bar">\n',
                '\t\t<div class="Status-bar__main">\n',
                '\t\t<h1 class="main_title">Job Program Specification</h1>\n',
                '\t\t</div>\n\n',

                '\t\t<div class="program_intro">\n',
                '\t\t<span class="sub_project">This document is based on a Job Program </span>\n',
                '\t\t</div>\n\n',
                '\t</div>\n',

             '\t<div class="menu-bar">\n',
                '\t\t<button class="home_btn">Home</button>\n',
                '\t\t<button class="label_btn">Label</button>\n',
                '\t\t<button class="variable_btn">Variable</button>\n',
                '\t\t<button class="function_btn">Function</button>\n',
             '\t</div>\n\n',

             '\t<!-- Main Frame Setting -->\n',
             '\t<div class="main_frame">\n\n',

             '\t\t<div class="description_UI">\n',
             '\t\t</div> <!--description_UI end-->\n\n',

             '\t\t<div class="label_UI">\n',
             '\t\t</div> <!--label_UI end-->\n\n',

             '\t\t<div class="variable_UI">\n',
             '\t\t</div> <!--variable_UI end-->\n\n',

             '\t\t<div class="function_UI">\n',
             '\t\t</div> <!--function_UI end-->\n\n',

             '\t\t<div class="label_UI">\n',
             '\t\t</div> <!--label_UI end-->\n\n',

             '\t</div> <!--main-frame end-->\n\n',
             # icon Setting
             '\t<script src = "https://kit.fontawesome.com/3dbd9a16b0.js" crossorigin = "anonymous" > </script>\n\n',

             # JS Setting
             '\t<script>\n',

             ########################################[Initial Setting]#####################################

             # | Initial DOM setting|
             # 1. DIV DOM
             '\t\tlet home_UI = document.querySelector(".description_UI");\n',
             '\t\tlet label_UI = document.querySelector(".label_UI");\n',
             '\t\tlet variable_UI = document.querySelector(".variable_UI");\n',
             '\t\tlet function_UI = document.querySelector(".function_UI");\n\n',


             # 2. Button DOM
             '\t\tlet home_btn=document.querySelector(".home_btn");\n',
             '\t\tlet label_btn=document.querySelector(".label_btn");\n',
             '\t\tlet variable_btn=document.querySelector(".variable_btn");\n',
             '\t\tlet function_btn=document.querySelector(".function_btn");\n\n',

             # | Initial Object setting |  : All variable is global variable
             '\t\t<!--Initial Btn Variable Setting-->\n',
             '\t\tlet home_btn_activation=false;\n',
             '\t\tlet label_btn_activation=false;\n',
             '\t\tlet variable_btn_activation=false;\n',
             '\t\tlet function_btn_activation=false;\n\n',

             '\t\t\thome_UI.style.display="block";\n',  # Activate
             '\t\t\tvariable_UI.style.display="none";\n',
             '\t\t\tfunction_UI.style.display="none";\n',
             '\t\t\tlabel_UI.style.display="none";\n\n',

             # | Event Setting|
             # Button Event Setting
             '\t\thome_btn.addEventListener("click",main_Btn_func )\n',
             '\t\tlabel_btn.addEventListener("click", main_Btn_func)\n',
             '\t\tvariable_btn.addEventListener("click", main_Btn_func)\n',
             '\t\tfunction_btn.addEventListener("click", main_Btn_func)\n\n',

             # Button Event Function
             '\t\tfunction main_Btn_func(event){   <!--main button function-->\n',
             '\t\t\tlet button_type=event.target.innerHTML\n',
             '\t\t\tswitch(button_type){\n',
             # [Home Button Click]_______
             '\t\t\t\tcase "Home":\n',
             '\t\t\t\t\thome_btn_activation=true;\n', # activatge
             '\t\t\t\t\tlabel_btn_activation=false;\n',
             '\t\t\t\t\tvariable_btn_activation=false;\n',
             '\t\t\t\t\tfunction_btn_activation=false;\n\n',

             '\t\t\t\t\thome_UI.style.display="block";\n',  # block
             '\t\t\t\t\tlabel_UI.style.display="none";\n',
             '\t\t\t\t\tvariable_UI.style.display="none";\n',
             '\t\t\t\t\tfunction_UI.style.display="none";\n',
             '\t\t\t\t\tbreak;\n\n',
             # [Label Button Click]_______
             '\t\t\t\tcase "Label":\n',
             '\t\t\thome_btn_activation=false;\n',
             '\t\t\tlabel_btn_activation=true;\n', # activate
             '\t\t\tvariable_btn_activation=false;\n',
             '\t\t\tfunction_btn_activation=false;\n\n',

             '\t\t\thome_UI.style.display="none";\n',
             '\t\t\tlabel_UI.style.display="block";\n',  # block
             '\t\t\tvariable_UI.style.display="none";\n',
             '\t\t\tfunction_UI.style.display="none";\n',
             '\t\t\t\t\tbreak;\n\n',
             # [Variable Button Click]______
             '\t\t\tcase "Variable":\n',
             '\t\t\t\thome_btn_activation=false;\n',
             '\t\t\t\tlabel_btn_activation=false;\n',
             '\t\t\t\tvariable_btn_activation=true;\n',  # activate
             '\t\t\t\tfunction_btn_activation=false;\n\n',

             '\t\t\t\thome_UI.style.display="none";\n',
             '\t\t\t\tlabel_UI.style.display="none";\n',
             '\t\t\t\tvariable_UI.style.display="block";\n',  # block
             '\t\t\t\tfunction_UI.style.display="none";\n',
             '\t\t\t\t\tbreak;\n\n',
             # [Function Button Click]______
             '\t\t\tcase "Function":\n',
             '\t\t\t\thome_btn_activation=false;\n',
             '\t\t\t\tlabel_btn_activation=false;\n',
             '\t\t\t\tvariable_btn_activation=false;\n',
             '\t\t\t\tfunction_btn_activation=true;\n\n',   # activate

             '\t\t\t\thome_UI.style.display="none";\n',
             '\t\t\t\tlabel_UI.style.display="none";\n',
             '\t\t\t\tvariable_UI.style.display="none";\n',
             '\t\t\t\tfunction_UI.style.display="block";\n', # block
             '\t\t\t\t\tbreak;\n\n',
             '\t\t\t}\n',
             '\t\t}\n\n',
             ########################################[Description Setting]###############################
             '\t\t<!--Description CONST Setting-->\n',
             '\t\tHEADER_STYLE={\n',
             '\t\t\th1_size:"50px",\n',
             '\t\t\th2_size:"40px",\n',
             '\t\t\th3_size:"30px",\n',
             '\t\t\th4_size:"20px",\n',
             '\t\t\th5_size:"10px",\n',
             '\t\t}\n\n',

             '\t\t<!--Description Function-->\n',
             # function check_Head_MD(line)
             '\t\tfunction check_Head_MD(line){\n',
             '\t\t\tfunction make_md(header,line){\n',
             '\t\t\tlet sentence=line.split(header)\n',
             '\t\t\tlet non_applined_part=sentence[0].trim();\n',
             '\t\t\tlet applied_part=sentence[1].trim();\n',
                
             '\t\tlet result={\n',
             '\t\t\t"non_applied":non_applined_part,\n',
             '\t\t\t"applied":applied_part,\n',
             '\t\t\t"header":header\n',
             '\t\t\t}\n\n',
             '\t\treturn result;',
             '\t\t}\n\n',
             '\t\tlet header;\n',
             '\t\tif (line.indexOf("####")!==-1){\n',
             '\t\theader="####";\n',
             '\t\t}else if (line.indexOf("###")!==-1){\n',
             '\t\theader="###";\n',
             '\t\t}else if (line.indexOf("##")!==-1){\n',
             '\t\theader="##";\n',
             '\t\t}else if (line.indexOf("#")!==-1){\n',
             '\t\theader="#";\n',
             '\t\t}\n',

             '\t\t let result=make_md(header,line);\n',
             '\t\t return result\n',
             '\t\t}\n\n',

             #########@#@#@#@
             #function apply_headerMD(parentNode, md_result, header_style)
             '\t\tfunction apply_headerMD(parentNode, md_result, header_style){\n',
             '\t\t\tfunction decide_font(header, header_style){\n',
             '\t\t\tlet header_size = "h" + header.length + "_size";\n',\
             '\t\t\treturn header_style[header_size];\n\n',
             '\t\t\t}\n\n',
             '\t\theader = md_result["header"];\n',
             '\t\tlet non_applied = document.createElement("span");\n',
             '\t\tnon_applied.innerText = md_result["non_applied"];\n\n',

             '\t\tlet applied = document.createElement("span");\n',
             '\t\tapplied.innerText = md_result["applied"];\n',
             '\t\t applied.style.fontSize = decide_font(header, header_style);\n',

             '\t\tparentNode.innerText = "";\n',
             '\t\tparentNode.appendChild(non_applied);\n',
             '\t\tparentNode.appendChild(applied);\n',
             '\t\t}\n',
             ##############@#@#

             '\t\t<!--Description DOM Setting-->\n',
             '\t\tlet description_readme= document.querySelector(".description_readme");\n\n',
             '\t\tconsole.log("readme",description_readme.childElementCount);\n\n',

             '\t\tlet readmeLine_num=description_readme.childElementCount;\n',
             '\t\tfor(let i=0; i<readmeLine_num;i++){\n',
             '\t\tif(i>=1){ // <!--header 제외-->\n',
             '\t\tlet readline=document.querySelector(".readme_"+(i-1).toString());\n',
             '\t\tlet readline__text=readline.innerText;\n',
             '\t\tif(readline__text.indexOf("#")!==-1){\n',
             '\t\tlet is_HeadMD=check_Head_MD(readline__text);\n',
             '\t\t apply_headerMD(readline,is_HeadMD,HEADER_STYLE)\n',
             '\t\t}\n',
             '\t\t}\n',
             '\t\t}\n',
             ########################################[Variable Setting]##################################

             # |Variable Constant Setting|
             '\t\t<!--Variable CONST Setting-->\n',
             '\t\tconst VARIABLE_TYPE_INDEX = 6;\n',
             '\t\tconst VARIABLE_JOB_INDEX = 5;\n',
             '\t\tconst VARIABLE_NAME_INDEX = 1;\n\n',

             # |Variable DOM setting|
             '\t\t<!--Variable DOM Setting-->\n',
             '\t\tlet variable_table= document.querySelector(".variable__table");\n\n',
             '\t\tlet variable_typeSelector= document.querySelector(".Type_selection");\n\n', # selector
             '\t\tlet variable_jobSelector= document.querySelector(".Job_selection");\n',  # Selector
             '\t\tlet variable_Search= document.querySelector(".variable__search");\n',  # Search
             '\t\tlet variable_Search_Input=document.querySelector(".variable_search__input");\n',  # Search input
             '\t\tlet variable_Search_Btn=document.querySelector(".variable_search__btn");\n',  # Search ok button

             # |Variable Event Setting|
             # (1). Variable Type Selector Event_____________________
             '\t\tvariable_typeSelector.addEventListener("change", () => {\n', # Event Setting
             '\t\tchange_typeSelection();\n',
             '\t\t});\n\n',

             # Type Selection Event Function
             '\t\tfunction change_typeSelection(){\n', # Event function Definition
             '\t\t\ttable_Obj=variable_table;\n',
             '\t\t\tselector_obj=variable_typeSelector;\n',
             '\t\t\tfilter_index=VARIABLE_TYPE_INDEX;\n',
             '\t\t\tfilter_property(table_Obj, selector_obj, filter_index);\n',
             '\t\t}\n\n',

             # (2). Variable Job Selector Event_____________________
             '\t\tvariable_jobSelector.addEventListener("change", () => {\n',  # Event Setting
             '\t\tchange_jobSelection();\n',
             '\t\t});\n\n',

             # Type Selection Event Function
             '\t\tfunction change_jobSelection(){\n',  # Event function Definition
             '\t\t\ttable_Obj=variable_table;\n',
             '\t\t\tselector_obj=variable_jobSelector;\n',
             '\t\t\tfilter_index=VARIABLE_JOB_INDEX;\n',
             '\t\t\tfilter_property(table_Obj, selector_obj, filter_index);\n',
             '\t\t}\n\n',

             # (3). Variable Search Event_____________________
             '\t\tvariable_Search_Btn.addEventListener("click", () => {\n',  # Event Setting
             '\t\tvar_search_Ok_btn_func();\n',
             '\t\t});\n\n',

             # Variable Name Search Event Function
            '\t\tfunction var_search_Ok_btn_func(){    <!--var_search_Ok_btn_func-->\n',
            '\t\t\tlet table_Obj=variable_table;\n',
            '\t\t\tlet input_Obj=variable_Search_Input;\n',
            '\t\t\tlet search_index=VARIABLE_NAME_INDEX;\n\n',
            '\t\t\tsearch_name(table_Obj, input_Obj, search_index)\n',
            '\t\t}\n\n',

            ########################################[Function Setting]################################
             # |Function Constant Setting|
             '\t\t<!--Variable CONST Setting-->\n',
             '\t\tconst FUNCTION_NAME_INDEX = 1;\n\n',

             # |Function DOM setting|
             '\t\t<!--Function DOM Setting-->\n',
             '\t\tlet function_Search_Input=document.querySelector(".function_search__input");\n',  # Search input
             '\t\tlet function_Search_Btn=document.querySelector(".function_search__btn");\n\n',  # Search ok button
             '\t\tlet function_table= document.querySelector(".function__table");\n\n',

             # |Function Event Setting|
             '\t\tfunction_Search_Btn.addEventListener("click", () => {\n',  # Event Setting
             '\t\tfunc_search_Ok_btn_func();\n',
             '\t\t});\n\n',

             # Function Name Search Event Function
             '\t\tfunction func_search_Ok_btn_func(){    <!--func_search_Ok_btn_func-->\n',
             '\t\t\tlet table_Obj=function_table;\n',
             '\t\t\tlet input_Obj=function_Search_Input;\n',
             '\t\t\tlet search_index=FUNCTION_NAME_INDEX ;\n\n',
             '\t\t\tsearch_name(table_Obj, input_Obj, search_index)\n',
             '\t\t}\n\n',

            ########################################[Reuse Function]##################################

             # |Resue Function1| : Seach item
             '\t\tfunction search_name(table_Obj,input_Obj,search_index){    <!--search function-->\n',
             '\t\t\tlet search_text= input_Obj.value;\n',
             '\t\t\tfor(let i=1;i<table_Obj.rows.length;i++){\n',
             '\t\t\t\tif(table_Obj.rows[i].cells[search_index].innerHTML.indexOf(search_text)!=-1){\n',
             '\t\t\t\t\ttable_Obj.rows[i].style.display="";\n',
             '\t\t\t\t}else{\n',
             '\t\t\t\t\ttable_Obj.rows[i].style.display="none";\n',
             '\t\t\t\t}\n',
             '\t\t\t}\n',
             '\t\t}\n\n',

             # |Reuse Function2| : Filter item
             '\t\tfunction filter_property(table_Obj,selector_obj,filter_index){    <!--filter function-->\n',
             '\t\tlet filter_parameter=selector_obj.value;\n',
             '\t\tfor (let i=1; i<table_Obj.rows.length;i++){\n',  # Header행 제외 -> i=1부터 시작
             '\t\t\tif (filter_parameter==="All"){\n',
             '\t\t\ttable_Obj.rows[i].style.display="";\n',
             '\t\t\t}else{\n',
             '\t\t\tif (table_Obj.rows[i].cells[filter_index].innerHTML.indexOf(filter_parameter)!=-1){\n',
             '\t\t\ttable_Obj.rows[i].style.display="";\n',
             '\t\t\t}else{\n',
             '\t\t\ttable_Obj.rows[i].style.display="none";\n',
             '\t\t\t}\n',
             '\t\t}\n',
             '\t\t}\n',
             '\t\t}\n\n',

            # Excution______________________________________________________

            '\t</script>\n',
            '</body>\n',
            '</html>\n',
         ]
         self.description_div_list=[]
         self.variable_div_list=[]
         self.variable_SearchPart_div_list=[]
         self.variable_TablePart_div_list = []
         self.function_div_list=[]
         self.label_div_list=[]
         self.index_div_list = []

         self.div_insert_location={
             # Insert class name : HTML List
              "description_UI": self.description_div_list,
              "index_UI": self.index_div_list,
              "variable_UI":self.variable_div_list,
              "function_UI": self.function_div_list,
              "label_UI":self.label_div_list,
         }

         self.var_table_index={
            # | Variable | Description | Default | Use | Job | type |
            "variable__name":0,
            "variable__desc":1,
            "variable__default":2,
            "variable__use": 3,
            "variable__jobNum":4,
            "variable__type":5,
        }

         self.function_table_index={
         # | Function | Description | Param | Result | Reference |
             "function__name": 0,
             "function__desc": 1,
             "function__param": 2,
             "function__result": 3,
             "function__ref": 4,
         }


         self.var_insertInfo={
            "Search":"Job_selection",
            "Table":"variable__table",
         }
    def update_all_htmlList(self):
        self.div_insert_location["description_UI"]=self.description_div_list
        self.div_insert_location["index_UI"]=self.index_div_list
        self.div_insert_location["variable_UI"]=self.variable_div_list
        self.div_insert_location["function_UI"]=self.function_div_list
        self.div_insert_location["label_UI"]=self.label_div_list

    def make_description_div(self,description_data:dict):
        '''
        description data form : {'description': 'Auto Teaching Job', 'version': 'v1.0', 'developer': 'Park Wonho, park.wonho@hyundai-robotics.com, 010-8332-1697'}
        :param description_data: Not Raw Data, only processed data
        :return: html div part for description (list)
        '''

        base_html_head=['\t\t<div class="description">\n']
        base_html_tail=['\t\t</div> <!--description END-->  \n\n']
        body_html=[]

        if "description" in description_data:
            description = description_data['description']
            description_html=[
                '\t\t\t<div class="description__description">\n',
                '\t\t\t\t<span class="description__title">\n',
                '\t\t\t\t<i class="fas fa-square"></i> Description : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="description__value">\n',
                '\t\t\t\t'+description+'\n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>\n\n'
            ]
            body_html+=description_html

        if 'version' in description_data:
            version = description_data['version']
            version_html=[
                '\t\t\t<div class="description__version">\n',
                '\t\t\t\t<span class="version__title">\n',
                '\t\t\t\t<i class="fas fa-square"></i> Version : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="version__value">\n',
                '\t\t\t\t' + version + '\n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>\n\n',
            ]
            body_html +=version_html

        if 'revdate' in description_data:
            revdate = description_data['revdate']
            revdate_html=[
                '\t\t\t<div class="description__revdate">\n',
                '\t\t\t\t<span class="revdate__title">\n',
                '\t\t\t\t<i class="fas fa-square"></i> Rev Date : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="revdate__value">\n',
                '\t\t\t\t' + revdate + '\n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>\n\n',
            ]
            body_html+= revdate_html

        if ('name' in description_data) or ('email' in description_data) or ('phone' in description_data):
            developer_html=[
                '\t\t\t<div class="description__name">\n',
                '\t\t\t\t<span class="name__title">\n',
                '\t\t\t\t<i class="fas fa-square"></i> Developer \n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>\n\n',
            ]
            body_html += developer_html

        if 'name' in description_data:
            name = description_data['name']
            name_html=[
                '\t\t\t<div class="description__name">\n',
                '\t\t\t\t<span class="name__title">\n',
                '\t\t\t\t<i class="fas fa-circle"></i> name : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="name__value">\n',
                '\t\t\t\t' + name + '\n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>\n\n',
            ]
            body_html+=name_html

        if 'email' in description_data:
            email = description_data['email']
            email_html=[
                '\t\t\t<div class="description__email">\n',
                '\t\t\t\t<span class="email__title">\n',
                '\t\t\t\t<i class="fas fa-circle"></i> email : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="email__value">\n',
                '\t\t\t\t' + email + '\n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>\n\n',
            ]
            body_html+= email_html

        if 'phone' in description_data:
            phone = description_data['phone']
            phone_html=[
                '\t\t\t<div class="description_phone">\n',
                '\t\t\t\t<span class="phone__title">\n',
                '\t\t\t\t<i class="fas fa-circle"></i> phone : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="phone__value">\n',
                '\t\t\t\t' + phone + '\n',
                '\t\t\t\t</span>\n',
                '\t\t\t</div>  <!--class="description_phone END-->\n\n',
            ]
            body_html += phone_html

        if 'readme' in description_data:

            readme=description_data['readme']
            readme_html_head=['\t\t\t<div class="description_readme">\n'
                              '\t\t\t\t<span class="readme__title">\n',
                              '\t\t\t\t<i class="fas fa-square"></i> Notice : \n',
                              '\t\t\t\t<br></span>\n',
                              ]
            readme_html_tail = ['\t\t\t</div>\n\n']
            readme_html_body = []
            for idx, line in enumerate(readme):
                class_name="readme_"+str(idx)
                html_line=['\t\t\t\t<span class="'+class_name+'">\n',
                           '\t\t\t\t\t'+line+'\n',
                           '\t\t\t\t<br></span>\n']

                readme_html_body+=html_line

            body_html +=(readme_html_head+ readme_html_body+readme_html_tail)

        self.description_div_list=base_html_head+body_html+base_html_tail
        self.update_all_htmlList()

    def make_varSearch_part(self, var_data: dict):
        def get_jobnum_list(var_data: dict)->list:
            '''
            프로그램에 존재하는 중복되지 않은 JOB번호 리스트 반환
            :param variable_info:
            :return:
            '''
            job_list = []
            for var_name, var_info in var_data.items():
                job_list.append(var_info['variable__loc'])

            result_list = list(set(job_list))  # list로 변환
            return result_list

        job_numList=get_jobnum_list(var_data)

        def make_optionList( job_numList: list) -> list:
            '''
             job_numLis를 option tag로 변환해서 return
            :param raw_list:
            :return: list
            '''

            def convert_htmlOpt(rawdata: str)->str: # map function
                if type(rawdata) == int:
                    rawdata = str(rawdata)
                result = '\t\t\t<option>' + rawdata + '</option>\n'
                return result

            result = list(map(convert_htmlOpt,  job_numList))
            return result

        self.variable_SearchPart_div_list= make_optionList(job_numList)
        return self.variable_SearchPart_div_list

    def make_varTable_part(self,var_data:dict):
        table_list = []
        var_Table_baseHTML=[
            '\t\t\t\t\t<tr class="variable__table_header">\n',  # Table Header
            '\t\t\t\t\t<th class="header_index" align="center">Index</th>\n',
            '\t\t\t\t\t<th class="header_variable" align="center">Variable</th>\n',
            '\t\t\t\t\t<th class="header_description" align="center">Description</th>\n',
            '\t\t\t\t\t<th class="header_default" align="center">Default</th>\n',
            '\t\t\t\t\t<th class="header_use" align="center">Use</th>\n',
            '\t\t\t\t\t<th class="header_job" align="center">Job</th>\n',
            '\t\t\t\t\t<th class="header_job" align="center">Type</th>\n',
            '\t\t\t\t\t</tr>\n\n',  # Table Header

        ]

        def make_colInfo(var_info: dict, index_info: dict):
            new_row = ['-', '-', '-', '-', '-', '-', ]  # '-' : 속성이 없다는 뜻

            # / Variable / Description / Default / Use / Job / Type }

            def write_row(var_info: dict, index_info: dict,row: list, property: str) -> list:
                if (var_info.get(property) != None):
                    row[index_info[property]] = var_info[property]
                return row

            # column별 속성 추가하기
            new_row = write_row(var_info, index_info, new_row, "variable__name")
            new_row = write_row(var_info, index_info, new_row, "variable__desc")
            new_row = write_row(var_info, index_info, new_row, "variable__type")
            new_row = write_row(var_info, index_info, new_row, "variable__use")
            new_row = write_row(var_info, index_info, new_row, "variable__default")
            new_row = write_row(var_info, index_info, new_row, "variable__jobNum")

            return new_row

        for var_name, var_info in var_data.items():
            new_row = make_colInfo(var_info, self.var_table_index)
            table_list.append(new_row)


        def convert_varTable_toHTML(var_table_list: list, index_info: dict) -> list:
            var_html_table = []

            def make_htmlTag(index, row_info):
                row_html = ['\t\t\t\t\t<tr class="variable__table_row '+ str(index) + '">\n',
                            '\t\t\t\t\t<td class="variable__table_row' + str(index) + '_col0" align="center">' + str(index+1) + '</td>\n'] # Index Column
                # Index Header에 center align 속성 추가

                # index_info Reverse Version
                reversed_index_info={}
                for key,value in index_info.items():
                    reversed_index_info[value]=key

                for col_idx, property_value in enumerate(row_info):
                    if("default" in reversed_index_info[col_idx] or "job" in reversed_index_info[col_idx]): # default와 job column은 text-align 적용
                        row_html.append(
                            '\t\t\t\t\t<td class="variable__table_row' + str(index) + '_col' + str(col_idx) + '" align="center">' + str(
                                property_value) + '</td>\n')
                    else:
                        row_html.append(
                            '\t\t\t\t\t<td class="variable__table_row' + str(index) + '_col' + str(col_idx) + '">' + str(
                                property_value) + '</td>\n')

                row_html.append('\t\t\t\t\t</tr>\n\n')
                return row_html

            for index, row_info in enumerate(var_table_list):
                var_html_table += make_htmlTag(index, row_info)

            return var_html_table

        self.variable_TablePart_div_list= var_Table_baseHTML+convert_varTable_toHTML(table_list,self.var_table_index)
        return self.variable_TablePart_div_list



    def make_var_div(self,var_data:dict)->list:
        # Variable base HTML frame
        html_base = [
            '\t\t<div class="variable">\n',
            # Selector Setting
            '\t\t\t<!--Selector Setting-->\n',  # comment

            '\t\t\t<!--variable_search_part-->\n',
            '\t\t\t<div class="variable_search_part">\n',

            '\t\t\t<div class="variable__selector">\n',
            ########################################[SELECTOR]################

            '\t\t\t<div class="variable__selector_type">\n',  # variable__selector_type
            '\t\t\t\t<span class="Type_name">Type</span>\n',
            '\t\t\t\t<select name="Type" class="Type_selection">\n',
            '\t\t\t\t\t<option>All</option>\n',
            '\t\t\t\t\t<option>Integer</option>\n',
            '\t\t\t\t\t<option>Double</option>\n',
            '\t\t\t\t\t<option>String</option>\n',
            '\t\t\t\t\t<option>Array</option>\n',
            '\t\t\t\t</select>\n',
            '\t\t\t</div><!--variable__selector_type End-->\n\n',  # variable__selector_type

            '\t\t\t<div class="variable__selector_job">\n',  # variable__selector_job
            '\t\t\t\t<span class="Job_name">Job</span>\n',
            '\t\t\t\t<select name="Job" class="Job_selection">\n',
            '\t\t\t\t\t<option>All</option>\n',
            # 이 부분에 JOB List 추가
            '\t\t\t\t</select>\n'
            '\t\t\t</div><!--variable__selector_job End-->\n\n',  # variable__selector_job

            '\t\t\t</div><!--selector End-->\n\n',  ########################################[SELECTOR]################

            ########################################[Search]################
            '\t\t\t<!--Search Setting-->\n',  # comment
            '\t\t\t<div class="variable__search">\n',
            '\t\t\t<span class="search__title">Search</span>\n',
            '\t\t\t<input type="text" class="variable_search__input" name="name" required minlength="4" maxlength="8" size="10">\n',
            '\t\t\t<button class = "variable_search__btn"><i class="fas fa-search"></i></button>\n',
            '\t\t\t</div>\n\n',
            ########################################[Search]################

            '\t\t\t</div><!--variable_search_part End-->\n\n',

            '\t\t\t<!--variable_table_part-->\n',
            '\t\t\t<div class="variable_table_part">\n',
            '\t\t\t\t<table class="variable__table">\n',
            #'\t\t\t\t\t<tr class="variable__table_header">\n'  # Table Header
            #'\t\t\t\t\t<th class="header_index">Index</th>\n',
            #'\t\t\t\t\t<th class="header_variable">Variable</th>\n',
            #'\t\t\t\t\t<th class="header_description">Description</th>\n',
            #'\t\t\t\t\t<th class="header_default">Default</th>\n',
            #'\t\t\t\t\t<th class="header_use">Use</th>\n',
            #'\t\t\t\t\t<th class="header_job">Job</th>\n',
            #'\t\t\t\t\t</tr>\n',  # Table Header

            '\t\t\t\t</table>\n',
            '\t\t\t</div> <!--variable_table_part End-->\n\n',
            ########################################[TABLE]################
            ########################################[TABLE]################

            '\t\t\t</div>   <!--variable End-->\n\n',  # variable end
        ]

        # Insert Function
        def insert_Div_to_base(base_html: list, insert_html: list, insert_class) -> list:
            for idx, line in enumerate(base_html):
                if insert_class in line:  # 삽입 위치
                    merged_html = base_html[:idx + 1] + insert_html + base_html[idx + 1:]
                    break
            return merged_html

        # Search Part
        self.make_varSearch_part(var_data)
        search_insertClass=self.var_insertInfo["Search"]
        result_html=insert_Div_to_base(html_base,self.variable_SearchPart_div_list, search_insertClass)

        # Table Part
        self.make_varTable_part(var_data)
        table_insertClass=self.var_insertInfo["Table"]
        result_html=insert_Div_to_base(result_html,self.variable_TablePart_div_list,table_insertClass)

        # Return & Update
        self.variable_div_list = result_html
        self.update_all_htmlList()

        def get_jobnum_list(var_data: dict)->list:
            '''
            프로그램에 존재하는 중복되지 않은 JOB번호 리스트 반환
            :param variable_info:
            :return:
            '''
            job_list = []
            for var_name, var_info in var_data.items():
                job_list.append(var_info['variable__loc'])

            result_list = list(set(job_list))  # list로 변환
            return result_list

        job_numList=get_jobnum_list(var_data)

        def make_optionList( job_numList: list) -> list:
            '''
             job_numLis를 option tag로 변환해서 return
            :param raw_list:
            :return: list
            '''

            def convert_htmlOpt(rawdata: str)->str: # map function
                if type(rawdata) == int:
                    rawdata = str(rawdata)
                result = '\t\t\t<option>' + rawdata + '</option>\n'
                return result

            result = list(map(convert_htmlOpt,  job_numList))
            return result

        job_optionList= make_optionList(job_numList)


        self.update_all_htmlList()

    def returnHTML_basicForm(self):
        '''
        최종적으로 만들어진 html 파일을 반환
        :return: HTML file
        '''
        result=''.join(self.html_base)

        return result

    def returnHTML_file(self,html_list:list):
        '''
        html list를 HTML파일로 만들어 반환
        :param html_list:
        :return:
        '''
        result=''.join(html_list)

        return result

    def find_classLoc(self,class_name:str,htmlline:list):
        '''
        class name을 이용하여 htmlline에서 해당 라인이 있는 위치 반환
        :param class_name: 
        :param htmlline: 
        :return: (is_find, class_loc)  /   is_find : 존재 유무, class_loc : htmlline에서의 index
        '''
        is_find=False
        class_loc=-1

        target_sentence='class="'+class_name
        
        for idx,line in enumerate(htmlline):
            if target_sentence in line:
                is_find = True
                class_loc = idx
                break
        
        return (is_find, class_loc)        

    def add_html(self, basic_html:list, operand_html:list,addtion_loc:int):
        '''
        basic_html의 addition_loc 위치에 operatnd html 삽입 후, 합쳐진 html list 반환        
        삽입 컨셉 : 클래스 정의 라인 밑에 삽입
        
        :param basic_html: 
        :param operand_html: 
        :param addtion_loc: 
        :return: 
        '''
        addtion_start_loc=addtion_loc+1 # 클래스 태그 다음에 삽입
        merged_htm1=basic_html[:addtion_start_loc]+operand_html+basic_html[addtion_start_loc:]

        return merged_htm1

    def merge_Allhtml(self):
        try:
            if (self.html_base==[]):
                raise Exception("No HTML Base")

            def find_classLoc(base_html:list,class_name:str)->dict:
                result = {
                    "is_find": False,
                    "location": -1,
                }
                for idx, line in enumerate(base_html):
                    if class_name in line:  # 삽입 위치
                        result = {
                            "is_find":True,
                            "location":idx,
                        }
                        break
                return result

            def insert_to_basehtml(base_html:list,insert_html:list,insert_loc:int)->list:
                result = base_html[:insert_loc] + insert_html + base_html[insert_loc:]
                return result

            for insert_className,insert_html in self.div_insert_location.items():
                if (insert_html!=[]):
                    find_result=find_classLoc(self.html_base, insert_className)
                    if find_result["is_find"] == True:
                        insert_loc = find_result["location"] + 1
                        self.html_base=insert_to_basehtml( self.html_base, insert_html, insert_loc)

        except Exception as e:
            print("An exception occurred: ", e)


    ################FUNCTION RELATED############################
    def make_function_div(self,func_data:dict):
        table_list = []
        function_table_frontHTML=[
            '\t\t\t<div class="function">\n',
            '\t<!--Function Search Setting-->\n',  # comment
            '\t<div class="function__search">\n',
            '\t<span class="function_search__title">Search</span>\n',
            '\t<input type="text" class="function_search__input" name="name" required minlength="4" maxlength="8" size="10">\n',
            '\t<button class ="function_search__btn"><i class="fas fa-search"></i></button>\n',
            '\t</div>\n\n',
            '\t\t\t\t<table class="function__table">\n',
            '\t\t\t\t\t<tr class="function__table_header">\n',  # Table Header
            '\t\t\t\t\t<th class="header_index" align="center">Index</th>\n',
            '\t\t\t\t\t<th class="header_variable" align="center">Function</th>\n',
            '\t\t\t\t\t<th class="header_description" align="center">Description</th>\n',
            '\t\t\t\t\t<th class="header_default" align="center">Param</th>\n',
            '\t\t\t\t\t<th class="header_use" align="center">Result</th>\n',
            '\t\t\t\t\t<th class="header_job" align="center">Reference</th>\n',
            '\t\t\t\t\t</tr>\n\n',  # Table Header
        ]
        function_table_rearHTML = [
            '\t\t\t\t</table>\n',
            '\t\t\t</div>   <!--function End-->\n\n',
        ]

        def make_colInfo(function_info: dict, func_index_info: dict)->list:
            new_row = ['-', '-', '-', '-', '-', ]  # '-' : 속성이 없다는 뜻
            # | Function | Description | Param | Result | Reference |

            def write_row(func_info: dict, index_info: dict, row: list, property: str) -> list:
                if (func_info.get(property) != None):
                    row[index_info[property]] = func_info[property]
                return row

            # Column에 속성 추가하기
            new_row = write_row(function_info, func_index_info, new_row, "function__name")
            new_row = write_row(function_info, func_index_info, new_row, "function__desc")
            new_row = write_row(function_info, func_index_info, new_row, "function__param")
            new_row = write_row(function_info, func_index_info, new_row, "function__result")
            new_row = write_row(function_info, func_index_info, new_row, "function__ref")

            return new_row

        for func_name,func_info in func_data.items():
            new_row= make_colInfo(func_info, self.function_table_index)
            table_list.append(new_row)

        def convert_funcTable_toHTML(func_table_list: list, func_index_info: dict) -> list:
            func_html_table = []

            def make_htmlTag(index, row_info):
                row_html = ['\t\t\t\t\t<tr class="function__table_row ' + str(index) + '">\n',
                            '\t\t\t\t\t<td class="function__table_row' + str(index) + '_col0" align="center">' + str(
                                index + 1) + '</td>\n']  # Index Column
                # Index Header에 center align 속성 추가

                # index_info Reverse Version
                reversed_index_info = {}
                for key, value in func_index_info.items():
                    reversed_index_info[value] = key

                for col_idx, property_value in enumerate(row_info):

                    row_html.append('\t\t\t\t\t<td class="function__table_row' + str(index) + '_col'
                                    + str(col_idx) + '">' + str(property_value) + '</td>\n'
                                    )

                row_html.append('\t\t\t\t\t</tr>\n\n')
                return row_html

            for index, row_info in enumerate(func_table_list):
                func_html_table += make_htmlTag(index, row_info)

            return func_html_table

        # HTML Struncture
        # front HTML + Converted HTML + rear HTML
        self.function_div_list= function_table_frontHTML+convert_funcTable_toHTML(table_list,self.function_table_index)+ function_table_rearHTML
        self.update_all_htmlList()

if __name__ == "__main__":
    testObj=HTML_Generator();

    html_file = open('html_file.html', 'w')
    html_file.write( testObj.returnHTML_basicForm())
    html_file.close()


    print('FOR TEST')
    test_descdata={'description': 'Auto Teaching Job', 'version': 'v1.0', 'developer': 'Park Wonho, park.wonho@hyundai-robotics.com, 010-8332-1697'}
    testObj.make_description_div(test_descdata)
    desc_file = open('desc_file.html', 'w')
    desc_file.write(testObj.returnHTML_file(testObj.description_div_list))
    desc_file.close()

    # TEST
    # 삽입할 위칭


    # TEST
    test_html=[
        '<!DOCTYPE html>\n',
        '<html>\n',
        '<head>\n',
        '\t<title>Page Title</title>\n',
        '\t<style>\n',  # CSS Setting
        '\tbody{\n',
        '\tbackground-color: lightblue;\n',
        '\t}\n',
        '\t.variable_search_part{\n',
        '\tdisplay: flex;\n',
        '\t}\n',

        '\t.variable__selector{\n',
        '\t\tdisplay: flex;\n',
        '\t}\n',

        '\t.variable__table{\n',
        '\t\tborder: 1px solid black;\n'
        '\t\tborder-collapse: collapse;\n',
        '\t}\n',

        '\t</style>\n',  # CSS Setting
        '</head>\n',

        '<body>\n',
        '<div class="variable">\n',
        # Selector Setting
        '\t<!--Selector Setting-->\n', # comment

        '\t<!--variable_search_part-->\n',
        '\t<div class="variable_search_part">\n',


        '\t<div class="variable__selector">\n', ########################################[SELECTOR]################

        '\t<div class="variable__selector_type">\n', # variable__selector_type
        '\t\t<span class="Type_name">Type</span>\n',
        '\t\t<select name="Type" class="Type_selection">\n',
        '\t\t\t<option>Integer</option>\n',
        '\t\t\t<option>Double</option>\n',
        '\t\t\t<option>String</option>\n',
        '\t\t\t<option>Array</option>\n',
        '\t\t</select>\n'
        '\t</div><!--variable__selector_type End-->\n\n', # variable__selector_type

        '\t<div class="variable__selector_job">\n',  # variable__selector_job
        '\t\t<span class="Job_name">Job</span>\n',
        '\t\t<select name="Job" class="Job_selection">\n',
        # 이 부분에 JOB List 추가
        '\t\t</select>\n'
        '\t</div><!--variable__selector_job End-->\n\n',  # variable__selector_job


        '\t</div><!--selector End-->\n\n',########################################[SELECTOR]################

        ########################################[Search]################
        '\t<!--Search Setting-->\n',  # comment
        '\t<div class="variable__search">\n',
        '\t<span class="search__title">Search</span>\n',
        '\t<input type="text" class="search__input" name="name" required minlength="4" maxlength="8" size="10">\n'
        '\t</div>\n\n',
        ########################################[Search]################

        '\t</div><!--variable_search_part End-->\n\n',

        '\t<!--variable_table_part-->\n',
        '\t<div class="variable_table_part">\n',
        '\t\t<table class="variable__table">\n',
        '\t\t\t<tr class="variable__table_header">\n' # Table Header 
        '\t\t\t<th class="header_index">Index</th>\n',
        '\t\t\t<th class="header_variable">Variable</th>\n',
        '\t\t\t<th class="header_description">Description</th>\n',
        '\t\t\t<th class="header_default">Default</th>\n',
        '\t\t\t<th class="header_use">Use</th>\n',
        '\t\t\t<th class="header_job">Job</th>\n',
        '\t\t\t</tr>\n',  # Table Header
        
        '\t\t</table>',
        '\t</div> <!--variable_table_part End-->\n\n',
        ########################################[TABLE]################
        ########################################[TABLE]################


        '</div>   <!--variable End-->\n\n', # variable end
        '</body>\n',
        '</html>\n',
        ]
    job_numlist=['\t\t\t<option>5001</option>\n',
                 '\t\t\t<option>5002</option>\n',
                 '\t\t\t<option>5003</option>\n']


    for idx,line in enumerate(test_html):
        if 'class="Job_selection"' in line:
            test_result=test_html[:idx+1]+job_numlist+test_html[idx+1:]

    test_file = open('test.html', 'w')
    test_file.write(testObj.returnHTML_file(test_result))
    test_file.close()
