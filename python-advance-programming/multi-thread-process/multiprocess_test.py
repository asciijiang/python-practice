import os
import time

pid = os.fork()
#fork 只能在linux/unix下运行
print("bobby")

if pid == 0:
	print("子进程{},父进程：{}".format(os.getpid(),os.getppid() ) )
else:
	print('我是父进程：{}'.format(pid))
	
time.sleep(2)

