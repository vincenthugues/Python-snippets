"""
Collatz Conjecture

Start with a number n > 1. Find the number of steps it takes to reach one
using the following process: If n is even, divide it by 2. If n is odd,
multiply it by 3 and add 1.

https://github.com/karan/Projects
"""

def collatz_it(n):
	"""Compute the Collatz Conjecture iteratively."""
	if n < 1:
		return None
	
	step = 0
	while n > 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = n * 3 + 1
		step += 1
	return step

def collatz_rec(n, step = 0):
	"""Compute the Collatz Conjecture recursively."""	
	if n < 1:
		return None
	
	if n == 1:
		return step
	if n % 2 == 0:
		return collatz_rec(n / 2, step + 1)
	else:
		return collatz_rec(n * 3 + 1, step + 1)

print collatz_it(0)
print collatz_it(9)
print collatz_rec(10)
