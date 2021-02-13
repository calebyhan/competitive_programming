f = open("balancing.in")

n, b = map(int, f.readline().strip().split())
points = []

for i in range(n):
  points.append(list(map(int, f.readline().strip().split())))

f.close()

m = n

for a in range(0, b + 1, 2):
  for b in range(0, b + 1, 2):
    go = True
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for cow in points:
      if cow[0] > a:
        if cow[1] > b:
          q1 += 1
        elif cow[1] < b:
          q2 += 1
        else:
          go = False
          break
      elif cow[0] < a:
        if cow[1] > b:
          q4 += 1
        elif cow[1] < b:
          q3 += 1
        else:
          go = False
          break
      else:
        go = False
        break
    if not go:
      break
    m = min(m, max(q1, q2, q3, q4))

f = open("balancing.out", "w")
f.write(str(m))
f.close()
