t=int(input())
def decode(x):
    for i in range(len(x)):
        try:
            if x[i]==0:
                if x[i+1]==0:
                    print(0,end=" ")
                    x.pop(i+1)
                else:
                    for _ in range(x[i+1]):

                        print(x[i+2],end=" ")
                    x.pop(i+1)
                    x.pop(i+1)
            else:
                print(x[i],end=" ")

        except:
            continue
    print(" ")


for i in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    for i in range(len(x)-1):
        print(x[i],end=" ")
    print(x[i+1])
    decode(x)
