f = open("crossroad.in")

n = int(f.readline().strip())

lst = []

output = 0

for i in range(n):
  temp = list(map(int, f.readline().strip().split()))
  temp1 = False
  temp2 = 0
  print(temp)
  for j in range(len(lst)):
    if temp[0] == lst[j][0]:
      temp1 = True
      temp2 = j
  if not temp1:
    if temp[1] == 1:
      lst.append(temp)
    else:
      lst.append([temp[0], -1])
  else:
    if temp[1] == 0:
      lst[temp2][1] -= 1
    else:
      lst[temp2][1] += 1
  for j in range(len(lst)):
    if lst[j][1] > 1:
      lst[j][1] = 1
    if lst[j][1] < -1:
      lst[j][1] = -1
  print(lst)
  lst1 = list(lst)
  for j in range(len(lst1)):
    if lst1[j][1] == 0:
      output += 1
      lst.remove(lst[j])
  print(output)
  print()


f.close()

f = open("crossroad.out", "w")
f.write(str(output))
f.close()
