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
            '\t\tborder: 1px solid black;\n'
            '\t\tborder-collapse: collapse;\n',
            '\t}\n',

            '\t.variable__table_header{\n',
            '\t\tbackground-color:var(--table_header_color)\n'
            '\t}\n',


            '\t</style>\n', # CSS Setting
            '</head>\n',

            '<body>\n',
                '\t<div class="Status-bar">\n',
                    '\t\t<h1 class="main_title">JOB Document</h1>\n',
                    '\t\t<p class="sub_title">This is a paragraph.</p>\n',
                '\t</div>\n',

             '\t<div class="menu-bar">\n',
                '\t\t<button onclick = "home_btn_func()">Home</button>\n',
                '\t\t<button onclick = "index_btn_func()">Index</button>\n',
                '\t\t<button onclick = "variable_btn_func()">Variable</button>\n',
                '\t\t<button onclick = "function_btn_func()">Function</button>\n',
             '\t</div>\n\n',

             '\t<!-- Main Frame Setting -->\n',
             '\t<div class="main_frame">\n\n',

             '\t\t<div class="description_UI">\n',
             '\t\t</div> <!--description_UI end-->\n\n',

             '\t\t<div class="index_UI">\n',
             '\t\t</div> <!--index_UI end-->\n\n',

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
                # DOM setting
                '\t\tlet description_UI = document.querySelector(".description_UI");\n',
                '\t\tlet index_UI = document.querySelector(".index_UI");\n',
                '\t\tlet variable_UI = document.querySelector(".variable_UI");\n',
                '\t\tlet function_UI = document.querySelector(".function_UI");\n',
                '\t\tlet label_UI = document.querySelector(".label_UI");\n',

                # Variable Definition : All variable is global variable
                '\t\t<!--Btn Variable Setting-->\n',
                '\t\tlet home_btn_activation=false;\n',
                '\t\tlet index_btn_activation=false;\n',
                '\t\tlet variable_btn_activation=false;\n',
                '\t\tlet function_btn_activation=false;\n\n',

                 # Event Setting
                '\t\t<!--Btn Event Function Setting-->\n',

                # Home Button Function________________________________________________________
                '\t\tfunction home_btn_func() {   <!--Home Btn Function-->\n',
                '\t\t\talert("This is a working button1");\n',
                '\t\t\thome_btn_activation=true;\n',
                '\t\t\tindex_btn_activation=false;\n',
                '\t\t\tvariable_btn_activation=false;\n',
                '\t\t\tfunction_btn_activation=false;\n\n',

                '\t\t\tdescription_UI.style.display="block";\n', # Activate
                '\t\t\tindex_UI.style.display="none";\n',
                '\t\t\tvariable_UI.style.display="none";\n',
                '\t\t\tfunction_UI.style.display="none";\n',
                '\t\t\tlabel_UI.style.display="none";\n',
                '\t\t}\n\n',

                # Index Button Function________________________________________________________
                '\t\tfunction index_btn_func() {   <!--Index Btn Function-->\n',
                '\t\t\talert("This is a working button2");\n',
                '\t\t\thome_btn_activation=false;\n',
                '\t\t\tindex_btn_activation=true;\n',
                '\t\t\tvariable_btn_activation=false;\n',
                '\t\t\tfunction_btn_activation=false;\n\n',

                '\t\t\tdescription_UI.style.display="none";\n',
                '\t\t\tindex_UI.style.display="block";\n', # Activate
                '\t\t\tvariable_UI.style.display="none";\n',
                '\t\t\tfunction_UI.style.display="none";\n',
                '\t\t\tlabel_UI.style.display="none";\n',
                '\t\t}\n\n',

                # Variable Button Function________________________________________________________
                '\t\tfunction variable_btn_func() {   <!--Variable Btn Function-->\n',
                '\t\t\thome_btn_activation=false;\n',
                '\t\t\tindex_btn_activation=false;\n',
                '\t\t\tvariable_btn_activation=true;\n',
                '\t\t\tfunction_btn_activation=false;\n',
                '\t\t\talert("This is a working button3");\n\n'
                
                '\t\t\tdescription_UI.style.display="none";\n',
                '\t\t\tindex_UI.style.display="none";\n',
                '\t\t\tvariable_UI.style.display="block";\n', # Activate
                '\t\t\tfunction_UI.style.display="none";\n',
                '\t\t\tlabel_UI.style.display="none";\n',
                '\t\t}\n\n',

                # Function Button Function________________________________________________________
                '\t\tfunction function_btn_func() {   <!--Function Btn Function-->\n',
                '\t\t\thome_btn_activation=false;\n',
                '\t\t\tindex_btn_activation=false;\n',
                '\t\t\tvariable_btn_activation=false;\n',
                '\t\t\tfunction_btn_activation=true;\n',
                '\t\t\talert("This is a working button4");\n\n',

                '\t\t\tdescription_UI.style.display="none";\n',
                '\t\t\tindex_UI.style.display="none";\n',
                '\t\t\tvariable_UI.style.display="none";\n',
                '\t\t\tfunction_UI.style.display="block";\n', # Activate
                '\t\t\tlabel_UI.style.display="none";\n',
                '\t\t}\n\n',

                # Search Button Function________________________________________________________
                '\t\tfunction search_Ok_btn_func(){    <!--search_Ok_btn_func-->\n',
                '\t\t\talert("Searching!");\n',
                '\t\t}\n\n',

                 # Search Button Function________________________________________________________
                 '\t\tfunction init(){\n',
                 '\t\t\tdescription_UI.style.display="block";\n',  # Activate
                 '\t\t\tindex_UI.style.display="none";\n',
                 '\t\t\tvariable_UI.style.display="none";\n',
                 '\t\t\tfunction_UI.style.display="none";\n',
                 '\t\t\tlabel_UI.style.display="none";\n',
                 '\t\t}\n\n',

            # Excution______________________________________________________
            '\t\tinit();\n\n', # init() Excution

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

        description=description_data['description']
        version=description_data['version']
        developer=description_data['developer']

        html_result = [

            '\t\t<div class="description">\n',
            ###########################################################################################
            '\t\t\t<div class="description__description">\n',
                '\t\t\t\t<span class="description__title">\n',
                '\t\t\t\t<i class="fas fa-square"></i> Description : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="description__value">\n',
                '\t\t\t\t'+description+'\n',
                '\t\t\t\t</span>\n',
            '\t\t\t</div>\n',
            ###########################################################################################
            '\t\t\t<div class="description__version">\n',
                '\t\t\t\t<span class="version__title">\n',
                '\t\t\t\t<i class="fas fa-square"></i> Version : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="version__value">\n',
                '\t\t\t\t' + version + '\n',
                '\t\t\t\t</span>\n',
            '\t\t\t</div>\n',
            ###########################################################################################
            '\t\t\t<div class="description__developer">\n',
                '\t\t\t\t<span class="developer__title">\n',
                '\t\t\t\t<i class="fas fa-square"></i> Developer : \n',
                '\t\t\t\t</span>\n',

                '\t\t\t\t<span class="developer__value">\n',
                '\t\t\t\t' + developer + '\n',
                '\t\t\t\t</span>\n',
            '\t\t\t</div>\n',
            ###########################################################################################
            '\t\t</div>\n',

        ]

        self.description_div_list=html_result
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
        var_Table_baseHTML=[
            '\t\t\t\t\t<tr class="variable__table_header">\n'  # Table Header 
            '\t\t\t\t\t<th class="header_index" align="center">Index</th>\n',
            '\t\t\t\t\t<th class="header_variable" align="center">Variable</th>\n',
            '\t\t\t\t\t<th class="header_description" align="center">Description</th>\n',
            '\t\t\t\t\t<th class="header_default" align="center">Default</th>\n',
            '\t\t\t\t\t<th class="header_use" align="center">Use</th>\n',
            '\t\t\t\t\t<th class="header_job" align="center">Job</th>\n',
            '\t\t\t\t\t<th class="header_job" align="center">Type</th>\n',
            '\t\t\t\t\t</tr>\n\n',  # Table Header
        ]
        table_list = []

        def make_colInfo(var_info: dict, index_info: dict):
            new_row = ['-', '-', '-', '-', '-', '-', ]  # '-' : 속성이 없다는 뜻

            # Index / Variable / Description / Default / Use / Job / type

            def write_row(var_info: dict, row: list, property: str) -> list:
                if (var_info.get(property) != None):
                    row[index_info[property]] = var_info[property]
                return row

            # column별 속성 추가하기
            new_row = write_row(var_info, new_row, "variable__name")
            new_row = write_row(var_info, new_row, "variable__desc")
            new_row = write_row(var_info, new_row, "variable__type")
            new_row = write_row(var_info, new_row, "variable__use")
            new_row = write_row(var_info, new_row, "variable__default")
            new_row = write_row(var_info, new_row, "variable__jobNum")

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
            '\t\t\t\t\t<option>Integer</option>\n',
            '\t\t\t\t\t<option>Double</option>\n',
            '\t\t\t\t\t<option>String</option>\n',
            '\t\t\t\t\t<option>Array</option>\n',
            '\t\t\t\t</select>\n',
            '\t\t\t</div><!--variable__selector_type End-->\n\n',  # variable__selector_type

            '\t\t\t<div class="variable__selector_job">\n',  # variable__selector_job
            '\t\t\t\t<span class="Job_name">Job</span>\n',
            '\t\t\t\t<select name="Job" class="Job_selection">\n',
            # 이 부분에 JOB List 추가
            '\t\t\t\t</select>\n'
            '\t\t\t</div><!--variable__selector_job End-->\n\n',  # variable__selector_job

            '\t\t\t</div><!--selector End-->\n\n',  ########################################[SELECTOR]################

            ########################################[Search]################
            '\t\t\t<!--Search Setting-->\n',  # comment
            '\t\t\t<div class="variable__search">\n',
            '\t\t\t<span class="search__title">Search</span>\n',
            '\t\t\t<input type="text" class="search__input" name="name" required minlength="4" maxlength="8" size="10">\n',
            '\t\t\t<button onclick = "search_Ok_btn_func()">ok</button>\n',
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

    def make_var_div2222(self,var_data:dict):
        html_base=[
            '\t\t<div class="variable">\n',
            # Selector Setting
            '\t\t\t<!--Selector Setting-->\n',  # comment

            '\t\t\t<!--variable_search_part-->\n',
            '\t\t\t<div class="variable_search_part">\n',

            '\t\t\t<div class="variable__selector">\n',  ########################################[SELECTOR]################

            '\t\t\t<div class="variable__selector_type">\n',  # variable__selector_type
            '\t\t\t\t<span class="Type_name">Type</span>\n',
            '\t\t\t\t<select name="Type" class="Type_selection">\n',
            '\t\t\t\t\t<option>Integer</option>\n',
            '\t\t\t\t\t<option>Double</option>\n',
            '\t\t\t\t\t<option>String</option>\n',
            '\t\t\t\t\t<option>Array</option>\n',
            '\t\t\t\t</select>\n',
            '\t\t\t</div><!--variable__selector_type End-->\n\n',  # variable__selector_type

            '\t\t\t<div class="variable__selector_job">\n',  # variable__selector_job
            '\t\t\t\t<span class="Job_name">Job</span>\n',
            '\t\t\t\t<select name="Job" class="Job_selection">\n',
            # 이 부분에 JOB List 추가
            '\t\t\t\t</select>\n'
            '\t\t\t</div><!--variable__selector_job End-->\n\n',  # variable__selector_job

            '\t\t\t</div><!--selector End-->\n\n',  ########################################[SELECTOR]################

            ########################################[Search]################
            '\t\t\t<!--Search Setting-->\n',  # comment
            '\t\t\t<div class="variable__search">\n',
            '\t\t\t<span class="search__title">Search</span>\n',
            '\t\t\t<input type="text" class="search__input" name="name" required minlength="4" maxlength="8" size="10">\n',
            '\t\t\t<button onclick = "search_Ok_btn_func()">ok</button>\n',
            '\t\t\t</div>\n\n',
            ########################################[Search]################

            '\t\t\t</div><!--variable_search_part End-->\n\n',

            '\t\t\t<!--variable_table_part-->\n',
            '\t\t\t<div class="variable_table_part">\n',
            '\t\t\t\t<table class="variable__table">\n',
            '\t\t\t\t\t<tr class="variable__table_header">\n'  # Table Header 
            '\t\t\t\t\t<th class="header_index">Index</th>\n',
            '\t\t\t\t\t<th class="header_variable">Variable</th>\n',
            '\t\t\t\t\t<th class="header_description">Description</th>\n',
            '\t\t\t\t\t<th class="header_default">Default</th>\n',
            '\t\t\t\t\t<th class="header_use">Use</th>\n',
            '\t\t\t\t\t<th class="header_job">Job</th>\n',
            '\t\t\t\t\t</tr>\n',  # Table Header

            '\t\t\t\t</table>\n',
            '\t\t\t</div> <!--variable_table_part End-->\n\n',
            ########################################[TABLE]################
            ########################################[TABLE]################

            '\t\t\t</div>   <!--variable End-->\n\n',  # variable end
        ]

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
        result=''.join(self.htmlline)

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
    isfind, location=testObj.find_classLoc("home_UI",testObj.htmlline)
    merged_html=testObj.add_html(testObj.htmlline,testObj.description_div_list,location)


    merged_file = open('merged.html', 'w')
    merged_file.write(testObj.returnHTML_file(merged_html))
    merged_file.close()

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
