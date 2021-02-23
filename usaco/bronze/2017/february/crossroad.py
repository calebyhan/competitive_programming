f = open("crossroad.in")

n = int(f.readline().strip())

lst = [-1] * 10

output = 0

for i in range(n):
  temp = list(map(int, f.readline().strip().split()))
  print(temp)
  if lst[temp[0] - 1] == -1:
    lst[temp[0] - 1] = temp[1]
  else:
    if lst[temp[0] - 1] != temp[1]:
      output += 1
      lst[temp[0] - 1] = temp[1]

f.close()

f = open("crossroad.out", "w")
f.write(str(output))
f.close()
