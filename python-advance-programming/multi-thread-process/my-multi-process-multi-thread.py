from concurrent.futures import ThreadPoolExecutor,as_completed
from concurrent.futures import ProcessPoolExecutor
import time

def work(process_name,thread_name,n):
	for i in range(2):
		time.sleep(n)
		print("process {} run thread {}!!".format(process_name,thread_name))
	return thread_name	

def single_process(name,n):
	with ThreadPoolExecutor(2) as executor:
		thread_task1 = executor.submit(work, name,"thread11",n  )
		thread_task2 = executor.submit(work, name,"thread22",n  )
		
		all_task = []
		all_task.append(thread_task1)
		all_task.append(thread_task2)
		
		for future in as_completed(all_task):
			data = future.result()
			#print("process {} thread {} ending!!".format(name,data))
		return name

if __name__ == "__main__":	
	with ProcessPoolExecutor(1) as executor:
		process_task1 = executor.submit(single_process,"process11",1)
		process_task2 = executor.submit(single_process,"process22",1)
		
		all_task = []
		all_task.append(process_task1)
		all_task.append(process_task2)
		
		
		for future in as_completed(all_task):
			data = future.result()
			print("process {} ending!!!".format(data))