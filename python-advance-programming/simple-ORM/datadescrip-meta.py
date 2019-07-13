class Field:
	pass
class Quantity(Field):
	def __init__(self):
		self.attrname = None
		
	def __get__(self,instance,owner):
		return instance.__dict__[self.attrname]
		
	def __set__(self,instance,value):
		if value > 0:
			instance.__dict__[self.attrname] = value
		else:
			raise ValueError("value must be bigger than zero")

class MyMeta(type):
	def __new__(cls,name,bases,attrs,**kwargs):
		for key,value in attrs.items():
			if isinstance(value,Field):
				# print(key)
				attrs[key].attrname = key
				
		return super().__new__(cls,name,bases,attrs,**kwargs)		
			
class Fruits(metaclass=MyMeta):
	weight = Quantity()
	price = Quantity()
	
	def __init__(self,price,weight,description=None):
		self.description = description
		self.price = price
		self.weight = weight
		
	def subtotal(self):
		return self.price * self.weight
		
if __name__ == '__main__':
	k1 = Fruits(weight=4,price=7,description="k111")
	k2 = Fruits(price=7,weight=8)
	# print(k1.weight,k1.price,k2.weight,k2.price)
	print(k1.subtotal())
	print(k2.subtotal())