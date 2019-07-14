def gen_func():
	yield 1
	yield 2
	yield 3

def func():
	return 1
	
def fib2(index):
	re_list = []
	n,a,b = 0,0,1
	while n<index:
		re_list.append(b)
		a,b = b,a+b
		n = n+1
	return re_list
	
def gen_fib(index):
	n,a,b = 0,0,1
	while n<index:
		yield b
		a,b = b,a+b
		n += 1
	
if __name__ == "__main__":
	for data in gen_fib(10):
		print (data)
	# gen = gen_func()
	# for value in gen:
		# print(value)
	# print(fib2(10))
	# re = func()
	# pass
