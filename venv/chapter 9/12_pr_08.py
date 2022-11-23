with open("C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\this.txt")as f:
    content=f.read()

with open("copy.txt","w") as f:
    f.write(content)