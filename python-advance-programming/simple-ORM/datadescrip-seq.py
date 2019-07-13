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
				attrs[key].attrname = "_"+key.upper()
				
		return super().__new__(cls,name,bases,attrs,**kwargs)		
			
class Fruits(metaclass=MyMeta):
	weight = Quantity()
	price = Quantity()
	
	def __init__(self,*args,**kwargs):
		for key,value in kwargs.items():
			setattr(self,key,value)
		
	def subtotal(self):
		return self.price * self.weight
		
if __name__ == '__main__':
	k1 = Fruits(weight=7,price=7,description="k111")
	k2 = Fruits(price=8,weight=8)
	# print(k1.weight,k1.price,k2.weight,k2.price)
	#print(k1.__dict__)
	print(getattr(k1,"weight"))
	print(getattr(k2,"weight"))
	setattr(k1,"weight",99)
	print(getattr(k1,"weight"))
	k1.__dict__["weight"] = -99
	print(getattr(k1,"weight"))
	print(k1.subtotal())
	k1.__dict__["_WEIGHT"] = -99
	print(getattr(k1,"weight"))
	print(k1.subtotal())	
	#print(k2.subtotal())
'''
运行结果：  -99 和 -693 是负数
D:\用户目录\我的文档\GitHub\python-practice\python-advance-programming\simple-OR
M>python datadescrip-seq.py
7
8
99
99
693
-99
-693

D:\用户目录\我的文档\GitHub\python-practice\python-advance-programming\simple-OR
M>
'''	