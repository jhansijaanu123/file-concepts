#python program to print word by word in afile
with open ('jaanu.txt','r')as file:
    for line in file:
        for word in line.split():
            print(word)