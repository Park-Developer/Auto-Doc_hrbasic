/*
   0 : none
   1 : header1(#)
   2 : header2(##)
   3 : header3(###)
   4 : header4(####)
   5 : emphasis
   6 : mark
   7 : color
   8 : u
   9 :
   */
 let MD_Module = {
     MD_CODE: {
         header_code: 0,
         emphasis_code: 5,
         mark_code: 6,
         reserved_code: 7,
         u_code: 8,
         color_red_code: 11,
         color_blue_code: 12,
         color_yellow_code: 13,
         color_green_code: 14,
     },


     HEADER_STYLE: {
         h1_size: "50px",
         h2_size: "40px",
         h3_size: "30px",
         h4_size: "20px",
         h5_size: "10px",
     },

     BOLD_STYLE: {
         fontWeight: "bold"
     },

     UNDERLINE_STYLE: {
         textDecoration: "underline"
     },

     HIGHLIGHT_STYLE: {
         backgroundColor: "#FFFF00"
     },

     COLOR_STYLE: {
         yellow: "#FFFF00",
         red: "#FF0000",
         blue: "#0000FF",
         green: "#008000",
     },
     tool: {
         parag_match: function (md_stk) {
             mark_loc = md_stk.indexOf(MD_Module.MD_CODE.mark_code);
             color_red_loc = md_stk.indexOf(MD_Module.MD_CODE.color_red_code);
             color_blue_loc = md_stk.indexOf(MD_Module.MD_CODE.color_blue_code);
             color_yellow_loc = md_stk.indexOf(MD_Module.MD_CODE.color_yellow_code);
             color_green_loc = md_stk.indexOf(MD_Module.MD_CODE.color_green_code);
             u_loc = md_stk.indexOf(MD_Module.MD_CODE.u_code);

             let max_idx = Math.max(mark_loc, color_yellow_loc, color_green_loc, color_blue_loc, color_red_loc, u_loc);
             return max_idx;
         },

     },
     getter: {
         get_headerInfo: function (line) {
             if (line.indexOf("####") !== -1) {
                 return 4;
             } else if (line.indexOf("###") !== -1) {
                 return 3;
             } else if (line.indexOf("##") !== -1) {
                 return 2;
             } else if (line.indexOf("#") !== -1) {
                 return 1;
             }
         },

     },
     removal: {
         remove_headerMD: function (origin_line, md_info) {
             //header1(#) : 1
             //header2(##) : 2
             //header3(###) : 3
             //header4(####) : 4
             while (true) {
                 if (origin_line.indexOf("#") !== -1) {
                     let header_loc = origin_line.indexOf("#");

                     origin_line = origin_line.substr(0, header_loc) + origin_line.substr(header_loc + 1, origin_line.length);
                     md_info.splice(header_loc, 1);
                 } else {
                     break;
                 }
             }
             let result = {
                 origin_line: origin_line,
                 md_info: md_info.slice()
             }
             return result;
         },

         remove_emphasisMD: function (origin_line, md_info) {
             // emphasis code : 5
             while (true) {
                 if (origin_line.indexOf("__") !== -1) {
                     let loc1 = origin_line.indexOf("__");

                     origin_line = origin_line.substr(0, loc1) + origin_line.substr(loc1 + 2, origin_line.length);
                     md_info.splice(loc1, 2);
                 } else {
                     break;
                 }
             }

             let result = {
                 origin_line: origin_line,
                 md_info: md_info.slice(),
             }
             return result;
         },

         remove_markMD: function (origin_line, md_info) {
             // mark code : 6
             while (true) {
                 if (origin_line.indexOf("@mark{") !== -1) {
                     let loc = origin_line.indexOf("@mark{");

                     origin_line = origin_line.substr(0, loc) + origin_line.substr(loc + 6, origin_line.length);

                     md_info.splice(loc, 6);
                 } else {
                     break;
                 }
             }

             let md_code = MD_Module.MD_CODE.mark_code;


             let processed_info = this.remove_closeParen(origin_line, md_info, md_code);


             let result = {
                 origin_line: processed_info.origin_line,
                 md_info: processed_info.md_info.slice(),
             }
             return result;
         }
         ,
         remove_uMD: function (origin_line, md_info) {
             // u code : 8
             while (true) {
                 if (origin_line.indexOf("@u{") !== -1) {
                     let loc = origin_line.indexOf("@u{");

                     origin_line = origin_line.substr(0, loc) + origin_line.substr(loc + 3, origin_line.length);
                     md_info.splice(loc, 3);
                 } else {
                     break;
                 }
             }
             let md_code = MD_Module.MD_CODE.u_code;

             let processed_info = this.remove_closeParen(origin_line, md_info, md_code);


             let result = {
                 origin_line: processed_info.origin_line,
                 md_info: processed_info.md_info.slice(),
             }
             return result;
         },
         remove_closeParen: function (origin_line, md_info, md_code) {
             let paren_info = {
                 is_find: false,
                 loc: -1
             };
             let start_p = 0;
             for (let i = 0; i < md_info.length; i++) {
                 if (start_p === 0 && md_info[i].indexOf(md_code) !== -1) {
                     start_p = i;
                 }

                 if (start_p !== 0 && md_info[i].indexOf(md_code) === -1) {
                     origin_line = origin_line.substr(0, i) + origin_line.substr(i + 1, origin_line.length);
                     md_info.splice(i, 1);
                     start_p = 0;
                 }

             }
             let result = {
                 origin_line: origin_line,
                 md_info: md_info.slice(),
             }
             return result;

         },
         remove_All_colorMD: function (origin_line, md_info, color_style) {
             function remove_colorMD(color, origin_line, md_info) {
                 let color_tag = "@" + color + "{";

                 while (true) {
                     if (origin_line.indexOf(color_tag) !== -1) {
                         let loc = origin_line.indexOf(color_tag);
                         origin_line = origin_line.substr(0, loc) + origin_line.substr(loc + color_tag.length, origin_line.length);
                         md_info.splice(loc, color_tag.length);
                     } else {
                         break;
                     }
                 }
                 let result = {
                     origin_line: origin_line,
                     md_info: md_info.slice(),
                 }
                 return result;
             }


             let color_lists = Object.keys(color_style);
             for (let i = 0; i < color_lists.length; i++) {
                 let color = color_lists[i];
                 let color_result = remove_colorMD(color, origin_line, md_info)
                 origin_line = color_result.origin_line;
                 md_info = color_result.md_info;

                 let md_code = MD_Module.MD_CODE["color_" + color + "_code"];


                 let processed_info = this.remove_closeParen(origin_line, md_info, md_code);



                 origin_line = processed_info.origin_line;
                 md_info = processed_info.md_info.slice();

             }

             let result = {
                 origin_line: origin_line,
                 md_info: md_info.slice()
             }
             return result;

         },
         remove_Allmd: function (origin_line, md_info) {
             let header_result = this.remove_headerMD(origin_line, md_info);
             origin_line = header_result.origin_line;
             md_info = header_result.md_info;

             let emphasis_result = this.remove_emphasisMD(origin_line, md_info);
             origin_line = emphasis_result.origin_line;
             md_info = emphasis_result.md_info;

             let mark_result = this.remove_markMD(origin_line, md_info);
             origin_line = mark_result.origin_line;
             md_info = mark_result.md_info;

             let u_result = this.remove_uMD(origin_line, md_info);
             origin_line = u_result.origin_line;
             md_info = u_result.md_info;

             const COLOR_STYLE = {
                 yellow: "#FFFF00",
                 red: "#FF0000",
                 blue: "#0000FF",
                 green: "#008000",
             }
             let color_result = this.remove_All_colorMD(origin_line, md_info, COLOR_STYLE);
             origin_line = color_result.origin_line;
             md_info = color_result.md_info;

             let result = {
                 origin_line: origin_line,
                 md_info: md_info.slice()
             }
             return result;
         }
     },
     creator: {
         create_MDinfo: function (line) {
             function check_header_Instack(stack) {
                 let result = false;
                 for (let i = 0; i < 4; i++) {
                     if (stack.indexOf(i + 1) !== -1) {
                         result = true;
                         break;
                     }
                 }
                 return result;
             };
             //initial setting
             let line_len = line.length;
             let md_stk = [];

             let line_info = [];
             for (let j = 0; j < line_len; j++) {
                 line_info.push([]);
             }

             for (let i = 0; i < line_len; i++) {
                 // [MD 검사]
                 if (line[i] === "#" && check_header_Instack(md_stk) === false) {
                     header_code = MD_Module.getter.get_headerInfo(line);
                     md_stk.push(header_code);
                 } else if (line[i] === "_" && line[i + 1] === "_") {
                     console.log(i);
                     if (md_stk.indexOf(MD_Module.MD_CODE.emphasis_code) !== -1) {
                         // close tag
                         let close_idx = md_stk.indexOf(5);
                         if (close_idx > -1) {
                             md_stk.splice(close_idx, 1);
                         }
                     } else {
                         // open tag
                         if (line.indexOf("__", i + 2) !== -1) {
                             md_stk.push(MD_Module.MD_CODE.emphasis_code);
                         }
                     }
                 } else if (line[i] === "@" && line[i + 1] === "m") { //  mark_code=6;
                     md_stk.push(MD_Module.MD_CODE.mark_code);
                 } else if (line[i] === "@" && line[i + 1] === "r") { // color_code=7;
                     md_stk.push(MD_Module.MD_CODE.color_red_code);
                 } else if (line[i] === "@" && line[i + 1] === "b") { // color_code=7;
                     md_stk.push(MD_Module.MD_CODE.color_blue_code);
                 } else if (line[i] === "@" && line[i + 1] === "y") { // color_code=7;
                     md_stk.push(MD_Module.MD_CODE.color_yellow_code);
                 } else if (line[i] === "@" && line[i + 1] === "g") { // color_code=7;
                     md_stk.push(MD_Module.MD_CODE.color_green_code);
                 } else if (line[i] === "@" && line[i + 1] === "u") { // u_code=8;
                     md_stk.push(MD_Module.MD_CODE.u_code);
                 } else if (line[i] === "}") {
                     let remove_idx = MD_Module.tool.parag_match(md_stk);
                     md_stk.splice(remove_idx, 1);
                 }

                 // [MD 적용]
                 line_info[i] = md_stk.slice();

             }


             console.log(line_info);
             return line_info;

         },
         /*
         header_code : 0,
         emphasis_code : 5,
         mark_code  :6,
         color_code : 7,
         u_code: 8,
         MD_Module

         */
         create_spanDIV: function (parent_node, processed_line, processed_md_info) {
             if (processed_line.length !== processed_md_info.length) {
                 alert("create span div error!");
             }
             for (let i = 0; i < processed_line.length; i++) {
                 let span_tag = document.createElement("span"); //
                 span_tag.innerText = processed_line[i];

                 // [1] header md check______
                 if (processed_md_info[i].indexOf(1) !== -1) {
                     span_tag.style.fontSize = MD_Module.HEADER_STYLE.h1_size;
                 }
                 if (processed_md_info[i].indexOf(2) !== -1) {

                     span_tag.style.fontSize = MD_Module.HEADER_STYLE.h2_size;
                 }
                 if (processed_md_info[i].indexOf(3) !== -1) {
                     span_tag.style.fontSize = MD_Module.HEADER_STYLE.h3_size;
                 }
                 if (processed_md_info[i].indexOf(4) !== -1) {
                     span_tag.style.fontSize = MD_Module.HEADER_STYLE.h4_size;
                 }

                 // [2] emphasize md check______
                 if (processed_md_info[i].indexOf(5) !== -1) {
                     span_tag.style.fontWeight = MD_Module.BOLD_STYLE.fontWeight;
                 }

                 // [3] mark md check______
                 if (processed_md_info[i].indexOf(6) !== -1) {
                     span_tag.style.backgroundColor = MD_Module.HIGHLIGHT_STYLE.backgroundColor;
                 }

                 // [4] u md check______
                 if (processed_md_info[i].indexOf(8) !== -1) {
                     span_tag.style.textDecoration = MD_Module.UNDERLINE_STYLE.textDecoration;
                 }

                 // [5] color md check______(color range : 11 ~ )
                 if (processed_md_info[i].indexOf(11) !== -1) { //     color_red_code:11,
                     span_tag.style.color = MD_Module.COLOR_STYLE.red;
                 }
                 if (processed_md_info[i].indexOf(12) !== -1) { //        color_blue_code:12,
                     span_tag.style.color = MD_Module.COLOR_STYLE.blue;
                 }
                 if (processed_md_info[i].indexOf(13) !== -1) { //      color_yellow_code:13,
                     span_tag.style.color = MD_Module.COLOR_STYLE.yellow;
                 }
                 if (processed_md_info[i].indexOf(14) !== -1) { //         color_green_code:14,
                     span_tag.style.color = MD_Module.COLOR_STYLE.green;
                 }

                 parent_node.appendChild(span_tag);
             }
         },
     }

 }

 let testdiv = document.querySelector(".test");
 testdiv.display = "flex";

 let raw_line = "__r__@u{a@mark{sd}h}l__ld__o##a@red{d}s__@blue{d}g__g";
 let raw_mdinfo = MD_Module.creator.create_MDinfo(raw_line);


 let converted = MD_Module.removal.remove_Allmd(raw_line, raw_mdinfo);

 let processed_line = converted.origin_line;
 let processed_info = converted.md_info;

 MD_Module.creator.create_spanDIV(testdiv, processed_line, processed_info);
