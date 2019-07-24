def gen_func():
	yield "http://projectsedu.com"
	# print(html)
	yield 2
	yield 3
	return "jiang-yang"
	
if __name__ == "__main__":
	gen = gen_func()
	print ( next(gen) )
	gen.close()
	next(gen)