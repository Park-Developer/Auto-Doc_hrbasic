class HTML_Generator:
    var_table_index = {
        # | Variable | Description | Default | Use | Job | type |
        "variable__name": 0,
        "variable__desc": 1,
        "variable__default": 2,
        "variable__use": 3,
        "variable__jobNum": 4,
        "variable__type": 5,
    }

    function_table_index = {
        # | Function | Description | Param | Result | Reference |
        "function__name": 0,
        "function__desc": 1,
        "function__param": 2,
        "function__result": 3,
        "function__ref": 4,
    }

    var_insertInfo = {
        "Search": "Job_selection",
        "Table": "variable__table",
    }

    Insert_classname={ # 각각의 HTML 파일을 넣을 Classname 설정
        "description":"description_UI",
        "index":"index_UI",
        "variable":"variable_UI",
        "function":"function_UI",
        "label":"label_UI",
    }
    def __init__(self):
        self.html_base = [  # Basic Form
            '<!DOCTYPE html>\n',
            '<html>\n',
            '<head>\n',
            # favicon
            '\t<link rel="apple-touch-icon" sizes="57x57" href="./favicon/apple-icon-57x57.png">\n',
            '\t<link rel="apple-touch-icon" sizes="60x60" href="./favicon/apple-icon-60x60.png">\n',
            '\t<link rel="apple-touch-icon" sizes="72x72" href="./favicon/apple-icon-72x72.png">\n',
            '\t<link rel="apple-touch-icon" sizes="76x76" href="./favicon/apple-icon-76x76.png">\n',
            '\t<link rel="apple-touch-icon" sizes="114x114" href="./favicon/apple-icon-114x114.png">\n',
            '\t<link rel="apple-touch-icon" sizes="120x120" href="./favicon/apple-icon-120x120.png">\n',
            '\t<link rel="apple-touch-icon" sizes="144x144" href="./favicon/apple-icon-144x144.png">\n',
            '\t<link rel="apple-touch-icon" sizes="152x152" href="./favicon/apple-icon-152x152.png">\n',
            '\t<link rel="apple-touch-icon" sizes="180x180" href="./favicon/apple-icon-180x180.png">\n',
            '\t<link rel="icon" type="image/png" sizes="192x192"  href="./favicon/android-icon-192x192.png">\n',
            '\t<link rel="icon" type="image/png" sizes="32x32" href="./favicon/favicon-32x32.png">\n',
            '\t<link rel="icon" type="image/png" sizes="96x96" href="./favicon/favicon-96x96.png">\n',
            '\t<link rel="icon" type="image/png" sizes="16x16" href="./favicon/favicon-16x16.png">\n',
            '\t<link rel="manifest" href="./favicon/manifest.json">\n',
            '\t<meta name="msapplication-TileColor" content="#ffffff">\n',
            '\t<meta name="msapplication-TileImage" content="/ms-icon-144x144.png">\n',
            '\t<meta name="theme-color" content="#ffffff">\n',

            '\t<title>JOB Specification</title>\n',
            '\t<style>\n',  # CSS Setting
            '\t:root{',  # CSS Variable Setting
            '\t\t--table_header_color:gray;',
            '\t}',

            '\tbody{\n',
            '\tbackground-color: lightblue;\n',
            '\t}\n',
            # Menu Bac Setting_______________________________
            '\t.menu-bar{\n',
            '\tmargin-top:30px;\n',
            '\tmargin-bottom:10px;\n',
            '\t}\n',
            # Variable Setting_______________________________
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

            '\t</style>\n',  # CSS Setting
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
            # '\t\t<button class="label_btn">Label</button>\n',
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
            # '\t\tlet label_UI = document.querySelector(".label_UI");\n',
            '\t\tlet variable_UI = document.querySelector(".variable_UI");\n',
            '\t\tlet function_UI = document.querySelector(".function_UI");\n\n',

            # 2. Button DOM
            '\t\tlet home_btn=document.querySelector(".home_btn");\n',
            # '\t\tlet label_btn=document.querySelector(".label_btn");\n',
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
            # '\t\t\tlabel_UI.style.display="none";\n\n',

            # | Event Setting|
            # Button Event Setting
            '\t\thome_btn.addEventListener("click",main_Btn_func )\n',
            # '\t\tlabel_btn.addEventListener("click", main_Btn_func)\n',
            '\t\tvariable_btn.addEventListener("click", main_Btn_func)\n',
            '\t\tfunction_btn.addEventListener("click", main_Btn_func)\n\n',

            # Button Event Function
            '\t\tfunction main_Btn_func(event){   <!--main button function-->\n',
            '\t\t\tlet button_type=event.target.innerHTML\n',
            '\t\t\tswitch(button_type){\n',
            # [Home Button Click]_______
            '\t\t\t\tcase "Home":\n',
            '\t\t\t\t\thome_btn_activation=true;\n',  # activatge
            # '\t\t\t\t\tlabel_btn_activation=false;\n',
            '\t\t\t\t\tvariable_btn_activation=false;\n',
            '\t\t\t\t\tfunction_btn_activation=false;\n\n',

            '\t\t\t\t\thome_UI.style.display="block";\n',  # block
            # '\t\t\t\t\tlabel_UI.style.display="none";\n',
            '\t\t\t\t\tvariable_UI.style.display="none";\n',
            '\t\t\t\t\tfunction_UI.style.display="none";\n',
            '\t\t\t\t\tbreak;\n\n',
            # [Label Button Click]_______
            '\t\t\t\tcase "Label":\n',
            '\t\t\thome_btn_activation=false;\n',
            # '\t\t\tlabel_btn_activation=true;\n', # activate
            '\t\t\tvariable_btn_activation=false;\n',
            '\t\t\tfunction_btn_activation=false;\n\n',

            '\t\t\thome_UI.style.display="none";\n',
            # '\t\t\tlabel_UI.style.display="block";\n',  # block
            '\t\t\tvariable_UI.style.display="none";\n',
            '\t\t\tfunction_UI.style.display="none";\n',
            '\t\t\t\t\tbreak;\n\n',
            # [Variable Button Click]______
            '\t\t\tcase "Variable":\n',
            '\t\t\t\thome_btn_activation=false;\n',
            # '\t\t\t\tlabel_btn_activation=false;\n',
            '\t\t\t\tvariable_btn_activation=true;\n',  # activate
            '\t\t\t\tfunction_btn_activation=false;\n\n',

            '\t\t\t\thome_UI.style.display="none";\n',
            # '\t\t\t\tlabel_UI.style.display="none";\n',
            '\t\t\t\tvariable_UI.style.display="block";\n',  # block
            '\t\t\t\tfunction_UI.style.display="none";\n',
            '\t\t\t\t\tbreak;\n\n',
            # [Function Button Click]______
            '\t\t\tcase "Function":\n',
            '\t\t\t\thome_btn_activation=false;\n',
            # '\t\t\t\tlabel_btn_activation=false;\n',
            '\t\t\t\tvariable_btn_activation=false;\n',
            '\t\t\t\tfunction_btn_activation=true;\n\n',  # activate

            '\t\t\t\thome_UI.style.display="none";\n',
            # '\t\t\t\tlabel_UI.style.display="none";\n',
            '\t\t\t\tvariable_UI.style.display="none";\n',
            '\t\t\t\tfunction_UI.style.display="block";\n',  # block
            '\t\t\t\t\tbreak;\n\n',
            '\t\t\t}\n',
            '\t\t}\n\n',
            ########################################[Description Setting]###############################
            '\t\t<!--Description CONST Setting-->\n',
            # HEADER CONSTANT
            '\t\tconst HEADER_STYLE={\n',
            '\t\t\th1_size:"50px",\n',
            '\t\t\th2_size:"40px",\n',
            '\t\t\th3_size:"30px",\n',
            '\t\t\th4_size:"20px",\n',
            '\t\t\th5_size:"10px",\n',
            '\t\t}\n\n',
            # BOLD CONSTANT
            '\t\tconst BOLD_STYLE={\n',
            '\t\t\tfontWeight:"bold"\n',
            '\t\t}\n\n',
            # UNDERLINE CONSTANT
            '\t\tconst UNDERLINE_STYLE={\n',
            '\t\t\ttextDecoration:"underline"\n',
            '\t\t}\n\n',
            # HIGHLIGHT CONSTANT
            '\t\tconst HIGHLIGHT_STYLE={\n',
            '\t\t\tbackgroundColor:"#FFFF00"\n',  # #FFFF00 : Yellow
            '\t\t}\n\n',
            # TEXTCOLOR CONSTANT
            '\t\tconst COLOR_STYLE={\n',
            '\t\t\tyellow:"#FFFF00",\n',
            '\t\t\tred:"#FF0000",\n',
            '\t\t\tblue:"#0000FF",\n',
            '\t\t\tgreen:"#008000",\n',
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
            # function apply_headerMD(parentNode, md_result, header_style)
            '\t\tfunction apply_headerMD(parentNode, md_result, header_style){\n',
            '\t\t\tfunction decide_font(header, header_style){\n',
            '\t\t\tlet header_size = "h" + header.length + "_size";\n',
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
            '\t\tparentNode.appendChild(document.createElement("br"));\n',
            '\t\t}\n\n',

            # function apply_boldMD(parentNode, md_result, header_style)
            '\t\tfunction apply_boldMD(parentNode,md_result,bold_style){\n',

            '\t\tlet applied = document.createElement("span");\n',
            '\t\tapplied.innerText = md_result["applied"];\n',
            '\t\tapplied.style.fontWeight=BOLD_STYLE.fontWeight;//[fontWeight];\n',

            '\t\tlet front_non_applined_part = document.createElement("span");\n',
            '\t\tfront_non_applined_part.innerText = md_result["front_non_applined_part"];\n',

            '\t\tlet rear_non_applined_part = document.createElement("span");\n',
            '\t\trear_non_applined_part.innerText = md_result["rear_non_applined_part"];\n',

            '\t\tparentNode.innerText="";\n',
            '\t\tparentNode.appendChild(front_non_applined_part);\n',
            '\t\tparentNode.appendChild(applied);\n',
            '\t\tparentNode.appendChild(rear_non_applined_part);\n',
            '\t\tparentNode.appendChild(document.createElement("br"));\n',
            '\t\t}\n\n',

            # function check_Bold_MD(line)
            '\t\tfunction check_Bold_MD(line){\n',
            '\t\tlet sentence=line.split("__");\n',
            '\t\tlet front_non_applined_part=sentence[0].trim();\n',
            '\t\tlet rear_non_applined_part=sentence[2].trim();\n',
            '\t\tlet applied_part=sentence[1].trim();\n',

            '\t\tlet result={\n',
            '\t\t"front_non_applined_part":front_non_applined_part,\n',
            '\t\t"rear_non_applined_part":rear_non_applined_part,\n',
            '\t\t"applied":applied_part,\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t}\n\n',
            ##############@#@#
            # function check_Underline_MD(line)
            '\t\tfunction check_Underline_MD(line){\n',
            '\t\tlet sentence=line.split("@u{");\n',
            '\t\tlet front_non_applined_part=sentence[0].trim();\n',
            '\t\tlet temp_line_part=sentence[1].split("}");\n',
            '\t\tlet rear_non_applined_part= temp_line_part[1].trim();\n',
            '\t\tlet applied_part= temp_line_part[0].trim();\n\n',

            '\t\tlet result={\n',
            '\t\t"front_non_applined_part":front_non_applined_part,\n',
            '\t\t"rear_non_applined_part":rear_non_applined_part,\n',
            '\t\t"applied":applied_part,\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t}\n\n',
            ##############@#@#
            # function apply_underlineMD(parentNode, md_result, header_style)
            '\t\tfunction apply_underlineMD(parentNode,md_result,bold_style){\n',

            '\t\tlet applied = document.createElement("span");\n',
            '\t\tapplied.innerText = md_result["applied"];\n',
            '\t\tapplied.style.textDecoration=UNDERLINE_STYLE.textDecoration;\n',

            '\t\tlet front_non_applined_part = document.createElement("span");\n',
            '\t\tfront_non_applined_part.innerText = md_result["front_non_applined_part"];\n',

            '\t\tlet rear_non_applined_part = document.createElement("span");\n',
            '\t\trear_non_applined_part.innerText = md_result["rear_non_applined_part"];\n',

            '\t\tparentNode.innerText="";\n',
            '\t\tparentNode.appendChild(front_non_applined_part);\n',
            '\t\tparentNode.appendChild(applied);\n',
            '\t\tparentNode.appendChild(rear_non_applined_part);\n',
            '\t\tparentNode.appendChild(document.createElement("br"));\n',
            '\t\t}\n\n',
            #######################################################################
            # function check_Highlight_MD(line)
            '\t\tfunction check_Highlight_MD(line){\n',
            '\t\tlet sentence=line.split("@mark{");\n',
            '\t\tlet front_non_applined_part=sentence[0].trim();\n',
            '\t\tlet temp_line_part=sentence[1].split("}");\n',
            '\t\tlet rear_non_applined_part= temp_line_part[1].trim();\n',
            '\t\tlet applied_part= temp_line_part[0].trim();\n',

            '\t\tlet result={\n',
            '\t\t"front_non_applined_part":front_non_applined_part,\n',
            '\t\t"rear_non_applined_part":rear_non_applined_part,\n',
            '\t\t"applied":applied_part,\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t}\n\n',
            #########################################################################
            # function apply_highlightMD(parentNode, md_result, header_style)
            '\t\tfunction apply_highlightMD(parentNode,md_result,bold_style){\n',

            '\t\tlet applied = document.createElement("span");\n',
            '\t\tapplied.innerText = md_result["applied"];\n',
            '\t\tapplied.style.backgroundColor=HIGHLIGHT_STYLE.backgroundColor;\n',

            '\t\tlet front_non_applined_part = document.createElement("span");\n',
            '\t\tfront_non_applined_part.innerText = md_result["front_non_applined_part"];\n',

            '\t\tlet rear_non_applined_part = document.createElement("span");\n',
            '\t\trear_non_applined_part.innerText = md_result["rear_non_applined_part"];\n',

            '\t\tparentNode.innerText="";\n',
            '\t\tparentNode.appendChild(front_non_applined_part);\n',
            '\t\tparentNode.appendChild(applied);\n',
            '\t\tparentNode.appendChild(rear_non_applined_part);\n',
            '\t\tparentNode.appendChild(document.createElement("br"));\n',
            '\t\t}\n\n',
            #########################################################################
            # function check_Color_MD(line)
            '\t\tfunction check_Color_MD(line){\n',
            '\t\tlet color_tag;\n',
            '\t\tif (line.indexOf("red")!==-1){\n',
            '\t\tcolor_tag="@red{";\n',
            '\t\t}else if (line.indexOf("blue")!==-1){\n',
            '\t\tcolor_tag="@blue{";\n',
            '\t\t}else if (line.indexOf("green")!==-1){\n',
            '\t\tcolor_tag="@green{";\n',
            '\t\t}else if (line.indexOf("yelllow")!==-1){\n',
            '\t\tcolor_tag="@yellow{";\n',
            '\t\t}\n\n',

            '\t\tlet sentence=line.split(color_tag);\n',
            '\t\tlet front_non_applined_part=sentence[0].trim();\n',
            '\t\tlet temp_line_part=sentence[1].split("}");\n',
            '\t\tlet rear_non_applined_part= temp_line_part[1].trim();\n',
            '\t\tlet applied_part= temp_line_part[0].trim();\n\n',

            '\t\tlet result={\n',
            '\t\t"front_non_applined_part":front_non_applined_part,\n',
            '\t\t"rear_non_applined_part":rear_non_applined_part,\n',
            '\t\t"applied":applied_part,\n',
            '\t\t"color_tag":color_tag.substring(1,color_tag.length-1),\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t}\n\n',
            #########################################################################
            # function apply_colorMD(parentNode, md_result, header_style)
            '\t\tfunction apply_colorMD(parentNode,md_result,bold_style){\n',

            '\t\tlet applied = document.createElement("span");\n',
            '\t\tapplied.innerText = md_result["applied"];\n',
            '\t\tlet color_style=md_result["color_tag"];\n',
            '\t\tapplied.style.color=COLOR_STYLE[color_style];\n',

            '\t\tlet front_non_applined_part = document.createElement("span");\n',
            '\t\tfront_non_applined_part.innerText = md_result["front_non_applined_part"];\n',

            '\t\tlet rear_non_applined_part = document.createElement("span");\n',
            '\t\trear_non_applined_part.innerText = md_result["rear_non_applined_part"];\n',

            '\t\tparentNode.innerText="";\n',
            '\t\tparentNode.appendChild(front_non_applined_part);\n',
            '\t\tparentNode.appendChild(applied);\n',
            '\t\tparentNode.appendChild(rear_non_applined_part);\n',
            '\t\tparentNode.appendChild(document.createElement("br"));\n',
            '\t\t}\n\n',
            #########################################################################
            '\t\t<!--Description DOM Setting-->\n',
            '\t\tlet description_readme= document.querySelector(".description_readme");\n\n',

            '\t\tlet readmeLine_num=description_readme.childElementCount;\n',
            '\t\tfor(let i=0; i<readmeLine_num;i++){\n',
            '\t\t\tif(i>=1){ // <!--header 제외-->\n',
            '\t\t\tlet readline=document.querySelector(".readme_"+(i-1).toString());\n',
            '\t\t\tlet readline__text=readline.innerText;\n',
            # [1]_ Header MD Check & Application
            '\t\t\tif(readline__text.indexOf("#")!==-1){\n',
            '\t\t\tlet is_HeadMD=check_Head_MD(readline__text);\n',
            '\t\t\tapply_headerMD(readline,is_HeadMD,HEADER_STYLE);\n',
            '\t\t\t}\n',

            # [2]_ Bold MD Check & Application
            '\t\t\tif(readline__text.indexOf("__")!==-1){\n',
            '\t\t\tlet first_loc=readline__text.indexOf("__");\n',
            '\t\t\tif(readline__text.indexOf("__",first_loc+3)!==-1){\n',
            '\t\t\tlet is_boldMD=check_Bold_MD(readline__text);\n',
            '\t\t\tapply_boldMD(readline,is_boldMD,BOLD_STYLE);\n',
            '\t\t\t}\n',
            '\t\t\t}\n',

            # [3]_ Underline MD Check & Application
            '\t\t\tif(readline__text.indexOf("@u")!==-1){\n',
            '\t\t\tlet is_underlineMD=check_Underline_MD(readline__text);\n',
            '\t\t\tapply_underlineMD(readline,is_underlineMD,UNDERLINE_STYLE);\n',
            '\t\t\t}\n',

            # [4]_ Highlight MD Check & Application
            '\t\t\tif(readline__text.indexOf("@mark")!==-1){\n',
            '\t\t\tlet is_highlightMD=check_Highlight_MD(readline__text);\n',
            '\t\t\tapply_highlightMD(readline,is_highlightMD,HIGHLIGHT_STYLE);\n',
            '\t\t\t}\n',

            # [5]_ Color MD Check & Application
            '\t\tlet colorList=Object.keys(COLOR_STYLE);\n',
            '\t\tfor(let i=0;i<colorList.length;i++){\n',
            '\t\t\tlet colorTag="@"+colorList[i];\n',
            '\t\t\tif(readline__text.indexOf(colorTag)!==-1){\n',
            '\t\t\t\tlet is_colorMD=check_Color_MD(readline__text);\n',
            '\t\t\t\tapply_colorMD(readline,is_colorMD,COLOR_STYLE);\n',
            '\t\t\t\tbreak;\n',
            '\t\t\t}\n',
            '\t\t}\n\n',
            '\t\t}\n',  ## Main Loop END
            '\t\t}\n\n',

            ########################################[Variable Setting]##################################

            # |Variable Constant Setting|
            '\t\t<!--Variable CONST Setting-->\n',
            '\t\tconst VARIABLE_TYPE_INDEX = 6;\n',
            '\t\tconst VARIABLE_JOB_INDEX = 5;\n',
            '\t\tconst VARIABLE_NAME_INDEX = 1;\n\n',

            # |Variable DOM setting|
            '\t\t<!--Variable DOM Setting-->\n',
            '\t\tlet variable_table= document.querySelector(".variable__table");\n\n',
            '\t\tlet variable_typeSelector= document.querySelector(".Type_selection");\n\n',  # selector
            '\t\tlet variable_jobSelector= document.querySelector(".Job_selection");\n',  # Selector
            '\t\tlet variable_Search= document.querySelector(".variable__search");\n',  # Search
            '\t\tlet variable_Search_Input=document.querySelector(".variable_search__input");\n',  # Search input
            '\t\tlet variable_Search_Btn=document.querySelector(".variable_search__btn");\n',  # Search ok button

            # |Variable Event Setting|
            # (1). Variable Type Selector Event_____________________
            '\t\tvariable_typeSelector.addEventListener("change", () => {\n',  # Event Setting
            '\t\tchange_typeSelection();\n',
            '\t\t});\n\n',

            # Type Selection Event Function
            '\t\tfunction change_typeSelection(){\n',  # Event function Definition
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
        self.description_div_list = []
        self.variable_div_list = []
        self.variable_SearchPart_div_list = []
        self.variable_TablePart_div_list = []
        self.function_div_list = []
        self.label_div_list = []
        self.index_div_list = []

        self.div_insert_location = {
            # Insert class name : HTML List
            HTML_Generator.Insert_classname["description"]: self.description_div_list,
            HTML_Generator.Insert_classname["variable"]:self.variable_div_list,
            HTML_Generator.Insert_classname["function"]:self.function_div_list,
            #"label_UI": self.label_div_list,
            # "index_UI": self.index_div_list,
        }


    def update_all_htmlList(self):
        desc_insertClass_name= HTML_Generator.Insert_classname["description"]
        var_insertClass_name =HTML_Generator.Insert_classname["variable"]
        func_insertClass_name = HTML_Generator.Insert_classname["function"]

        self.div_insert_location[desc_insertClass_name] = self.description_div_list
        self.div_insert_location[var_insertClass_name] = self.variable_div_list
        self.div_insert_location[func_insertClass_name] = self.function_div_list
        #self.div_insert_location["label_UI"] = self.label_div_list
        #self.div_insert_location["index_UI"] = self.index_div_list

    def returnHTML_basicForm(self):
        '''
        최종적으로 만들어진 html 파일을 반환
        :return: HTML file
        '''
        result = ''.join(self.html_base)

        return result

    def returnHTML_file(self, html_list: list):
        '''
        html list를 HTML파일로 만들어 반환
        :param html_list:
        :return:
        '''
        result = ''.join(html_list)

        return result

    def find_classLoc(self, class_name: str, htmlline: list):
        '''
        class name을 이용하여 htmlline에서 해당 라인이 있는 위치 반환
        :param class_name:
        :param htmlline:
        :return: (is_find, class_loc)  /   is_find : 존재 유무, class_loc : htmlline에서의 index
        '''
        is_find = False
        class_loc = -1

        target_sentence = 'class="' + class_name

        for idx, line in enumerate(htmlline):
            if target_sentence in line:
                is_find = True
                class_loc = idx
                break

        return (is_find, class_loc)

    def add_html(self, basic_html: list, operand_html: list, addtion_loc: int):
        '''
        basic_html의 addition_loc 위치에 operatnd html 삽입 후, 합쳐진 html list 반환
        삽입 컨셉 : 클래스 정의 라인 밑에 삽입

        :param basic_html:
        :param operand_html:
        :param addtion_loc:
        :return:
        '''
        addtion_start_loc = addtion_loc + 1  # 클래스 태그 다음에 삽입
        merged_htm1 = basic_html[:addtion_start_loc] + operand_html + basic_html[addtion_start_loc:]

        return merged_htm1

    def merge_Allhtml(self):
        try:
            self.update_all_htmlList() # update html list to insert

            if (self.html_base == []):
                raise Exception("No HTML Base")

            def find_classLoc(base_html: list, class_name: str) -> dict:
                result = {
                    "is_find": False,
                    "location": -1,
                }
                for idx, line in enumerate(base_html):
                    if class_name in line:  # 삽입 위치
                        result = {
                            "is_find": True,
                            "location": idx,
                        }
                        break
                return result

            def insert_to_basehtml(base_html: list, insert_html: list, insert_loc: int) -> list:
                result = base_html[:insert_loc] + insert_html + base_html[insert_loc:]
                return result

            for insert_className, insert_html in self.div_insert_location.items():
                if (insert_html != []):
                    find_result = find_classLoc(self.html_base, insert_className)
                    if find_result["is_find"] == True:
                        insert_loc = find_result["location"] + 1
                        self.html_base = insert_to_basehtml(self.html_base, insert_html, insert_loc)

        except Exception as e:
            print("An exception occurred: ", e)

if __name__ == "__main__":
    import Desc_Generator as desc_ge
    import Func_Generator as func_ge
    import Var_Generator as var_ge
    import JobReader as job_re
    import raw_func
    job_address=r"C:\Users\gnvid\.Nimi Places\Project\HRBASIC AutoDoc\Test code" # for Test

    # [1]_ raw data 읽기
    job_reader = job_re.JobReader(job_address)
    job_reader.read_n_make_rawData()
    descrition_raw_data = job_reader.Job_description
    variable_raw_data = job_reader.Variable_raw_List
    function_raw_data = job_reader.Function_raw_List

    # [2]_ 데이터 가공
    descrition_processed_data = raw_func.extract_descripInfo(descrition_raw_data)
    variable_processed_data = raw_func.extract_varInfo(variable_raw_data)
    function_processed_data = raw_func.extract_functionInfo(function_raw_data)

    # [3]_ HTML 파일 생성
    html_generator = HTML_Generator()

    html__desc_generator=desc_ge.Description_Generator(descrition_processed_data) # description 객체 생성
    html__func_generator=func_ge.Function_Generator(function_processed_data) # function 객체 생성
    html__var_generator=var_ge.Variable_Generator(variable_processed_data) # variable 객체 생성

    html_generator.description_div_list = html__desc_generator.return_description_div()
    html_generator.variable_div_list = html__var_generator.return_variable_div()
    html_generator.function_div_list =html__func_generator.return_function_div()

    html_generator.merge_Allhtml()
    result_html = html_generator.returnHTML_file(html_generator.html_base)
    html_file = open('Job Specification.html', 'w')
    html_file.write(result_html)
    html_file.close()