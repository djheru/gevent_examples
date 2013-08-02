import gevent
from gevent import Greenlet

'''
Spawning Greenlets
gevent has wrappers around Greenlet initialization
'''

def foo(message, n):
	'''
	Each thread will be passed the message 
	and n arguments after its initialization
	'''
	gevent.sleep(n)
	print(message)
	
def main():
	
	# new Greenlet instance running function foo
	thread1 = Greenlet.spawn(foo, 'Hello', 1)
	
	# gevent wrapper
	thread2 = gevent.spawn(foo, 'Word up!', 2)
	
	# Lambda expression instead of named function
	thread3 = gevent.spawn(lambda x: (x + 1), 2)
	
	threads = [thread1, thread2, thread3]
	
	# block till all threads are complete
	gevent.joinall(threads)

if __name__ == '__main__': main()
