import threading
#threading contains Condition
class XiaoAi(threading.Thread):
	def __init__(self,cond):
		super().__init__(name="小爱")
		self.cond = cond

	def run(self):
		with self.cond:
			self.cond.wait()
			print("{}:在".format(self.name))
			self.cond.notify()
			
			self.cond.wait()
			print("{}:好啊".format(self.name))
			self.cond.notify()
			
			self.cond.wait()
			print("{}:君住长江尾".format(self.name))
			self.cond.notify()
			
			self.cond.wait()
			print("{}:共饮长江水".format(self.name))
			self.cond.notify()
		
class TianMao(threading.Thread):
	def __init__(self,cond):
		super().__init__(name="天猫精灵")
		self.cond = cond
		
	def run(self):
		with self.cond:
			print("{}:小爱同学".format(self.name,))
			self.cond.notify()
			self.cond.wait()
			
			print("{}:我们来对古诗吧".format(self.name))
			self.cond.notify()
			self.cond.wait()
			
			print("{}:我住长江头".format(self.name))
			self.cond.notify()
			self.cond.wait()
			
			print("{}:日日思君不见君".format(self.name))
			self.cond.notify()
			self.cond.wait()
		
if __name__ == "__main__":
	cond = threading.Condition()
	xiaoai = XiaoAi(cond)
	tianmao = TianMao(cond)
	
	xiaoai.start()
	tianmao.start()
	
	