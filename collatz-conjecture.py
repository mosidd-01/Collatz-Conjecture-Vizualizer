list = []

def collatz_con(num):
  while num != 1:
    list.append(num)
    if num%2==0:
      num = int(num/2)
    elif num%1==0:
      num = (3*num) + 1
  list.append(num)

collatz_con(17)
print(list)
    