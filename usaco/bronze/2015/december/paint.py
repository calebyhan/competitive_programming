f = open("paint.in")
lines = f.readlines()
f.close()

john_paint = list(map(int, lines[0].split()))
bessie_paint = list(map(int, lines[1].split()))

fence = []
for i in range(100):
  fence.append(0)

paint = False
paint1 = False

for i in range(100):
  if i == john_paint[0] - 1:
    paint = True
  elif i == john_paint[1] - 1:
    paint = False
    fence[i] = 1
  if i == bessie_paint[0] - 1:
    paint1 = True
  elif i == bessie_paint[1] - 1:
    paint1 = False
    fence[i] = 1
  if paint or paint1:
    fence[i] = 1

count = 0
f = open("paint.out", "w")
for i in range(99):
  if fence[i] == 1 and fence[i] == fence[i + 1]:
    count += 1
f.write(str(count))
f.close()
