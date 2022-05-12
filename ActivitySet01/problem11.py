name = "mbox-short.txt"
dic={ }
fh=open(name)
c=fh.readlines()
for i in c :
    k=i.split()
    if i.find("From ") != -1:
        if k[1] not in dic:
            dic[k[1]]=0
for i in c :
    k=i.split()
    if i.find("From ") != -1:
        if k[1] in dic:
            dic[k[1]]=dic[k[1]]+1
v=list(dic.values())
keys=list(dic.keys())
print(keys[v.index(max(v))],max(v))