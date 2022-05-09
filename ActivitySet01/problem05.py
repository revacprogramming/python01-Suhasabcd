def computepay(h, r):
    if(h<=40):
    	pay=(h*r)
    elif(h>40):
    	pay=40*r
    	h=h-40
    	pay=pay+(h*1.5*r)
    return pay
    

hrs = input("Enter Hours:")
hrs=float(hrs)
rate=float(input("rate:"))
p = computepay(hrs,rate)
print("Pay",p)