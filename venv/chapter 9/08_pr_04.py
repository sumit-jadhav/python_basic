

with open('C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\sample.txt') as f:
    content=f.read()

content=content.replace("donkey","don$$@@#")

with open('C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\sample.txt',"w") as f:
    f.write(content)


