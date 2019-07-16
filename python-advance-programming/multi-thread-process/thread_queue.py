import time
import threading

detail_url_list = []

def get_detail_html():
	#爬去文章详情页
	while True:
		if len(detail_url_list):
			global detail_url_list
			url = detail_url_list.pop()
			# for url in detail_url_list:
	
			print("get detail html started")
			time.sleep(2)
			print("get detail html end")
	
def get_detail_url():
	global detail_url_list
	#爬去文章列表页
	print("get detail url started")
	time.sleep(4)
	for i in range(20):
		detail_url_list.append("http://projectsedu.com/{id}".format(id=i))
	print("get detail url end")
	
#1 线程通信方式 - 共享变量

if __name__ == "__main__":
	thread_detail_url = threading.Thread(target=get_detail_url)
	
	

	
	
	