
def add(a, b):
    return(a+b)


def output(a, b, sum):
    print(a,"+",b,"=",sum)


def main():
  a=int(input("A = "))
  b=int(input("B = "))  
  sum = add(a, b)
  output(a, b, sum)


main()