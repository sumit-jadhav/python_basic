with open("C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\log.txt")as f:
    content=f.read().lower()

if 'python' in content:  # if 'python' in content.lower():
    print("Python is present ")
else:
    print("python is not present ")