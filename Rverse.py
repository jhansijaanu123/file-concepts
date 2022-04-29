#python program to reverse the content of a file and store it in another file
f1=open("jaanu.tct","w")
with open("raj.txt","r")as myfile:
    data=myfile.read()
data_1 = data[::-1] 
f1.write(data_1) 
f1.close()
