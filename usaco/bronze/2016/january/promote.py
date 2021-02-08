f = open("promote.in")
participants = []
for i in range(4):
  participants.append(list(map(int, f.readline().strip().split())))
f.close()

output = [0, 0, 0]

participants1 = []
for r in participants:
  participants1.append(r[1] - r[0])

for i in range(4):
  if i != 0:
    if participants1[i] != 0:
      for j in range(i):
        output[j] += participants1[i]

print(output)

f = open("promote.out", "w")
for i in output:
  f.write(str(i) + "\n")
f.close()
