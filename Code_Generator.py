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
            '\t\t\t<div class="code_search_part" style="display:flex">\n',

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
        divlist_temp=[]
        for code_num,code_data in self.code_data.items():

            job_number = code_data['job_num']
            if type(job_number) == int:
                job_number= str(job_number)
            divlist_temp.append('\t\t\t<option>' + job_number+ '</option>\n')

        self.code_SearchPart_div_list=list(set(divlist_temp))
        return self.code_SearchPart_div_list

    def overlapped_syntax__TO(self,applined_line):
        '''
        END | IF | ENDIF가 중복되는 경우 방지용
        :param applined_line:
        :return:
        '''
        if "TO" in applined_line: # END인 경우
            loc=applined_line.find("TO")

            if applined_line[loc-1:loc+3] == "STOP": # END가 ENDIF에 포함되어 있는 경우
                return applined_line
            else:
                syntax="TO"
                color=HTML_Generator.code_UI_setting["HRBasic_Syntax"]["TO"]
                applined_line = applined_line.replace(syntax.strip(), '<span style="color:{0}">'.format(
                    color.strip()) + syntax.strip() + "</span>")
                return applined_line
        else:
            return applined_line

    def overlapped_syntax__END(self,applined_line):
        '''
        END | IF | ENDIF가 중복되는 경우 방지용
        :param applined_line:
        :return:
        '''
        if "END" in applined_line: # END인 경우
            loc=applined_line.find("END")

            if applined_line[loc:loc+5] == "ENDIF": # END가 ENDIF에 포함되어 있는 경우
                return applined_line
            else:
                syntax="END"
                color=HTML_Generator.code_UI_setting["HRBasic_Syntax"]["END"]
                applined_line = applined_line.replace(syntax.strip(), '<span style="color:{0}">'.format(
                    color.strip()) + syntax.strip() + "</span>")
                return applined_line

        elif "IF" in applined_line: # IF인 경우
            loc=applined_line.find("IF")

            if applined_line[loc-3:loc+2] == "ENDIF": # END가 ENDIF에 포함되어 있는 경우
                return applined_line
            else:
                syntax="IF"
                color=HTML_Generator.code_UI_setting["HRBasic_Syntax"]["IF"]
                applined_line = applined_line.replace(syntax.strip(), '<span style="color:{0}">'.format(
                    color.strip()) + syntax.strip() + "</span>")
                return applined_line

        else:
            return applined_line

    def HRBasic_Syntax_highlight(self,line:str,sytax_color_list:dict)->str:
        '''
        code에 HRBasic 문법 적용
        :param line:
        :return:
        '''
        applined_line=line
        for syntax,color in sytax_color_list.items():
            if syntax.strip() in line:
                if syntax=="END" or syntax=="IF":   # 중복 방지 작업1 : END - ENDIF - IF
                    applined_line=self.overlapped_syntax__END(applined_line)
                elif syntax=="TO":
                    applined_line = self.overlapped_syntax__TO(applined_line)
                else: # 중복이 없는 경우
                    applined_line=applined_line.replace(syntax.strip(),'<span style="color:{0}">'.format(color.strip())+syntax.strip()+"</span>")

        return applined_line

    def MixedCmt_convert_toSpan(self,raw_list):
        span_list=[]
        def maxLine_filter(line):
            filter_list=["\n"]
            for filter in filter_list:
                if (filter in line):
                    line=line.replace(filter,"")

            conversion_list=[" "]
            for conversion in conversion_list:
                if conversion in line:
                    line = line.replace(" ","&nbsp") # &nbsp : HTML 공백태그
            return line
        # Comment UI Setting
        comment_font_color=HTML_Generator.code_UI_setting["table_UI"]["comment_font_color"]
        comment_font_style = HTML_Generator.code_UI_setting["table_UI"]["comment_font_style"]

        for idx,line in enumerate(raw_list):
            filtered_line = maxLine_filter(line)
            if "'" in filtered_line : # 주석과 코드가 같이 있는 경우
                temp=filtered_line .split("'")
                temp__code=self.HRBasic_Syntax_highlight(temp[0],HTML_Generator.code_UI_setting["HRBasic_Syntax"])
                temp__cmt= "' "+temp[1]
                span_list.append("<span>" +temp__code + "</span>"+'<span style="color:{0};font-style:{1}">'.format(comment_font_color,comment_font_style) +temp__cmt + "</span><br>")
            else:
                syntax_highlighted_line=self.HRBasic_Syntax_highlight(filtered_line,HTML_Generator.code_UI_setting["HRBasic_Syntax"])
                span_list.append("<span>"+syntax_highlighted_line+"</span><br>")

        result=''.join(span_list)

        return result

    def PureCmt_convert_toSpan(self,raw_list):
        span_list=[]
        def pureLine_filter(line):
            filter_list=["\n","@code/","/@code","'"]
            for filter in filter_list:
                if (filter in line):
                    line=line.replace(filter,"")

            return line

        for idx,line in enumerate(raw_list):
            filtered_line=pureLine_filter(line)
            if len(filtered_line.strip())!=0: # 빈 문자열이 아닌 경우
                span_list.append('<span class="comment_{0}">'.format(idx)+pureLine_filter(line)+'<br></span>')

        result=''.join(span_list)

        return result
    def make_codeTable_part(self):
        table_base=['<tr class="code__table_header">',
		'<th class="header_index" align="center">Index</th>',
		'<th class="header_code">Code</th>',
		'<th class="header_comment">Comment</th>',
		'<th class="header_job" align="center">Job</th>',
		'</tr>',]

        def match_col_property(code_info:dict,code_index_info: dict)->list:
            new_row = ['-', '-', '-']  # '-' : 속성이 없다는 뜻  //  | Code | Comment | Job |
            for property, index in code_index_info.items():
                if code_info.get(property)!=None:
                    if(property=="mixedComment_part"):
                        converted_list=self.MixedCmt_convert_toSpan(code_info[property])
                        new_row[code_index_info[property]] = converted_list
                    elif (property=="pureComment_part"):
                        converted_list = self.PureCmt_convert_toSpan(code_info[property])
                        new_row[code_index_info[property]] =converted_list
                    else:
                        new_row[code_index_info[property]]=code_info[property]
            return new_row

        code_index=0

        # Table UI Setting
        table_theme_color=HTML_Generator.code_UI_setting["table_UI"]["theme_color"]
        table_basic_font_color=HTML_Generator.code_UI_setting["table_UI"]["basic_font_color"]

        for code_number, code_info in self.code_data.items():
            row_html = ['\t\t\t\t\t<tr bgcolor={0} style="color:{1}"'.format(table_theme_color,table_basic_font_color) + ' class="code__table_row{0}">\n'.format(code_index) ,
                        '\t\t\t\t\t<td style="font-weight:bold" class="code__table_row' + str(code_index) + '_col0" align="center">' + str(
                            code_index + 1) + '</td>\n']  # Index Column

            row_info=match_col_property(code_info,HTML_Generator.code_table_index)

            for col_idx, property_value in enumerate(row_info):
                row_html.append('\t\t\t\t\t<td valign="top" class="code__table_row' + str(code_index) + '_col'
                                + str(col_idx+1) + '">' + str(property_value) + '</td>\n'
                                )

            code_index+=1
            row_html.append('\t\t\t\t\t</tr>\n\n')
            table_base=table_base+row_html
        self.code_TablePart_div_list =table_base

        return self.code_TablePart_div_list


    def return_code_div(self):
        self.make_code_div()
        return self.code_div_list