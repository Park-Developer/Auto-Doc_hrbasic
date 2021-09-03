from HTML_Generator import HTML_Generator
class Variable_Generator(HTML_Generator):
    def __init__(self,var_data: dict):
        self.var_data=var_data
        self.variable_div_list=[]

    def make_varSearch_part(self):
        def get_jobnum_list(var_data: dict) -> list:
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

        job_numList = get_jobnum_list(self.var_data)

        def make_optionList(job_numList: list) -> list:
            '''
             job_numLis를 option tag로 변환해서 return
            :param raw_list:
            :return: list
            '''

            def convert_htmlOpt(rawdata: str) -> str:  # map function
                if type(rawdata) == int:
                    rawdata = str(rawdata)
                result = '\t\t\t<option>' + rawdata + '</option>\n'
                return result

            result = list(map(convert_htmlOpt, job_numList))
            return result

        self.variable_SearchPart_div_list = make_optionList(job_numList)
        return self.variable_SearchPart_div_list

    def make_varTable_part(self):
        table_list = []
        var_Table_baseHTML = [
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

            def write_row(var_info: dict, index_info: dict, row: list, property: str) -> list:
                if (var_info.get(property) != None):
                    row[index_info[property]] = var_info[property]
                return row

            # column별 속성 추가하기
            new_row = write_row(var_info, index_info, new_row, "variable__name")
            new_row = write_row(var_info, index_info, new_row, "variable__desc")
            new_row = write_row(var_info, index_info, new_row, "variable__type")
            new_row = write_row(var_info, index_info, new_row, "variable__use")
            new_row = write_row(var_info, index_info, new_row, "variable__default")
            new_row = write_row(var_info, index_info, new_row, "variable__loc")

            return new_row

        for var_name, var_info in self.var_data.items():
            new_row = make_colInfo(var_info, HTML_Generator.var_table_index)
            table_list.append(new_row)

        def convert_varTable_toHTML(var_table_list: list, index_info: dict) -> list:
            var_html_table = []

            def make_htmlTag(index, row_info):
                row_html = ['\t\t\t\t\t<tr class="variable__table_row ' + str(index) + '">\n',
                            '\t\t\t\t\t<td class="variable__table_row' + str(index) + '_col0" align="center">' + str(
                                index + 1) + '</td>\n']  # Index Column
                # Index Header에 center align 속성 추가

                # index_info Reverse Version
                reversed_index_info = {}
                for key, value in index_info.items():
                    reversed_index_info[value] = key

                for col_idx, property_value in enumerate(row_info):
                    if ("default" in reversed_index_info[col_idx] or "job" in reversed_index_info[
                        col_idx]):  # default와 job column은 text-align 적용
                        row_html.append(
                            '\t\t\t\t\t<td class="variable__table_row' + str(index) + '_col' + str(
                                col_idx) + '" align="center">' + str(
                                property_value) + '</td>\n')
                    else:
                        row_html.append(
                            '\t\t\t\t\t<td class="variable__table_row' + str(index) + '_col' + str(
                                col_idx) + '">' + str(
                                property_value) + '</td>\n')

                row_html.append('\t\t\t\t\t</tr>\n\n')
                return row_html

            for index, row_info in enumerate(var_table_list):
                var_html_table += make_htmlTag(index, row_info)

            return var_html_table

        self.variable_TablePart_div_list = var_Table_baseHTML + convert_varTable_toHTML(table_list,
                                                                                        HTML_Generator.var_table_index)
        return self.variable_TablePart_div_list


    def make_var_div(self) -> list:
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
            '\t\t\t\t<span class="Type_name"><Strong>Type</Strong></span>\n',
            '\t\t\t\t<select name="Type" class="Type_selection">\n',
            '\t\t\t\t\t<option>All</option>\n',
            '\t\t\t\t\t<option>Integer</option>\n',
            '\t\t\t\t\t<option>Double</option>\n',
            '\t\t\t\t\t<option>String</option>\n',
            '\t\t\t\t\t<option>Array</option>\n',
            '\t\t\t\t\t<option>Pose</option>\n',
            '\t\t\t\t\t<option>Shift</option>\n',
            '\t\t\t\t\t<option>User-defined</option>\n',
            '\t\t\t\t</select>\n',
            '\t\t\t</div><!--variable__selector_type End-->\n\n',  # variable__selector_type

            '\t\t\t<div class="variable__selector_job">\n',  # variable__selector_job
            '\t\t\t\t<span class="Job_name"><Strong>Job</Strong></span>\n',
            '\t\t\t\t<select name="Job" class="Job_selection">\n',
            '\t\t\t\t\t<option>All</option>\n',
            # 이 부분에 JOB List 추가
            '\t\t\t\t</select>\n',
            '\t\t\t</div><!--variable__selector_job End-->\n\n',  # variable__selector_job

            '\t\t\t</div><!--selector End-->\n\n',
            ########################################[SELECTOR]################

            ########################################[Search]################
            '\t\t\t<!--Search Setting-->\n',  # comment
            '\t\t\t<div class="variable__search">\n',
            '\t\t\t<span class="search__title"><Strong>Search</Strong></span>\n',
            '\t\t\t<input type="text" class="variable_search__input" name="name" required minlength="4" maxlength="8" size="10">\n',
            '\t\t\t<button class = "variable_search__btn"><i class="fas fa-search"></i></button>\n',
            '\t\t\t</div>\n\n',
            ########################################[Search]################

            '\t\t\t</div><!--variable_search_part End-->\n\n',

            '\t\t\t<!--variable_table_part-->\n',
            '\t\t\t<div class="variable_table_part">\n',
            '\t\t\t\t<table class="variable__table">\n',

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
        self.make_varSearch_part()
        search_insertClass = HTML_Generator.var_insertInfo["Search"]
        result_html = insert_Div_to_base(html_base, self.variable_SearchPart_div_list, search_insertClass)

        # Table Part
        self.make_varTable_part()
        table_insertClass = HTML_Generator.var_insertInfo["Table"]
        result_html = insert_Div_to_base(result_html, self.variable_TablePart_div_list, table_insertClass)

        # Return & Update
        self.variable_div_list = result_html

    def return_variable_div(self):
        self.make_var_div()
        return self.variable_div_list