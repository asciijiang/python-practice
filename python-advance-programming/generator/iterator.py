from collections.abc import Iterator

class Company:
	def __init__(self,employee_list):
		self.employee = employee_list
	
	def __iter__(self):
		return MyIterator(self.employee)
		

class MyIterator(Iterator):
	def __init__(self,employee_list):
		self.iter_list = employee_list
		self.index = 0
	def __next__(self):
		try:
			word = self.iter_list[self.index]
		except IndexError:
			raise StopIteration
		self.index += 1
		return word
		

if __name__ == "__main__":
	company = Company(["tom","bob","jane"])
	my_itor = iter(company)
	# while True:
		# try:
			# print(next(my_itor))
		# except StopIteration:
			# pass
	for item in company:
		print(item)
	