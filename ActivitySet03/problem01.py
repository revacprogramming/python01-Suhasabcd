t=int(input())
for i in range(t):
    x=list(map(int,input().split()))
    x1,y1=x[0],x[1]
    x2,y2=x[2],x[3]
    x3,y3=x[4],x[5]
    area=(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
    if area<0:
        print(area*-1)
    else:
        print(area)