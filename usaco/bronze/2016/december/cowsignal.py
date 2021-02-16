f = open("cowsignal.in")
m, n, k = map(int, f.readline().strip().split())

lines = []
for i in range(m):
  lines.append(list(f.readline().strip()))

f.close()

output = []

for i in range(m):
  temp = ""
  for j in range(n):
    for l in range(k):
      #print(i, j)
      temp += lines[i][j]
  for l in range(k):
    output.append(temp)

f = open("cowsignal.out", "w")
for i in output:
  f.write(i + "\n")
f.close()
