f = open("crossroad.in")

n = int(f.readline().strip())

ids = []
cross = []

for i in range(n):
  temp = f.readline().strip().split()
  ids.append(int(temp[0]))
  cross.append(int(temp[1]))

f.close()

cows1 = []
cows2 = []

output = 0

for i in range(n):
  if ids[i] in cows1:
    if cross[i] == 1:
      cows2[cows1.index(ids[i])] += 1
    else:
      cows2[cows1.index(ids[i])] -= 1
  else:
    cows1.append(ids[i])
    if cross[i] == 1:
      cows2.append(1)
    else:
      cows2.append(-1)
  for j in range(len(cows2)):
    print(cows1, cows2)
    print(j)
    if j + 1 > len(cows2):
      break
    if cows2[j] == 0:
      output += 1
      cows1.remove(cows1[j])
      cows2.remove(cows2[j])
    print(output)



f = open("crossroad.out", "w")
f.write(str(output))
f.close()
