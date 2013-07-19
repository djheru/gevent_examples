import gevent
from gevent import Timeout

def wait():
	gevent.sleep(2)
	
def main():
	timer = Timeout(1).start()
	thread1 = gevent.spawn(wait)
	
	try:
		thread1.join(timeout = timer)
	except Timeout:
		print('Thread1 timed out')
	
	# --
	
	timer = Timeout.start_new(1)
	thread2 = gevent.spawn(wait)
	
	try: 
		thread2.get(timeout = timer)
	except Timeout:
		print('thread2 timedout')
		
	# --
	
	try:
		gevent.with_timeout(1, wait)
	except Timeout:
		print('thread 3 timeout')

if __name__ == '__main__': main()
