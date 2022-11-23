
# use open function to read the content of the file. 
#f=open('sample.txt','w')
f=open('C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\sample.txt')
data=f.read() 
#data=f.read(2)       IT WILL READ ONLY TWO CHARACTER FROM THE FILE
print(data)
f.close()