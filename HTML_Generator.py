class HTML_Generator:
    var_table_index = {
        # | Variable | Description | Default | Use | Job | type |
        "variable__name": 0,
        "variable__desc": 1,
        "variable__default": 2,
        "variable__use": 3,
        "variable__loc": 4,
        "variable__type": 5,
    }
    var_insertInfo = {
        "Search": "Job_selection",
        "Table": "variable__table",
    }

    function_table_index = {
        # | Function | Description | Param | Result | Reference |
        "function__name": 0,
        "function__desc": 1,
        "function__param": 2,
        "function__result": 3,
        "function__ref": 4,
    }

    code_table_index = {
        # | Code | Comment | Job |
        "mixedComment_part": 0,
        "pureComment_part": 1,
        "job_num": 2,
    }
    code_insertInfo = {
        "Search": "code_Job_selection",
        "Table": "code__table",
    }
    code_UI_setting={
        "table_UI":{
            "theme_color": "#121212",
            "basic_font_color": "white",
            "comment_font_color": "pink",
            "comment_font_style": "italic",
        },
        "HRBasic_Syntax":{
            # [1] Motion I/O_____
           "MOVE ":"blue",
           "PRINT":"blue",
           "INPUT":"blue",
           "WAIT":"blue",
           "CONTPATH":"orange",

            # [2] Flow 제어_____
           "GOTO":"purple",
           "GOSUB":"purple",
           "CALL":"purple",
           "IF":"green",
           "THEN":"green",
           "FOR":"green",
           "DELAY":"purple",
           "END":"purple",
           "RETURN":"purple",
           "ELSEIF":"green",
           "ELSE":"green",
           "ENDIF":"green",
           "NEXT":"green",
           "JMPP":"purple",
           "STOP":"purple",
           "SELECT":"green",
           "CASE":"green",
           "Lable":"purple",
           "END_SELECT":"green",
           "EXIT":"purple",
           "TO":"green",
           "STEP":"green",

            # [3] 기타_____
           "REM ":"red",
           "GATHER":"orange",
           "StoPoCnd":"orange",
           "TaskStart":"orange",
           "DIM": "orange",
           "AS": "orange",

            # [4] Function_____
           "ABS":"pink",
           "MAX":"pink",
           "MIN":"pink",
           "DEGRAD":"pink",
           "RADDEG ":"pink",
           "SQR":"pink",
           "SIN":"pink",
           "COS":"pink",
           "TAN":"pink",
           "ATN":"pink",
           "ATN2":"pink",
           "DIST":"pink",
           "VAL":"pink",
           "LEN":"pink",
           "TIMER":"pink",
           "STR$":"pink",
           "CHR$":"pink",
           "LEFT$":"pink",
           "RIGHT$":"pink",
           "MID$":"pink",
           "DATE$":"pink",
           "TIME$":"pink",

           # [5] Property_____
           "_AX_X":"#B9862E", # Brown
           "_AX_TH":"#B9862E", # Brown
           "_AX_R":"#B9862E", # Brown
           "_AX_L":"#B9862E", # Brown
           "_AX_RA":"#B9862E", # Brown
           "_AX_LA":"#B9862E", # Brown
           "_AX_Z1":"#B9862E", # Brown
           "_AX_Z2":"#B9862E", # Brown

           "Accuracy": "#B9862E",  # Brown
           "SPDRATE": "#B9862E",  # Brown
           "ACCRATE": "#B9862E",  # Brown
           "DECRATE": "#B9862E",  # Brown
        }

    }

    Insert_classname={ # 각각의 HTML 파일을 넣을 Classname 설정
        "description":"description_UI",
        "index":"index_UI",
        "variable":"variable_UI",
        "function":"function_UI",
        "label":"label_UI",
        "code":"code_UI",
    }
    def __init__(self):
        self.manual_link="https://mica-mule-62a.notion.site/0dd6366820874e8a84bf0a1e762fa4ff" # * manual이 작성된 notion link
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
            '\t\t--table_header_color:#47c58f;\n',
            '\t}',

            '\tbody{\n',
            '\tbackground-color: white;\n',
            '\t}\n',
            '\t.Status-bar{\n',
            '\tbackground-color:#D1F2EB;\n',
            '\t}\n\n',
            # Menu Bac Setting_______________________________
            '\t.menu-bar{\n',
            '\tpadding-top:30px;\n',
            '\tmargin-bottom:10px;\n',
            '\tbackground-color:#D1F2EB;\n',
            '\t}\n',

            # Table Setting
            '\ttable, th, td {\n',
            '\t    border: 1px solid gray;\n',
            '\t}\n',
            # Description Setting________________
            '\t.description_readme{\n',
            '\twidth: 50%;\n',
            '\tborder: 1px solid;\n',
            '\tborder-color: #47c58f;\n',
            '\tbackground-color:#F8F8FF;\n',
            '\tmargin-top:11px;\n',
            '\tmargin-left:5px;\n',
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
            '\t.code__table_header{\n',
            '\t\tbackground-color:var(--table_header_color)\n',
            '\t}\n',
            # TEST to solve bug
            '\t.header_index{\n',
            '\twidth:30px;\n',
            '\t}\n',

            # Function CSS Setting_______________________________
            '\t.function__table{\n',
            '\t\tborder: 1px solid black;\n',
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
            '\t\t<button class="home_btn"><strong>Home</strong></button>\n',
            '\t\t<button class="variable_btn"><strong>Variable</strong></button>\n',
            '\t\t<button class="function_btn"><strong>Function</strong></button>\n',
            '\t\t<button class="code_btn"><strong>Code</strong></button>\n',
            '\t\t<a href='+self.manual_link+'class="btn btn-primary"><i class="fas fa-external-link-square-alt"></i>Manual</a>\n',
            '\t</div>\n\n',

            '\t<!-- Main Frame Setting -->\n',
            '\t<div class="main_frame">\n\n',

            '\t\t<div class="description_UI">\n',
            '\t\t</div> <!--description_UI end-->\n\n',

            '\t\t<div class="label_UI">\n',
            '\t\t</div> <!--label_UI end-->\n\n',

            '\t\t<div class="variable_UI" hidden>\n',
            '\t\t</div> <!--variable_UI end-->\n\n',

            '\t\t<div class="function_UI" hidden>\n',
            '\t\t</div> <!--function_UI end-->\n\n',

            '\t\t<div class="label_UI">\n',
            '\t\t</div> <!--label_UI end-->\n\n',

            '\t\t<div class="code_UI" hidden>\n',
            '\t\t</div> <!--code_UI end-->\n\n',

            '\t</div> <!--main-frame end-->\n\n',
            # icon Setting
            '\t<script src = "https://kit.fontawesome.com/3dbd9a16b0.js" crossorigin = "anonymous" > </script>\n\n',

            # JS Setting
            '\t<script>\n',

            ########################################[Initial Setting]#####################################
            '\t\tlet MD_Module = {\n',
            '\t\tMD_CODE: {\n',
            '\t\theader_code: 0,\n',
            '\t\temphasis_code: 5,\n',
            '\t\tmark_code: 6,\n',
            '\t\treserved_code: 7,\n',
            '\t\tu_code: 8,\n',
            '\t\tcolor_red_code: 11,\n',
            '\t\tcolor_blue_code: 12,\n',
            '\t\tcolor_yellow_code: 13,\n',
            '\t\tcolor_green_code: 14,\n',
            '\t\t},\n',
            '\t\t\n',
            '\t\t\n',
            '\t\tHEADER_STYLE: {\n',
            '\t\th1_size: "50px",\n',
            '\t\th2_size: "40px",\n',
            '\t\th3_size: "30px",\n',
            '\t\th4_size: "20px",\n',
            '\t\th5_size: "10px",\n',
            '\t\t},\n',
            '\t\t\n',
            '\t\tBOLD_STYLE: {\n',
            '\t\tfontWeight: "bold"\n',
            '\t\t},\n',
            '\t\t\n',
            '\t\tUNDERLINE_STYLE: {\n',
            '\t\ttextDecoration: "underline"\n',
            '\t\t},\n',
            '\t\t\n',
            '\t\tHIGHLIGHT_STYLE: {\n',
            '\t\tbackgroundColor: "#FFFF00"\n',
            '\t\t},\n',
            '\t\t\n',
            '\t\tCOLOR_STYLE: {\n',
            '\t\tyellow: "#FFFF00",\n',
            '\t\tred: "#FF0000",\n',
            '\t\tblue: "#0000FF",\n',
            '\t\tgreen: "#008000",\n',
            '\t\t},\n',
            '\t\ttool: {\n',
            '\t\tparag_match: function (md_stk) {\n',
            '\t\tmark_loc = md_stk.indexOf(MD_Module.MD_CODE.mark_code);\n',
            '\t\tcolor_red_loc = md_stk.indexOf(MD_Module.MD_CODE.color_red_code);\n',
            '\t\tcolor_blue_loc = md_stk.indexOf(MD_Module.MD_CODE.color_blue_code);\n',
            '\t\tcolor_yellow_loc = md_stk.indexOf(MD_Module.MD_CODE.color_yellow_code);\n',
            '\t\tcolor_green_loc = md_stk.indexOf(MD_Module.MD_CODE.color_green_code);\n',
            '\t\tu_loc = md_stk.indexOf(MD_Module.MD_CODE.u_code);\n',
            '\t\t\n',
            '\t\tlet max_idx = Math.max(mark_loc, color_yellow_loc, color_green_loc, color_blue_loc, color_red_loc, u_loc);\n',
            '\t\treturn max_idx;\n',
            '\t\t},\n',
            '\t\t\n',
            '\t\t},\n',
            '\t\tgetter: {\n',
            '\t\tget_headerInfo: function (line) {\n',
            '\t\tif (line.indexOf("####") !== -1) {\n',
            '\t\treturn 4;\n',
            '\t\t} else if (line.indexOf("###") !== -1) {\n',
            '\t\treturn 3;\n',
            '\t\t} else if (line.indexOf("##") !== -1) {\n',
            '\t\treturn 2;\n',
            '\t\t} else if (line.indexOf("#") !== -1) {\n',
            '\t\treturn 1;\n',
            '\t\t}\n',
            '\t\t},\n',
            '\t\t\n',
            '\t\t},\n',
            '\t\tremoval: {\n',
            '\t\tremove_headerMD: function (origin_line, md_info) {\n',
            '\t\t//header1(#) : 1\n',
            '\t\t//header2(##) : 2\n',
            '\t\t//header3(###) : 3\n',
            '\t\t//header4(####) : 4\n',
            '\t\twhile (true) {\n',
            '\t\tif (origin_line.indexOf("#") !== -1) {\n',
            '\t\tlet header_loc = origin_line.indexOf("#");\n',
            '\t\t\n',
            '\t\torigin_line = origin_line.substr(0, header_loc) + origin_line.substr(header_loc + 1, origin_line.length);\n',
            '\t\tmd_info.splice(header_loc, 1);\n',
            '\t\t} else {\n',
            '\t\tbreak;\n',
            '\t\t}\n',
            '\t\t}\n',
            '\t\tlet result = {\n',
            '\t\torigin_line: origin_line,\n',
            '\t\tmd_info: md_info.slice()\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t},\n',
            '\t\t\n',
            '\t\tremove_emphasisMD: function (origin_line, md_info) {\n',
            '\t\t// emphasis code : 5\n',
            '\t\twhile (true) {\n',
            '\t\tif (origin_line.indexOf("__") !== -1) {\n',
            '\t\tlet loc1 = origin_line.indexOf("__");\n',
            '\t\t\n',
            '\t\torigin_line = origin_line.substr(0, loc1) + origin_line.substr(loc1 + 2, origin_line.length);\n',
            '\t\tmd_info.splice(loc1, 2);\n',
            '\t\t} else {\n',
            '\t\tbreak;\n',
            '\t\t}\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\tlet result = {\n',
            '\t\torigin_line: origin_line,\n',
            '\t\tmd_info: md_info.slice(),\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t},\n',
            '\t\t\n',
            '\t\tremove_markMD: function (origin_line, md_info) {\n',
            '\t\t// mark code : 6\n',
            '\t\twhile (true) {\n',
            '\t\tif (origin_line.indexOf("@mark{") !== -1) {\n',
            '\t\tlet loc = origin_line.indexOf("@mark{");\n',
            '\t\t\n',
            '\t\torigin_line = origin_line.substr(0, loc) + origin_line.substr(loc + 6, origin_line.length);\n',
            '\t\t\n',
            '\t\tmd_info.splice(loc, 6);\n',
            '\t\t} else {\n',
            '\t\tbreak;\n',
            '\t\t}\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\tlet md_code = MD_Module.MD_CODE.mark_code;\n',
            '\t\t\n',
            '\t\t\n',
            '\t\tlet processed_info = this.remove_closeParen(origin_line, md_info, md_code);\n',
            '\t\t\n',
            '\t\t\n',
            '\t\tlet result = {\n',
            '\t\torigin_line: processed_info.origin_line,\n',
            '\t\tmd_info: processed_info.md_info.slice(),\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t}\n',
            '\t\t,\n',
            '\t\tremove_uMD: function (origin_line, md_info) {\n',
            '\t\t// u code : 8\n',
            '\t\twhile (true) {\n',
            '\t\tif (origin_line.indexOf("@u{") !== -1) {\n',
            '\t\tlet loc = origin_line.indexOf("@u{");\n',
            '\t\t\n',
            '\t\torigin_line = origin_line.substr(0, loc) + origin_line.substr(loc + 3, origin_line.length);\n',
            '\t\tmd_info.splice(loc, 3);\n',
            '\t\t} else {\n',
            '\t\tbreak;\n',
            '\t\t}\n',
            '\t\t}\n',
            '\t\tlet md_code = MD_Module.MD_CODE.u_code;\n',
            '\t\t\n',
            '\t\tlet processed_info = this.remove_closeParen(origin_line, md_info, md_code);\n',
            '\t\t\n',
            '\t\t\n',
            '\t\tlet result = {\n',
            '\t\torigin_line: processed_info.origin_line,\n',
            '\t\tmd_info: processed_info.md_info.slice(),\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t},\n',
            '\t\tremove_closeParen: function (origin_line, md_info, md_code) {\n',
            '\t\tlet paren_info = {\n',
            '\t\tis_find: false,\n',
            '\t\tloc: -1\n',
            '\t\t};\n',
            '\t\tlet start_p = 0;\n',
            '\t\tfor (let i = 0; i < md_info.length; i++) {\n',
            '\t\tif (start_p === 0 && md_info[i].indexOf(md_code) !== -1) {\n',
            '\t\tstart_p = i;\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\tif (start_p !== 0 && md_info[i].indexOf(md_code) === -1) {\n',
            '\t\torigin_line = origin_line.substr(0, i) + origin_line.substr(i + 1, origin_line.length);\n',
            '\t\tmd_info.splice(i, 1);\n',
            '\t\tstart_p = 0;\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\t}\n',
            '\t\tlet result = {\n',
            '\t\torigin_line: origin_line,\n',
            '\t\tmd_info: md_info.slice(),\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t\n',
            '\t\t},\n',
            '\t\tremove_All_colorMD: function (origin_line, md_info, color_style) {\n',
            '\t\tfunction remove_colorMD(color, origin_line, md_info) {\n',
            '\t\tlet color_tag = "@" + color + "{";\n',
            '\t\t\n',
            '\t\twhile (true) {\n',
            '\t\tif (origin_line.indexOf(color_tag) !== -1) {\n',
            '\t\tlet loc = origin_line.indexOf(color_tag);\n',
            '\t\torigin_line = origin_line.substr(0, loc) + origin_line.substr(loc + color_tag.length, origin_line.length);\n',
            '\t\tmd_info.splice(loc, color_tag.length);\n',
            '\t\t} else {\n',
            '\t\tbreak;\n',
            '\t\t}\n',
            '\t\t}\n',
            '\t\tlet result = {\n',
            '\t\torigin_line: origin_line,\n',
            '\t\tmd_info: md_info.slice(),\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\t\n',
            '\t\tlet color_lists = Object.keys(color_style);\n',
            '\t\tfor (let i = 0; i < color_lists.length; i++) {\n',
            '\t\tlet color = color_lists[i];\n',
            '\t\tlet color_result = remove_colorMD(color, origin_line, md_info)\n',
            '\t\torigin_line = color_result.origin_line;\n',
            '\t\tmd_info = color_result.md_info;\n',
            '\t\t\n',
            '\t\tlet md_code = MD_Module.MD_CODE["color_" + color + "_code"];\n',
            '\t\t\n',
            '\t\t\n',
            '\t\tlet processed_info = this.remove_closeParen(origin_line, md_info, md_code);\n',
            '\t\t\n',
            '\t\t\n',
            '\t\t\n',
            '\t\torigin_line = processed_info.origin_line;\n',
            '\t\tmd_info = processed_info.md_info.slice();\n',
            '\t\t\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\tlet result = {\n',
            '\t\torigin_line: origin_line,\n',
            '\t\tmd_info: md_info.slice()\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t\n',
            '\t\t},\n',
            '\t\tremove_Allmd: function (origin_line, md_info) {\n',
            '\t\tlet header_result = this.remove_headerMD(origin_line, md_info);\n',
            '\t\torigin_line = header_result.origin_line;\n',
            '\t\tmd_info = header_result.md_info;\n',
            '\t\t\n',
            '\t\tlet emphasis_result = this.remove_emphasisMD(origin_line, md_info);\n',
            '\t\torigin_line = emphasis_result.origin_line;\n',
            '\t\tmd_info = emphasis_result.md_info;\n',
            '\t\t\n',
            '\t\tlet mark_result = this.remove_markMD(origin_line, md_info);\n',
            '\t\torigin_line = mark_result.origin_line;\n',
            '\t\tmd_info = mark_result.md_info;\n',
            '\t\t\n',
            '\t\tlet u_result = this.remove_uMD(origin_line, md_info);\n',
            '\t\torigin_line = u_result.origin_line;\n',
            '\t\tmd_info = u_result.md_info;\n',
            '\t\t\n',
            '\t\tconst COLOR_STYLE = {\n',
            '\t\tyellow: "#FFFF00",\n',
            '\t\tred: "#FF0000",\n',
            '\t\tblue: "#0000FF",\n',
            '\t\tgreen: "#008000",\n',
            '\t\t}\n',
            '\t\tlet color_result = this.remove_All_colorMD(origin_line, md_info, COLOR_STYLE);\n',
            '\t\torigin_line = color_result.origin_line;\n',
            '\t\tmd_info = color_result.md_info;\n',
            '\t\t\n',
            '\t\tlet result = {\n',
            '\t\torigin_line: origin_line,\n',
            '\t\tmd_info: md_info.slice()\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t}\n',
            '\t\t},\n',
            '\t\tcreator: {\n',
            '\t\tcreate_MDinfo: function (line) {\n',
            '\t\tfunction check_header_Instack(stack) {\n',
            '\t\tlet result = false;\n',
            '\t\tfor (let i = 0; i < 4; i++) {\n',
            '\t\tif (stack.indexOf(i + 1) !== -1) {\n',
            '\t\tresult = true;\n',
            '\t\tbreak;\n',
            '\t\t}\n',
            '\t\t}\n',
            '\t\treturn result;\n',
            '\t\t};\n',
            '\t\t//initial setting\n',
            '\t\tlet line_len = line.length;\n',
            '\t\tlet md_stk = [];\n',
            '\t\t\n',
            '\t\tlet line_info = [];\n',
            '\t\tfor (let j = 0; j < line_len; j++) {\n',
            '\t\tline_info.push([]);\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\tfor (let i = 0; i < line_len; i++) {\n',
            '\t\t// [MD 검사]\n',
            '\t\tif (line[i] === "#" && check_header_Instack(md_stk) === false) {\n',
            '\t\theader_code = MD_Module.getter.get_headerInfo(line);\n',
            '\t\tmd_stk.push(header_code);\n',
            '\t\t} else if (line[i] === "_" && line[i + 1] === "_") {\n',
            '\t\tif (md_stk.indexOf(MD_Module.MD_CODE.emphasis_code) !== -1) {\n',
            '\t\t// close tag\n',
            '\t\tlet close_idx = md_stk.indexOf(5);\n',
            '\t\tif (close_idx > -1) {\n',
            '\t\tmd_stk.splice(close_idx, 1);\n',
            '\t\t}\n',
            '\t\t} else {\n',
            '\t\t// open tag\n',
            '\t\tif (line.indexOf("__", i + 2) !== -1) {\n',
            '\t\tmd_stk.push(MD_Module.MD_CODE.emphasis_code);\n',
            '\t\t}\n',
            '\t\t}\n',
            '\t\t} else if (line[i] === "@" && line[i + 1] === "m") { //  mark_code=6;\n',
            '\t\tmd_stk.push(MD_Module.MD_CODE.mark_code);\n',
            '\t\t} else if (line[i] === "@" && line[i + 1] === "r") { // color_code=7;\n',
            '\t\tmd_stk.push(MD_Module.MD_CODE.color_red_code);\n',
            '\t\t} else if (line[i] === "@" && line[i + 1] === "b") { // color_code=7;\n',
            '\t\tmd_stk.push(MD_Module.MD_CODE.color_blue_code);\n',
            '\t\t} else if (line[i] === "@" && line[i + 1] === "y") { // color_code=7;\n',
            '\t\tmd_stk.push(MD_Module.MD_CODE.color_yellow_code);\n',
            '\t\t} else if (line[i] === "@" && line[i + 1] === "g") { // color_code=7;\n',
            '\t\tmd_stk.push(MD_Module.MD_CODE.color_green_code);\n',
            '\t\t} else if (line[i] === "@" && line[i + 1] === "u") { // u_code=8;\n',
            '\t\tmd_stk.push(MD_Module.MD_CODE.u_code);\n',
            '\t\t} else if (line[i] === "}") {\n',
            '\t\tlet remove_idx = MD_Module.tool.parag_match(md_stk);\n',
            '\t\tmd_stk.splice(remove_idx, 1);\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\t// [MD 적용]\n',
            '\t\tline_info[i] = md_stk.slice();\n',
            '\t\t\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\t\n',
            '\t\treturn line_info;\n',
            '\t\t\n',
            '\t\t},\n',
            '\t\t/*\n',
            '\t\theader_code : 0,\n',
            '\t\temphasis_code : 5,\n',
            '\t\tmark_code  :6,\n',
            '\t\tcolor_code : 7,\n',
            '\t\tu_code: 8,\n',
            '\t\tMD_Module\n',
            '\t\t\n',
            '\t\t*/\n',
            '\t\tcreate_spanDIV: function (parent_node, processed_line, processed_md_info) {\n',
            '\t\tif (processed_line.length !== processed_md_info.length) {\n',
            '\t\talert("create span div error!");\n',
            '\t\t}\n',
            '\t\tparent_node.innerText="";\n',
            '\t\tfor (let i = 0; i < processed_line.length; i++) {\n',
            '\t\tlet span_tag = document.createElement("span"); //\n',
            '\t\tspan_tag.innerText = processed_line[i];\n',
            '\t\t\n',
            '\t\t// [1] header md check______\n',
            '\t\tif (processed_md_info[i].indexOf(1) !== -1) {\n',
            '\t\tspan_tag.style.fontSize = MD_Module.HEADER_STYLE.h1_size;\n',
            '\t\t}\n',
            '\t\tif (processed_md_info[i].indexOf(2) !== -1) {\n',
            '\t\t\n',
            '\t\tspan_tag.style.fontSize = MD_Module.HEADER_STYLE.h2_size;\n',
            '\t\t}\n',
            '\t\tif (processed_md_info[i].indexOf(3) !== -1) {\n',
            '\t\tspan_tag.style.fontSize = MD_Module.HEADER_STYLE.h3_size;\n',
            '\t\t}\n',
            '\t\tif (processed_md_info[i].indexOf(4) !== -1) {\n',
            '\t\tspan_tag.style.fontSize = MD_Module.HEADER_STYLE.h4_size;\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\t// [2] emphasis md check______\n',
            '\t\tif (processed_md_info[i].indexOf(5) !== -1) {\n',
            '\t\tspan_tag.style.fontWeight = MD_Module.BOLD_STYLE.fontWeight;\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\t// [3] mark md check______\n',
            '\t\tif (processed_md_info[i].indexOf(6) !== -1) {\n',
            '\t\tspan_tag.style.backgroundColor = MD_Module.HIGHLIGHT_STYLE.backgroundColor;\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\t// [4] u md check______\n',
            '\t\tif (processed_md_info[i].indexOf(8) !== -1) {\n',
            '\t\tspan_tag.style.textDecoration = MD_Module.UNDERLINE_STYLE.textDecoration;\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\t// [5] color md check______(color range : 11 ~ )\n',
            '\t\tif (processed_md_info[i].indexOf(11) !== -1) { //     color_red_code:11,\n',
            '\t\tspan_tag.style.color = MD_Module.COLOR_STYLE.red;\n',
            '\t\t}\n',
            '\t\tif (processed_md_info[i].indexOf(12) !== -1) { //        color_blue_code:12,\n',
            '\t\tspan_tag.style.color = MD_Module.COLOR_STYLE.blue;\n',
            '\t\t}\n',
            '\t\tif (processed_md_info[i].indexOf(13) !== -1) { //      color_yellow_code:13,\n',
            '\t\tspan_tag.style.color = MD_Module.COLOR_STYLE.yellow;\n',
            '\t\t}\n',
            '\t\tif (processed_md_info[i].indexOf(14) !== -1) { //         color_green_code:14,\n',
            '\t\tspan_tag.style.color = MD_Module.COLOR_STYLE.green;\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\tparent_node.appendChild(span_tag);\n',
            '\t\t}\n',
            '\t\tparent_node.appendChild(document.createElement("br"));\n',
            '\t\t},\n',
            '\t\t}\n',
            '\t\t\n',
            '\t\t}\n',
            #############
            # | Initial DOM setting|
            # main constant setting
            '\t\tlet BTN_ACTIVATION_COLOR="#47c58f";\n',
            '\t\tlet BTN_DEACTIVATION_COLOR="#696868";\n',
            # 1. DIV DOM
            '\t\tlet home_UI = document.querySelector(".description_UI");\n',
            '\t\tlet variable_UI = document.querySelector(".variable_UI");\n',
            '\t\tlet function_UI = document.querySelector(".function_UI");\n\n',
            '\t\tlet code_UI = document.querySelector(".code_UI");\n\n',

            # 2. Button DOM
            '\t\tlet home_btn=document.querySelector(".home_btn");\n',
            '\t\tlet variable_btn=document.querySelector(".variable_btn");\n',
            '\t\tlet function_btn=document.querySelector(".function_btn");\n\n',
            '\t\tlet code_btn=document.querySelector(".code_btn");\n\n',

            # Button Color Setting
            '\t\t\thome_btn.style.backgroundColor=BTN_ACTIVATION_COLOR;\n',  # Activate
            '\t\t\tvariable_btn.style.backgroundColor=BTN_DEACTIVATION_COLOR;\n',
            '\t\t\tfunction_btn.style.backgroundColor=BTN_DEACTIVATION_COLOR;\n',
            '\t\t\tcode_btn.style.backgroundColor=BTN_DEACTIVATION_COLOR;\n',

            # | Initial Object setting |  : All variable is global variable
            '\t\t<!--Initial Btn Variable Setting-->\n',
            '\t\tlet home_btn_activation=true;\n',
            '\t\tlet label_btn_activation=false;\n',
            '\t\tlet variable_btn_activation=false;\n',
            '\t\tlet function_btn_activation=false;\n\n',
            '\t\tlet code_btn_activation=false;\n\n',

            # Search Activation
            '\t\tlet func_search_focus=false;\n',
            '\t\tlet var_search_focus=false;\n\n',
            '\t\tlet code_search_focus=false;\n\n',

            # Button Visibility Setting
            '\t\t\thome_UI.style.display="block";\n',  # Activate
            '\t\t\tvariable_UI.style.display="none";\n',
            '\t\t\tfunction_UI.style.display="none";\n',
            '\t\t\tcode_UI.style.display="none";\n',

            # | Event Setting|
            # Button Event Setting
            '\t\thome_btn.addEventListener("click",main_Btn_func )\n',
            '\t\tvariable_btn.addEventListener("click", main_Btn_func)\n',
            '\t\tfunction_btn.addEventListener("click", main_Btn_func)\n\n',
            '\t\tcode_btn.addEventListener("click", main_Btn_func)\n\n',

            # Button Event Function
            '\t\tfunction main_Btn_func(event){   <!--main button function-->\n',
            '\t\t\tlet button_type=event.target.innerHTML\n',
            '\t\t\tswitch(button_type){\n',
            # [1. Home Button Click]_______
            '\t\t\t\tcase "Home":\n',
            '\t\t\t\t\thome_btn_activation=true;\n',  # activatge
            '\t\t\t\t\tvariable_btn_activation=false;\n',
            '\t\t\t\t\tfunction_btn_activation=false;\n\n',
            '\t\t\t\t\tcode_btn_activation=false;\n\n',

            '\t\t\t\t\thome_UI.style.display="block";\n',  # block
            '\t\t\t\t\thome_btn.style.backgroundColor =BTN_ACTIVATION_COLOR;\n',  # block
            '\t\t\t\t\tvariable_UI.style.display="none";\n',
            '\t\t\t\t\tvariable_btn.style.backgroundColor=BTN_DEACTIVATION_COLOR;\n',
            '\t\t\t\t\tfunction_UI.style.display="none";\n',
            '\t\t\t\t\tfunction_btn.style.backgroundColor=BTN_DEACTIVATION_COLOR;\n',
            '\t\t\t\t\tcode_UI.style.display="none";\n',
            '\t\t\t\t\tcode_btn.style.backgroundColor=BTN_DEACTIVATION_COLOR;\n',
            '\t\t\t\t\tbreak;\n\n',

            # [2. Variable Button Click]______
            '\t\t\tcase "Variable":\n',
            '\t\t\t\thome_btn_activation=false;\n',
            '\t\t\t\t\thome_btn.style.backgroundColor =BTN_DEACTIVATION_COLOR;\n',  # block
            '\t\t\t\tvariable_btn_activation=true;\n',  # activate
            '\t\t\t\t\tvariable_btn.style.backgroundColor =BTN_ACTIVATION_COLOR;\n',  # block
            '\t\t\t\tfunction_btn_activation=false;\n\n',
            '\t\t\t\t\tfunction_btn.style.backgroundColor =BTN_DEACTIVATION_COLOR;\n',  # block
            '\t\t\t\tcode_btn_activation=false;\n\n',
            '\t\t\t\t\tcode_btn.style.backgroundColor =BTN_DEACTIVATION_COLOR;\n',  # block

            '\t\t\t\thome_UI.style.display="none";\n',
            '\t\t\t\tvariable_UI.style.display="block";\n',  # block
            '\t\t\t\tfunction_UI.style.display="none";\n',
            '\t\t\t\tcode_UI.style.display="none";\n',
            '\t\t\t\t\tbreak;\n\n',

            # [3. Function Button Click]______
            '\t\t\tcase "Function":\n',
            '\t\t\t\thome_btn_activation=false;\n',
            '\t\t\t\t\thome_btn.style.backgroundColor =BTN_DEACTIVATION_COLOR;\n',  # block
            '\t\t\t\tvariable_btn_activation=false;\n',
            '\t\t\t\t\tvariable_btn.style.backgroundColor =BTN_DEACTIVATION_COLOR;\n',  # block
            '\t\t\t\tfunction_btn_activation=true;\n\n',  # activate
            '\t\t\t\t\tfunction_btn.style.backgroundColor =BTN_ACTIVATION_COLOR;\n',  # block
            '\t\t\t\tcode_btn_activation=true;\n\n',  # activate
            '\t\t\t\t\tcode_btn.style.backgroundColor =BTN_DEACTIVATION_COLOR;\n',  # block

            '\t\t\t\thome_UI.style.display="none";\n',
            '\t\t\t\tvariable_UI.style.display="none";\n',
            '\t\t\t\tfunction_UI.style.display="block";\n',  # block
            '\t\t\t\tcode_UI.style.display="none";\n',
            '\t\t\t\t\tbreak;\n\n',

            # [4. Code Button Click]______
            '\t\t\tcase "Code":\n',
            '\t\t\t\thome_btn_activation=false;\n',
            '\t\t\t\t\thome_btn.style.backgroundColor =BTN_DEACTIVATION_COLOR;\n',  # block
            '\t\t\t\tvariable_btn_activation=false;\n',
            '\t\t\t\t\tvariable_btn.style.backgroundColor =BTN_DEACTIVATION_COLOR;\n',  # block
            '\t\t\t\tfunction_btn_activation=true;\n\n',  # activate
            '\t\t\t\t\tfunction_btn.style.backgroundColor =BTN_DEACTIVATION_COLOR;\n',  # block
            '\t\t\t\tcode_btn_activation=true;\n\n',  # activate
            '\t\t\t\t\tcode_btn.style.backgroundColor =BTN_ACTIVATION_COLOR;\n',  # block

            '\t\t\t\thome_UI.style.display="none";\n',
            '\t\t\t\tvariable_UI.style.display="none";\n',
            '\t\t\t\tfunction_UI.style.display="none";\n',  # block
            '\t\t\t\tcode_UI.style.display="block";\n',
            '\t\t\t\t\tbreak;\n\n',

            '\t\t\t}\n',
            '\t\t}\n\n',
            ########################################[Description Setting]###############################

            '\t\t<!--Description DOM Setting-->\n',
            '\t\tlet description_readme= document.querySelector(".description_readme");\n\n',

            '\t\tlet readmeLine_num=description_readme.childElementCount;\n',
            '\t\tfor(let i=0; i<readmeLine_num;i++){\n',
            '\t\t\tif(i>=1){ // <!--header 제외-->\n',
            '\t\t\tlet readline = document.querySelector(".readme_" + (i - 1).toString());\n',
           '\t\t\tlet raw_line = readline.innerText;\n',
           '\t\t\tlet raw_mdinfo = MD_Module.creator.create_MDinfo(raw_line);\n',
           '\t\t\tlet converted = MD_Module.removal.remove_Allmd(raw_line, raw_mdinfo);\n',
           '\t\t\tlet processed_line = converted.origin_line;\n',
           '\t\t\tlet processed_info = converted.md_info;\n',
           '\t\t\tMD_Module.creator.create_spanDIV(readline, processed_line, processed_info);\n',
            '\t\t}\n',  ## Main Loop END
            '\t\t}\n\n',

            ########################################[Code Setting]######################################
            '\t<!--Code DOM Setting-->\n',
            '\tlet Code_Info={\n',
            '\tcomment_index:2,\n',
            '\t}\n',

            '\t<!--Code MD Application-->\n',
            '\tlet code__table= document.querySelector(".code__table");\n',
            '\tfor(let i=1;i<code__table.rows.length;i++){\n',
            '\tlet commentTD=code__table.rows[i].cells[Code_Info.comment_index];\n',
            '\tlet tdLine_num=commentTD.childElementCount;\n',
            '\tfor(let j=0;j<tdLine_num;j++){\n',

            '\tlet commentline=commentTD.querySelector(".comment_"+(j+1).toString());\n',

            '\tif (commentline!==null){ <!--encoding problem-->\n',
            '\tlet raw_line=commentline.innerText;\n',

            '\tlet raw_mdinfo = MD_Module.creator.create_MDinfo(raw_line);\n',

            '\tlet converted = MD_Module.removal.remove_Allmd(raw_line, raw_mdinfo);\n',
            '\tlet processed_line = converted.origin_line;\n',
            '\tlet processed_info = converted.md_info;\n',
            '\tMD_Module.creator.create_spanDIV(commentline, processed_line, processed_info);\n',
            '\t}\n',
            '\t}\n',
            '\t}\n',
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

            # (4). Variable Search Short Key Event_____________________
            '\t\tvariable_Search_Input.addEventListener("focusin", () => {\n',  # Event Setting
            '\t\tvar_search_focusIn();\n',
            '\t\t});\n\n',
            '\t\tvariable_Search_Input.addEventListener("focusout", () => {\n',  # Event Setting
            '\t\tvar_search_focusOut();\n',
            '\t\t});\n\n',

            '\t\tfunction var_search_focusIn(){\n',
            '\t\t\tvar_search_focus = true;\n',
            '\t\t}\n\n',

            '\t\tfunction var_search_focusOut(){\n',
            '\t\t\tvar_search_focus = false;\n',
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

            '\t\tfunction_Search_Input.addEventListener("focusin", () => {\n',  # Event Setting
            '\t\tfunc_search_focusIn();\n',
            '\t\t});\n\n',
            '\t\tfunction_Search_Input.addEventListener("focusout", () => {\n',  # Event Setting
            '\t\tfunc_search_focusOut();\n',
            '\t\t});\n\n',

            '\t\tfunction func_search_focusIn(){\n',
            '\t\t\tfunc_search_focus = true;\n',
            '\t\t}\n\n',

            '\t\tfunction func_search_focusOut(){\n',
            '\t\t\tfunc_search_focus = false;\n',
            '\t\t}\n\n',
            ########################################[Body Setting]####################################
            '\t\tlet body = document.getElementsByTagName("body")[0];\n\n',
            '\t\tbody.addEventListener("keypress", function (e) {\n',
            '\t\tif (e.key === "Enter") {\n',
            '\t\t\tif( var_search_focus==true){\n',
            '\t\t\t\tvar_search_Ok_btn_func();\n',
            '\t\t\t}else if( func_search_focus==true){\n',
            '\t\t\t\tfunc_search_Ok_btn_func();\n',
            '\t\t\t}\n',
            '\t\t}\n',
            '\t\t});\n\n',
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

            #############
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
        self.code_div_list=[]

        self.div_insert_location = {
            # Insert class name : HTML List
            HTML_Generator.Insert_classname["description"]: self.description_div_list,
            HTML_Generator.Insert_classname["variable"]:self.variable_div_list,
            HTML_Generator.Insert_classname["function"]:self.function_div_list,
            HTML_Generator.Insert_classname["code"]: self.code_div_list,
        }


    def update_all_htmlList(self):
        desc_insertClass_name= HTML_Generator.Insert_classname["description"]
        var_insertClass_name =HTML_Generator.Insert_classname["variable"]
        func_insertClass_name = HTML_Generator.Insert_classname["function"]
        code_insertClass_name = HTML_Generator.Insert_classname["code"]

        self.div_insert_location[desc_insertClass_name] = self.description_div_list
        self.div_insert_location[var_insertClass_name] = self.variable_div_list
        self.div_insert_location[func_insertClass_name] = self.function_div_list
        self.div_insert_location[code_insertClass_name] = self.code_div_list
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
                #print("debuh1",insert_className, insert_html)
                if (insert_html != []):
                    find_result = find_classLoc(self.html_base, insert_className)
                    #print("debuh134124", find_result)
                    if find_result["is_find"] == True:
                        #print("debuh2", insert_className)
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