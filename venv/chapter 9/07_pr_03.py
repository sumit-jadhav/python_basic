
for i in range (2,21): #to create the txt file 
    with open (f'C:\\Users\\DELL\\Desktop\\msc\\code with harry\\venv\\chapter 9\\tables\\Mltiplication table of {i}.txt','w')as f:
        for j in range(1,11): #to create the table range to the table
            f.write(f"{i}*{j}={i*j}\n")