f = open("mowing.in")
n = int(f.readline().strip())

mowed = []
for i in range(n):
  temp = f.readline().strip().split()
  mowed.append([temp[0], int(temp[1])])

f.close()

f = open("mowing.out", "w")

print(mowed)

field = []
for i in range(2000):
  temp = []
  for j in range(2000):
    temp.append(0)
  field.append(temp)

field1 = list(field)

prev = [1000, 1000]
field[1000][1000] = 1

go = True
temp = 0

for i in range(1, n + 1):
  d = mowed[i - 1][0]
  for j in range(mowed[i - 1][1]):
    if d == "N":
      field[prev[0]][prev[1] + 1] = i
    elif d == "S":
      field[prev[0]][prev[1] - 1] = i
    elif d == "E":
      field[prev[0] + 1][prev[1]] = i
    else:
      field[prev[0] - 1][prev[1]] = i

for i in range(n):
  d = mowed[i][0]
  for j in range(mowed[i][1]):
    if go:
      if d == "N":
        if field1[prev[0]][prev[1] + 1] == 1:
          go = False
          temp = i + 1
        else:
          field1[prev[0]][prev[1] + 1] = 1
      elif d == "S":
        if field1[prev[0]][prev[1] - 1] == 1:
          go = False
          temp = i + 1
        else:
          field1[prev[0]][prev[1] - 1] = 1
      elif d == "E":
        if field1[prev[0] + 1][prev[1]] == 1:
          go = False
          temp = i + 1
        else:
          field1[prev[0] + 1][prev[1]] = 1
      else:
        if field1[prev[0] - 1][prev[1]] == 1:
          go = False
          temp = i + 1
        else:
          field1[prev[0] - 1][prev[1]] = 1

output = 0

if go:
  f.write(str(-1))
else:
  for i in range(temp):
    output += mowed[i][1]
  f.write(str(output))

f.close()
