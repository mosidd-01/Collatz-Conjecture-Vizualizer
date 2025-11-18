import matplotlib.pyplot as plt

list = []

def collatz_con(num):
  while num != 1:
    list.append(num)
    if num%2==0:
      num = int(num/2)
    elif num%1==0:
      num = (3*num) + 1
  list.append(num)

start_num = int(input("Enter a starting number: "))
collatz_con(start_num)
print(list)
print("steps: ", len(list))

plt.figure(figsize=(10, 6))
plt.plot(list, marker='o')
plt.title(f"Collatz Conjecture Starting from {list[0]}")
plt.xlabel('Step')
plt.ylabel('Number')
plt.grid(True)
plt.show()

    