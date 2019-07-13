class Quantity:
	def __init__(self,attrname):
		self.attrname = attrname
		
	def __get__(self,instance,owner):
		return instance.__dict__[self.attrname]
		
	def __set__(self,instance,value):
		if value > 0:
			instance.__dict__[self.attrname] = value
		else:
			raise ValueError("value must be bigger than zero")
			
class Fruits:
	weight = Quantity("weight")
	price = Quantity("price")
	
	def __init__(self,price,weight,description=None):
		self.description = description
		self.price = price
		self.weight = weight
		
	def subtotal(self):
		return self.price * self.weight
		
if __name__ == '__main__':
	k1 = Fruits(weight=2,price=3,description="k111")
	k2 = Fruits(price=4,weight=5)
	print(k1.subtotal())
	print(k2.subtotal())