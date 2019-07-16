import time
import threading

def get_detail_html(url):
	print("get detail html started")
	time.sleep(2)
	print("get detail html end")
	
def get_detail_url(url):
	print("get detail url started")
	time.sleep(2)
	print("get detail url end")
	

	
class GetDetailHtml(threading.Thread):
	def __init__(self,name):
		super().__init__(name=name)
		
	def run(self):
		print("get detail html started")
		time.sleep(2)
		print("get detail html end")

class GetDetailUrl(threading.Thread):
	def __init__(self,name):
		super().__init__(name=name)
		
	def run(self):
		print("get detail url started")
		time.sleep(4)
		print("get detail url end")
		
if __name__ == "__main__":
	thread1 = GetDetailHtml("get_detail_html")
	thread2 = GetDetailUrl("get_detail_url")
	# thread1.setDaemon(True)
	# thread2.setDaemon(True)
	start_time = time.time()
	
	thread1.start()
	thread2.start()
	
	thread1.join()
	thread2.join()
	
	print("last time:{}".format(time.time()-start_time))