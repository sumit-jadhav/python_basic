i=1
content =True
with open("C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\log.txt")as f:
    while content:
         content=f.readline().lower()
         if 'python' in content:  # if 'python' in content.lower():
             print(content)
             print(f"Python is present on line number {i} ")
         i+=1
