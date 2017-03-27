

def fib1(n):
	d = {}
	return __fib1__(n, d)

def __fib1__(n, d):
	if n<=2: return 1
	if n-1 not in d:
		ret1 = __fib1__(n-1, d)
	else:
		ret1 = d[n-1]
	if n-2 not in d:
		ret2 = __fib1__(n-2, d)
	else:
		ret2 = d[n-2]
	d[n] = ret1+ret2
	return  d[n]

def fib2(n):
	if n==1 or n==2:
		return 1

	d = {}

	for i in range(1, n+1):
		__fib1__(i, d)

	return d[n]

def sfib(n):
	return sfib(n-1)+sfib(n-2) if n>=2 else 1

def fib3(n):
	"""
	use list(array) for memoization and no recursion
	"""

	if n <= 2:
		return 1

	f = [0]*n
	f[0] = 1
	f[1] = 1

	for i in range(2, n):
		f[i] = f[i-1] + f[i-2]
	return f[n-1]

def fib4(n):
	"""
	use 2 temp vars for memoization, no list
	"""
	f0, f1 = 1, 1

	if n <= 2:
		return f0

	f = 0
	for i in range(2, n):
		f = f0 + f1
		f0, f1 = f1, f
	return f

def runtest(N):
	for i in range(1, N):
		# print i, sfib(i)
		# print i, fib1(i)
		# print i, fib2(i)
		# print i, fib3(i)
		print i, fib4(i)

if __name__ == '__main__':
	import timeit
	N = 1500
	T = 10
	print timeit.timeit("runtest(%s)"%N, setup="from __main__ import runtest", number=T)
	# runtest(10)