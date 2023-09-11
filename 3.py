def factor(n):
	factors = []
	p = 2
	while n >= p^2:
		if n%p == 0:
			factors.append(p)
			while n%p == 0:
				n/=p
		else:
			p+=1
	
	if n != 1:
		factors.append(int(n))
	return factors

Factors = factor(2)
print(Factors)
