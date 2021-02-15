f = open("blocks.in")

n = int(f.readline().strip())

blocks = []
for i in range(n):
  blocks.append(list(f.readline().strip().split()))

f.close()

print(blocks)

output = [0] * 26

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(n):
  print()
  nums = [0] * 26
  nums1 = [0] * 26
  for j in blocks[i][0]:
    nums[alphabet.index(j)] += 1
  print(nums)
  for j in blocks[i][1]:
    nums1[alphabet.index(j)] += 1
  print(nums1)
  for j in range(26):
    temp = max(nums[j], nums1[j])
    if temp != 0:
      output[j] += temp
  print(output)

f = open("blocks.out", "w")
for i in range(26):
  f.write(str(output[i]) + "\n")
f.close()
