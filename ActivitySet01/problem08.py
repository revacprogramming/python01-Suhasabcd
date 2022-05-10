# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
n,a=0,0
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        k=line.split()
    	a+=float(k[1])
        n+=1
print("Average spam confidence:",a/n)