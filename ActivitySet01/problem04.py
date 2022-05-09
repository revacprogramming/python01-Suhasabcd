# Conditional Execution
hrs = input("Enter Hours:")
h = float(hrs)
rate=input("input rate")
r=float(rate)
if(h<=40):
    pay=(h*r)
elif(h>40):
    pay=40*r
    h=h-40
    pay=pay+(h*1.5*r)
print(pay)
