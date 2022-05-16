import re
file_name="actualdata.txt"
f=open(file_name,"r")
c=f.read()
sum=0
num=re.findall("[0-9]+",c)
for i in num:
    sum=sum+int(i)
print(sum)
