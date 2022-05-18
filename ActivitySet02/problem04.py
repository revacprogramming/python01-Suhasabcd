def get_cs():
  s=input("Enter the string")
  return s


def cs_to_lot(cs):
  lot=cs.split()
  return lot



def lot_to_cs(lot):
  a=" "
  a=a.join(lot)
  return a


def main():
  cs=get_cs()
  lot=cs_to_lot(cs)  # convert connect string to list of tuples
  print(lot)
  cs=lot_to_cs(lot)  # convert list of strings to connect string
  print(cs)
main()
