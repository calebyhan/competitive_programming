f = open("square.in")
p1 = list(map(int, f.readline().strip().split()))
p2 = list(map(int, f.readline().strip().split()))
f.close()

xd1 = max(abs(p1[2] - p2[0]), abs(p1[3] - p2[1]))
yd1 = max(abs(p1[1] - p2[3]), abs(p1[0] - p2[2]))
xd2 = max(abs(p1[2] - p1[0]), abs(p1[3] - p1[1]))
yd2 = max(abs(p2[1] - p2[3]), abs(p2[0] - p2[2]))

side = max(max(xd1, yd1), max(xd2, yd2))

f = open("square.out", "w")
f.write(str(side * side))
f.close()
