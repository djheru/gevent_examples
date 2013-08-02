import gevent, random

'''
Illustrates asynchronous task running and 
contrasts it with sequential (synchronous) execution
'''

def task(pid):
	'''
	Some non-deterministic task
	'''
	duration = random.randint(0, 2) * 0.01
	gevent.sleep(duration)
	print('Task:', pid, 'duration:', duration, 'done')

def synchronous():
	for i in range(1, 10):
		task(i)

def asynchronous():
	threads = [gevent.spawn(task, i) for i in xrange(10)]
	gevent.joinall(threads)
	
def main():
	print('Synchronous: ')
	synchronous()
	
	print('Asynchronous: ')
	asynchronous()

if __name__ == '__main__': main()
