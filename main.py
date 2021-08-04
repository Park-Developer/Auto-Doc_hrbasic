

if __name__ == "__main__":
    testObj=HTML_Generator();




    html_file = open('html_file.html', 'w')
    html_file.write( testObj.returnHTML_Text())
    html_file.close()

