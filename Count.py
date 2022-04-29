# python program to count the number of occurences of key value pair in a text file
file=open("jaanu.txt","r")
dct=dict()
for temp in file:
    temp=temp.strip()
    temp=temp.lower()
    readline=temp.split()
    for i in readline:
        if i in dct:
            dct[i]=dct[i]+1
        else:
            dct[i]=1
file.close()
print("count of: ")
for k in list(dct.keys()):
    print("{} is{}".format(k,dct[k]))                
    