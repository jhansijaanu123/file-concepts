# python program to copy odd lines of one file to another
file1=open('jaanu.txt','r')
file2=open('raj.txt','w')
lines=file1.readlines()
type(lines)
for i in range(0,len(lines)):
    if(i % 2 !=0):
        file2.write(lines[i])
file1.close()
file2.close()
file1=open ('jaanu.txt','r')
file2=open('raj.txt','r')
str1=file1.read()
str2=file2.read()
print("jaanu jhansi....")
print(str1)
print()
print("raj content....")
print(str2)
file1.close()
file2.close()