class Menu:
  def __init__(self,name,quantity):
    self.name=name
    self.quantity=quantity


m1 = Menu("idly",10)
m2=Menu("vada",20)
x=[m1,m2]

for i in x:
    print(i.name,i.quantity)