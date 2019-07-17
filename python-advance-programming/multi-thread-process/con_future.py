from concurrent.futures import ThreadPoolExecutor,as_completed
import time

def get_html(times):
	time.sleep(times)
	print("get page {} success".format(times))
	return times

executor = ThreadPoolExecutor(max_workers=2)

#通过submit函数提交执行的函数到线程池中
# task1 = executor.submit(get_html,(3))	
# task2 = executor.submit(get_html,(2))	

urls = [3,2,4]
all_task = [executor.submit(get_html,(url)) for url in urls]
	
for future in as_completed(all_task):
	data = future.result()
	print("get {} page success".format())
# print(task1.done() )
# print(task2.cancel())
# time.sleep(4)
# print(task1.done())
# print(task1.result())