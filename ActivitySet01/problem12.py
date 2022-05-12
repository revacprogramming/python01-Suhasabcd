name = "mbox-short.txt"
dic=list()
a=list()
n=list()
fh=open(name)
c=fh.readlines()
for i in c :
    k=i.split(" ")
    if i.find("From ") != -1:
        if k[5] not in dic:
            dic.append(k[6])
for i in dic :
    b=i.split(":")
    a.append(b[0])
                            
           
a.sort() 
for i in a:
    if i not in n:
        print(i,a.count(i))
        n.append(i)