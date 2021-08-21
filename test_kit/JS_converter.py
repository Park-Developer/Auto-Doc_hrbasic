red=[]
with open(r"/autodocJS.js", 'r', encoding='UTF-8') as file:
    for i, line in enumerate(file):
        red.append("\'"+"\\"+"t"+"\\"+"t"+line.strip()+"\\"+"n"+"\'"+",\n")

print(red)


f = open("dd.txt", 'w', encoding='utf8')
for data in red:
    f.write(data)

f.close()