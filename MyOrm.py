import numbers

class Field:
	pass

class IntField(Field):
	def __init__(self,db_column=None,min_value=None,max_value=None):
		self.attrname = None
		self.db_column = db_column
		self.min_value = min_value
		self.max_value = max_value
		
		
		if min_value is not None:
			if not isinstance(min_value,numbers.Integral):
				raise ValueError("min_value must be int")
			elif min_value < 0:
				raise ValueError("min_value must be positive")
				
		if max_value is not None:
			if not isinstance(max_value,numbers.Integral):
				raise ValueError("max_value must be int")
			elif max_value < 0:
				raise ValueError("max_value must be positive")
		if min_value is not None and max_value is not None:
			if min_value > max_value:
				raise ValueError("min_value must be smaller than max_value")
		
	def __get__(self,instance,owner):
		return instance.__dict__[self.attrname]
	def __set__(self,instance,value):
		if not isinstance(value,numbers.Integral):
			raise ValueError("int value need")
		if value < self.min_value or value > self.max_value:
			raise ValueError("value must between min_value and max_value")
		instance.__dict__[self.attrname] = value
		
		
class CharField(Field):
	def __init__(self,db_column=None,max_length=None):
		self.attrname = None
		self.db_column = db_column
		if max_length is None:
			raise ValueError("you must specify max_length for charfield")
		self.max_length = max_length	
		
	def __get__(self,instance,owner):
		return instance.__dict__[self.attrname]
	def __set__(self,instance,value):
		if not isinstance(value,str):
			raise ValueError("string value need")
		if len(value) > self.max_length:
			raise ValueError("value length excess max_length")
		instance.__dict__[self.attrname] = value
		

class ModelMetaClass(type):
	def __new__(cls,name,bases,attrs,**kwargs):
		if name == "BaseModel":
			return   super().__new__(cls,name,bases,attrs,**kwargs)
	
		fields = {}
		for key,value in attrs.items():
			if isinstance(value,Field):
				attrs[key].attrname = key
				fields[key] = value
		attrs_meta = attrs.get("Meta",None)
		_meta = {}
		db_table = name.lower()
		if attrs_meta is not None:
			table = getattr(attrs_meta,"db_table",None)
			if table is not None:
				db_table = table
		_meta["db_table"] = db_table
		attrs["_meta"] = _meta
		attrs["fields"] = fields
		del attrs["Meta"]
		return super().__new__(cls,name,bases,attrs,**kwargs)
 		

class BaseModel(metaclass=ModelMetaClass):
	def __init__(self,*args,**kwargs):
		for key,value in kwargs.items():
			setattr(self,key,value)
		#super().__init__()
	def save(self):
		fields = []
		values = []
		for key,value in self.fields.items():
			db_column = value.db_column
			if db_column is None:
				db_column = key.lower()
			fields.append(db_column)
			value = getattr(self,key)
			if isinstance(value,str):
				value = "'"+value+"'"
				values.append(value)
			else:
				values.append(str(value))
			
		sql = "insert into {db_table}({fields}) value({values})".format(db_table=self._meta["db_table"],fields=",".join(fields),values=",".join(values))
		print(sql)

class User(BaseModel):
	name = CharField(db_column="myname",max_length=10) 
	age = IntField(min_value=0,max_value=100)
	
	class Meta:
		db_table = "user"
		pass
		
if __name__ == "__main__":
	user = User()
	user.name = "jiang"
	user.age = 30
	
	user2 = User(name="Michal",age=40)

	print(user.__dict__)
	print(user2.__dict__)
	user.save()
	user2.save()
