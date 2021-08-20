from HTML_Generator import HTML_Generator
class Function_Generator(HTML_Generator):
    def __init__(self,function_data: dict):
        self.function_div_list = []
        self.func_data=function_data

    def make_function_div(self):
        table_list = []
        function_table_frontHTML = [
            '\t\t\t<div class="function">\n',
            '\t<!--Function Search Setting-->\n',  # comment
            '\t<div class="function__search">\n',
            '\t<span class="function_search__title"><Strong>Search</Strong></span>\n',
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

        def make_colInfo(function_info: dict, func_index_info: dict) -> list:
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

        for func_name, func_info in self.func_data.items():
            new_row = make_colInfo(func_info, HTML_Generator.function_table_index)
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
        self.function_div_list = function_table_frontHTML + convert_funcTable_toHTML(table_list,
                                                                                     HTML_Generator.function_table_index) + function_table_rearHTML


    def return_function_div(self):
        self.make_function_div()
        return self.function_div_list

