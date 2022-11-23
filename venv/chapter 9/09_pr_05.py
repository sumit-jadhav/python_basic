words=["donkey","monkey","motu","chu"]

with open('C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\sample.txt') as f:
    content=f.read()
for word in words:
    content=content.replace(word,"#$$@@#")
    with open('C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\sample.txt',"w") as f:
        f.write(content)


