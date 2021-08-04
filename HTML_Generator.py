class HTML_Generator:
    def __init__(self):
         self.htmlline=[ # Basic Form
            '<!DOCTYPE html>\n',
            '<html>\n',
            '<head>\n',
            '\t<title>Page Title</title>\n',
            '\t<style>\n', # CSS Setting
            '\tbody{\n',
            '\tbackground-color: lightblue;\n',
            '\t}\n',
            '\t</style>\n', # CSS Setting
            '</head>\n',

            '<body>\n',
                '\t<div class="Status-bar">\n',
                    '\t\t<h1 class="main_title">This is a Heading</h1>\n',
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
             '\t\t<div class="home_UI">\n',
             '\t\t<span> Home UI </span>\n',
             '\t\t</div> <!--home_UI end-->\n\n',

             '\t\t<div class="index_UI">\n',
             '\t\t<span> index ui </span>\n',
             '\t\t</div> <!--index_UI end-->\n\n',

             '\t\t<div class="variable_UI">\n',
             '\t\t<span> variable ui </span>\n',
             '\t\t</div> <!--variable_UI end-->\n\n',

             '\t\t<div class="function_UI">\n',
             '\t\t</div> <!--function_UI end-->\n\n',

             '\t</div> <!--main-frame end-->\n\n',
             '\t<script>\n',
                # Variable Definition : All variable is global variable
                '\t\t<!--Btn Variable Setting-->\n',
                '\t\tlet home_btn_activation=false;\n',
                '\t\tlet index_btn_activation=false;\n',
                '\t\tlet variable_btn_activation=false;\n',
                '\t\tlet function_btn_activation=false;\n\n',

                 # Event Setting
                '\t\t<!--Btn Event Function Setting-->\n',
                '\t\tfunction home_btn_func() {   <!--Home Btn Function-->\n', # Home Button Function
                '\t\t\talert("This is a working button1");\n',
                '\t\t\thome_btn_activation=true;\n',
                '\t\t\tindex_btn_activation=false;\n',
                '\t\t\tvariable_btn_activation=false;\n',
                '\t\t\tfunction_btn_activation=false;\n',
                '\t\t}\n\n',

                '\t\tfunction index_btn_func() {   <!--Index Btn Function-->\n', # Index Button Function
                '\t\t\talert("This is a working button2");\n',
                '\t\t\thome_btn_activation=false;\n',
                '\t\t\tindex_btn_activation=true;\n',
                '\t\t\tvariable_btn_activation=false;\n',
                '\t\t\tfunction_btn_activation=false;\n',
                '\t\t}\n\n',

                '\t\tfunction variable_btn_func() {   <!--Variable Btn Function-->\n', # Variable Button Function
                '\t\t\thome_btn_activation=false;\n',
                '\t\t\tindex_btn_activation=false;\n',
                '\t\t\tvariable_btn_activation=true;\n',
                '\t\t\tfunction_btn_activation=false;\n',
                '\t\t\talert("This is a working button3");\n'
                '\t\t}\n\n',

                '\t\tfunction function_btn_func() {   <!--Function Btn Function-->\n', # Function Button Function
                '\t\t\thome_btn_activation=false;\n',
                '\t\t\tindex_btn_activation=false;\n',
                '\t\t\tvariable_btn_activation=false;\n',
                '\t\t\tfunction_btn_activation=true;\n',
                '\t\t\talert("This is a working button4");\n',
                '\t\t}\n\n',

             '\t</script>\n',
            '</body>\n',
            '</html>\n',
         ]
         self.description_div_list=[]

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

            '\t<div class="description">\n',
            ###########################################################################################
            '\t\t<div class="description__description">\n',
                '\t\t\t<span class="description__title">\n',
                '\t\t\t<i class="fas fa-square"></i> Description : \n',
                '\t\t\t</span>\n',

                '\t\t\t<span class="description__value">\n',
                '\t\t\t'+description+'\n',
                '\t\t\t</span>\n',
            '\t\t</div>\n',
            ###########################################################################################
            '\t\t<div class="description__version">\n',
                '\t\t\t<span class="version__title">\n',
                '\t\t\t<i class="fas fa-square"></i> Version : \n',
                '\t\t\t</span>\n',

                '\t\t\t<span class="version__value">\n',
                '\t\t\t' + version + '\n',
                '\t\t\t</span>\n',
            '\t\t</div>\n',
            ###########################################################################################
            '\t\t<div class="description__developer">\n',
                '\t\t\t<span class="developer__title">\n',
                '\t\t\t<i class="fas fa-square"></i> Developer : \n',
                '\t\t\t</span>\n',

                '\t\t\t<span class="developer__value">\n',
                '\t\t\t' + developer + '\n',
                '\t\t\t</span>\n',
            '\t\t</div>\n',
            ###########################################################################################
            '\t</div>\n',
            '<script src = "https://kit.fontawesome.com/3dbd9a16b0.js" crossorigin = "anonymous" > </script >'
        ]

        self.description_div_list=html_result

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