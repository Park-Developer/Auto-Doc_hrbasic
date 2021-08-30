from HTML_Generator import HTML_Generator
class Code_Generator(HTML_Generator):
    def __init__(self,code_data: dict):
        self.code_data=code_data
        self.code_div_list=[]
        self.code_SearchPart_div_list=[]
        self.code_TablePart_div_list=[]

    def make_code_div(self) -> list:
        code_html_base = [
            '\t\t<div class="code">\n',
            # Selector Setting
            '\t\t\t<!--code_search_part-->\n',
            '\t\t\t<div class="code_search_part">\n',

            '\t\t\t<div class="code__selector">\n',
            ########################################[SELECTOR]################
            '\t\t\t<div class="code__selector_job">\n',  # variable__selector_job
            '\t\t\t\t<span class="Job_name"><Strong>Job</Strong></span>\n',
            '\t\t\t\t<select name="Job" class="code_Job_selection">\n',
            '\t\t\t\t\t<option>All</option>\n',
            # 이 부분에 JOB List 추가
            '\t\t\t\t</select>\n',
            '\t\t\t</div><!--code__selector_job End-->\n\n',  # variable__selector_job

            '\t\t\t</div><!--selector End-->\n\n',
            ########################################[SELECTOR]################

            ########################################[Search]################
            '\t\t\t<!--Search Setting-->\n',  # comment
            '\t\t\t<div class="code__search">\n',
            '\t\t\t<span class="search__title"><Strong>Search</Strong></span>\n',
            '\t\t\t<input type="text" class="code_search__input" name="name" required minlength="4" maxlength="8" size="10">\n',
            '\t\t\t<button class = "code_search__btn"><i class="fas fa-search"></i></button>\n',
            '\t\t\t</div>\n\n',
            ########################################[Search]################

            '\t\t\t</div><!--code_search_part End-->\n\n',

            '\t\t\t<!--code_table_part-->\n',
            '\t\t\t<div class="code_table_part">\n',
            '\t\t\t\t<table class="code__table">\n',

            '\t\t\t\t</table>\n',
            '\t\t\t</div> <!--code_table_part End-->\n\n',
            ########################################[TABLE]################
            ########################################[TABLE]################

            '\t\t\t</div>   <!--code End-->\n\n',  # variable end
        ]

        # Insert Function
        def insert_Div_to_base(base_html: list, insert_html: list, insert_class) -> list:
            for idx, line in enumerate(base_html):
                if insert_class in line:  # 삽입 위치
                    merged_html = base_html[:idx + 1] + insert_html + base_html[idx + 1:]
                    break
            return merged_html

        # Search Part
        self.make_codeSearch_part()
        search_insertClass = HTML_Generator.code_insertInfo["Search"]
        result_html = insert_Div_to_base(code_html_base , self.code_SearchPart_div_list, search_insertClass)

        # Table Part
        self.make_codeTable_part()
        table_insertClass = HTML_Generator.code_insertInfo["Table"]
        result_html = insert_Div_to_base(result_html, self.code_TablePart_div_list, table_insertClass)

        # Return & Update
        self.code_div_list = result_html

    def make_codeSearch_part(self):
        code_num=0
        job_searchOpt_list=[]
        for code_num,code_data in self.code_data.items():
            code_num+=1
            job_number=code_data['job_num']

            if type(job_number) == int:
                job_number= str(job_number)
            job_searchOpt_list.append('\t\t\t<option>' + job_number+ '</option>\n')

        self.code_SearchPart_div_list = job_searchOpt_list
        return self.code_SearchPart_div_list

    def make_codeTable_part(self):
        pass
        # 여기에 header부분은 하드코딩

    def return_code_div(self):
        self.make_code_div()
        return self.code_div_list