#python program to remove lines starting with any prefix
file1=open('jaanu.txt','r')
file2=open('raj.txt','w')
for line in file1.readlines():
    if not(line.startswith('textgenerator')):
        print(line)
        file2.write(line)
file2.close() 
file1.close()       
