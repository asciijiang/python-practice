from concurrent.futures import ThreadPoolExecutor,as_completed
from concurrent.futures import ProcessPoolExecutor
import time

def fib(n):
	if n <= 2:
		return 1
	return fib(n-1)+fib(n-2)


def random_sleep(n):
	time.sleep(n)
	return n

if __name__ == "__main__":	
	with ProcessPoolExecutor(8) as executor:
		all_task = [executor.submit(random_sleep,(num)) for num in [2]*30 ]
		start_time = time.time()
		for future in as_completed(all_task):
			data = future.result()
			print("exe result:{}".format(data))
		
		print("Process pool last time is:{}".format(time.time()-start_time))
		
	with ThreadPoolExecutor(8) as executor:
		all_task = [executor.submit(random_sleep,(num)) for num in [2]*30 ]
		start_time = time.time()
		for future in as_completed(all_task):
			data = future.result()
			print("exe result:{}".format(data))
		
		print("Thread pool last time is:{}".format(time.time()-start_time))