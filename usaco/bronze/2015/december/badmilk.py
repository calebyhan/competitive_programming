f = open("badmilk.in")
n, m, d, s = map(int, f.readline().strip().split())

people = {}
for i in range(d):
  temp = list(map(int, f.readline().strip().split()))
  if temp[0] in people:
    people[temp[0]].append((temp[1], temp[2]))
  else:
    people[temp[0]] = [(temp[1], temp[2])]

print(people)

infected = {}
for i in range(s):
  temp = list(map(int, f.readline().strip().split()))
  infected[temp[0]] = temp[1]

print(infected)

badmilk = set()
for p, t in infected.items():
  drank = set()
  for i in people.values():
    for j in i:
      if j[1] < t:
        if len(drank) == len(infected):
          badmilk.add(j[0])
        else:
          drank.add(j[0])

print(badmilk)
doses = 0
for person, things in people.items():
  if badmilk in things[0]:
    doses += 1

print(doses)
