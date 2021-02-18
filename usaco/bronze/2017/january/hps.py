f = open("hps.in")
n = int(f.readline().strip())

plays = []
for i in range(n):
  plays.append(list(map(int, f.readline().strip().split())))

f.close()

def determine(a, b):
  #1 = scissors
  #2 = hoof
  #3 = paper
  if a == 1:
    if b == 2:
      return 0
    else:
      return 1
  elif a == 2:
    if b == 1:
      return 1
    else:
      return 0
  else:
    if b == 1:
      return 0
    else:
      return 1

possible = []
for i in range(1, 4):
  for j in range(1, 4):
    for k in range(1, 4):
      if i != j and i != k and j != k:
        if [i, j, k] not in possible:
          possible.append([i, j, k])

output = 0

for i in range(len(possible)):
  total = 0
  a = list(map(int, possible[i]))
  for j in range(n):
    det = ()
    if plays[j][0] == 1:
      if plays[j][1] == 2:
        det = (a[0], a[1])
      elif plays[j][1] == 3:
        det = (a[0], a[2])
    elif plays[j][0] == 2:
      if plays[j][1] == 1:
        det = (a[1], a[0])
      elif plays[j][1] == 3:
        det = (a[1], a[2])
    elif plays[j][0] == 3:
      if plays[j][1] == 1:
        det = (a[2], a[0])
      elif plays[j][1] == 2:
        det = (a[2], a[1])
    if plays[j][0] == plays[j][1]:
      continue
    else:

      total += determine(det[0], det[1])

  output = max(output, total)


f = open("hps.out", "w")
f.write(str(output))
f.close()
