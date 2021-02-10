f = open("angry.in")
n = int(f.readline().strip())

bales = []
for i in range(n):
  bales.append(int(f.readline().strip()))

f.close()

bales = sorted(bales)
print(bales)

output = 0
radius = 1

for i in range(n):
  left = []
  middle = i
  right = []
  count = 1
  for j in range(n):
    try:
      if i - j >= 0 and i - j < n:
        left.append(bales[i-j])
    except:
      continue
    try:
      if i + j + 1 < n:
        right.append(bales[i + j + 1])
    except:
      continue

  if bales[middle] in left:
    left.remove(bales[middle])
  if bales[middle] in right:
    right.remove(bales[middle])

  # print(list(reversed(left)), bales[middle], right)
  for j in left:
    print(j - middle, radius)
    if abs(j - middle) == radius:
      count += 1
    else:
      break
  for j in right:
    print(j - middle, radius)
    if abs(j - middle) == radius:
      count += 1
    else:
      break
  output = max(output, count)

  radius += 1

f = open("angry.out", "w")
f.write(str(output))
f.close()
