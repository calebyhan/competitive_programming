f = open("cowtip.in")

n = int(f.readline().strip())

cows = []
for i in range(n):
  cows.append(list(map(int, f.readline().strip())))

f.close()

output = 0

def flip(lst, num1, num2):
  for i in range(num1 + 1):
    for j in range(num2 + 1):
      lst[i][j] = abs(lst[i][j] - 1)
  return lst

cows1 = list(cows)
for i in range(n - 1, -1, -1):
  for j in range(n - 1, -1, -1):
    temp = cows1[i][j]
    if temp == 1:
      cows1 = flip(cows1, i, j)
      output += 1

f = open("cowtip.out", "w")
f.write(str(output))
f.close()
