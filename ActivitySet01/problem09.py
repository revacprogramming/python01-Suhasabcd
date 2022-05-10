fname = input("Enter file name: ")
fh = open(fname)
a=[]
lst = list()
for line in fh:
    x=line.split()
    for i in x:
        if i not in a:
            a.append(i)
print(sorted(a))