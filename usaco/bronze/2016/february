f = open("pails.in")
x, y, m = map(int, f.readline().strip().split())
f.close()

def maxproduct(x, y):
  count = 1
  while True:
    if (x * count) > y:
      return count - 1
    count += 1

output = 0

for i in range(maxproduct(x, m) + 3):
  for j in range(maxproduct(y, m) + 3):
    if (x * i) + (y * j) <= m:
      output = max(output, (x * i) + (y * j))

f = open("pails.out", "w")
f.write(str(output))
f.close()
