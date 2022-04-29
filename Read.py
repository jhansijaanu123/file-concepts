#python programe to read character bycharacter in file
file=open('jaanu.txt','r')
while 1:
    char=file.read(1)
    if not char:
        break
    print(char)
file.close()    
