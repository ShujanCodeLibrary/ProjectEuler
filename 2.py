fib = [1, 2]
count = 2
while fib[-1] <= 4000000:
	fib.append(fib[-2] + fib[-1])
	if fib[-1] % 2 == 0:
		count += fib[-1]
print(count)
