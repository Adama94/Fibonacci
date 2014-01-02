def fib(n):
	a, b = 0, 1
	print a
	for x in range(0, n - 1):
		print b
		a, b = b, a + b

if __name__ == '__main__':
	import sys
	if len(sys.argv) >= 2:
		if len(sys.argv) > 2:
			print "Ignoring extra arguments."
		fib(int(sys.argv[1]))
	else:
		print "You need to specify a number."