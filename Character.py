with  open ("def.txt","r")  as file:
    for readline in file:
        for str in readline.split():
            print(str)


