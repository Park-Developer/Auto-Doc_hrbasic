class HTML_Generator:
    def __init__(self):
         self.htmlline=[ # Basic Form
            '<!DOCTYPE html>\n',
            '<html>\n',
            '<head>\n',
            '\t<title>Page Title</title>\n',
            '</head>\n',

            '<body>\n',
                '\t<div class="Status-bar">\n',
                    '\t\t<h1 class="main_title">This is a Heading</h1>\n',
                    '\t\t<p class="sub_title">This is a paragraph.</p>\n',
                '\t</div>\n',

             '\t<div class="menu-bar">\n',
                '\t\t<button onclick = "home_btn_func()">Home</button>\n'
                '\t\t<button onclick = "index_btn_func()">Index</button>\n'
                '\t\t<button onclick = "variable_btn_func()">Variable</button>\n'
                '\t\t<button onclick = "function_btn_func()">Function</button>\n'
             '\t</div>\n',

             '\t<div class="main_frame">\n',
             
             '\t</div>\n',
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

