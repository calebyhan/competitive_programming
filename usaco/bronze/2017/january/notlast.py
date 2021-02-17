f = open("notlast.in")
n = int(f.readline().strip())

cows = {"Bessie": 0, "Elsie": 0, "Daisy": 0, "Gertie": 0, "Annabelle": 0, "Maggie": 0, 
"Henrietta": 0}
for i in range(n):
  temp = f.readline().strip().split()
  cows[temp[0]] += int(temp[1])

f.close()

temp = dict(sorted(cows.items(), key=lambda item: item[1]))

tie = False
first = (0, False)
second = (0, False)

for value in temp.values():
  if first[0] == 0 and not first[1]:
    first = (value, True)
  if second[0] == 0 and first[1] and value != first[0]:
    second = (value, True)

count = 0
for value in temp.values():
  if value == second[0]:
    count += 1


if count > 1 or second[0] == 0:
  tie = True

f = open("notlast.out", "w")
if tie:
  f.write("Tie\n")
else:
  f.write(list(temp.keys())[list(temp.values()).index(second[0])] + "\n")
f.close()
