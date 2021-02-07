f = open("speeding.in")
n, m = map(int, f.readline().split(" "))
lines = f.readlines()
f.close()

limits = []
for i in range(n):
  temp = list(map(int, lines[i].split(" ")))
  for j in range(temp[0]):
    limits.append(temp[1])

bspeeds = []
for i in range(n):
  temp = list(map(int, lines[i + n].split(" ")))
  for j in range(temp[0]):
    bspeeds.append(temp[1])

output = 0

for i in range(100):
  if bspeeds[i] > limits[i]:
    output = max(output, bspeeds[i] - limits[i])

f = open("speeding.out", "w")
f.write(str(output))
f.close()
