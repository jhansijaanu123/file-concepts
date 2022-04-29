#python program to merge two files in to third file
data=data2=""
with open('jaanu.txt')as fp:
    data=fp.read()
with open('raj.txt')as fp:
    data2=fp.read()
data += "\n" 
data += data2
with open('jhansi.txt','w')as fp:
    fp.write(data)