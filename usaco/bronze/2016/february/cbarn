f = open("cbarn.in")
n = int(f.readline().strip())

rooms = []
for i in range(n):
  rooms.append(int(f.readline().strip()))

f.close()

output = 1000000000000

for i in range(n):
  total = sum(rooms)
  d = 0
  rooms1 = []
  for j in range(n):
    rooms1.append(rooms[(i + j) - n])
  for j in range(n - 1):
    total = total - rooms1[j]
    d += total
  output = min(d, output)

f = open("cbarn.out", "w")
f.write(str(output))
f.close()
