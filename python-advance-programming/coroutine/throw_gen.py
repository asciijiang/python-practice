def gen_func():
	try:
		yield "http://projectsedu.com"
	except Exception as e:
		pass
	# yield "http://projectsedu.com"
	yield 2
	yield 3
	return "jiang-yang"
	
if __name__ == "__main__":
	gen = gen_func()
	print ( next(gen) )
	gen.throw(Exception,"download error")
	print( next(gen) )