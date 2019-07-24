def gen_func():
	html = yield "http://projectsedu.com"
	print(html)
	yield 2
	yield 3
	return "bobby"
	
if __name__ == "__main__":
	gen = gen_func()
	url = gen.send(None)
	#download url
	html = "<html>jiang-yang</html>"
	print( gen.send(html)  )
	
	
	# print(next(gen))
	# print(next(gen))
	# print(next(gen))
	# print(next(gen))