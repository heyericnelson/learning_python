a = 1
b = 2
c = 1
p_sq = []

while c ** 2 < 1000:
	p_sq.append(c ** 2)
	c += 1

for i in range(0, len(p_sq) - 2):
	for j in range(i + 1, len(p_sq - 1):
		if p_sq[i] + p_sq[j] == 