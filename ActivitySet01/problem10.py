fname=input("enter file name:")
n=0
f=open(fname,"r")
c=f.readlines()
for i in c:
    k=i.split()
    if i.find("From ") != -1:
        print(k[1])
        n+=1
f.close()
print(f"There were {n} lines in the file with From as the first word")