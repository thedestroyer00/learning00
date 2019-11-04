# multi-threading in python 

import concurrent.futures
import time 

def thread(sec):
	print(f'{sec}The world is beautiful!')
	time.sleep(sec)
	return f'{sec}The world is still beautiful!'

with concurrent.futures.ThreadPoolExecutor() as executor:
	secs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	t = [executor.submit(thread, sec) for sec in secs]
	for i in concurrent.futures.as_completed(t):
		 print(i.result())
	 
	
	
