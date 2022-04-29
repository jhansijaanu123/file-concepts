#python program to reverse the single line of text
readfile=open('jaanu.txt','r')
row=readfile.readlines()
readfile.close()
selectrow=0
tmp=row[selectrow].split()
strrev=" ".join(tmp[::-1])
row.pop(selectrow)
row.insert(selectrow,strrev)
writefile=open('jaanu.txt','w')
writefile.writelines(row)
writefile.close()