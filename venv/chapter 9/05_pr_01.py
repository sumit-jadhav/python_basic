f=open('C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\poems.txt','r')
#w=f.write('how are u ')
t=f.read( )
if 'Twinkel' in t:
     print("twinkel is present in the poem")
else :
     print("twinkel is not present in the poem")
#print(count)
f.close()