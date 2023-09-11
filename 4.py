def ispal(x, y):
	mult = list(str(x*y))
	rmult = list(reversed(mult))
	if mult == rmult:
		return int("".join(mult))
	else:
		return 0
count = 0
for x in range(100, 1000):
	for y in range(100, 1000):
		value = ispal(x, y)
		if value != 0 and value > count:
			count = value
			slurp = [x,y]
print(count)
print(slurp)
