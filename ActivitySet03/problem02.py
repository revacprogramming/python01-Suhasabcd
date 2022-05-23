l=[]
t=int(input())
for i in range(t):
    hcf=1
    n=int(input())
    x=list(map(int,input().split()))
    if len(x)>n:
        print("input limit exceded")
        break

    sum_num=1
    sum_den=x[0]
    print(f"1/{x[0]} ",end="")
    for i in range(1,len(x)):
        print("+ ",end="")
        print(f"1/{x[i]}",end="")
        sum_num=(sum_den+sum_num*x[i])
        sum_den=(sum_den*x[i])
    for i in range(1, min(sum_den, sum_num)):

        if sum_num % i == 0 and sum_den % i == 0:
            hcf = i    
        
    sum_num=sum_num/hcf
    sum_den=sum_den/hcf
    print(f"= {int(sum_num)}/{int(sum_den)}")