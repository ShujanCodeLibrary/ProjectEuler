factors = set()
for n in range(2, 21):
	p=2
	while n >= p**2:
		if n % p == 0:
			factors.add(p)
			while n % p == 0:
				n/=p
		else:
			p+=1
	if n != 1:
		factors.add(n)
ans = 1
for x in factors:
	ans *= x
print(ans)
