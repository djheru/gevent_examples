import gevent
from gevent.queue import Queue, Empty

'''
this example illustrates a queue that blocks when the queue size reaches 3
the you can pass a timeout to the get method, and if no items show up in the queue in that timeframe
then it will raise an Empty exception
'''

tasks = Queue(maxsize = 3)

def worker(n):
	try:
		while True:
			task = tasks.get(timeout = 1)
			print('worker {0} got task {1}'.format(n, task))
			gevent.sleep(0)
	except Empty:
		print('Tasks all completed')

def boss():
	"""
	Boss will wait to hand out jobs until an individual worker
	is free since th maxsize of the task queue is 3
	"""
	for i in xrange(1, 10):
		tasks.put(i)
	print('Assigned all tasks for the first iteration')
	
	for i in xrange(10, 20):
		tasks.put(i)
	print('assigned all tasks for the 2nd iteration')
	
def main():
	gevent.joinall([
		gevent.spawn(boss),
		gevent.spawn(worker, 'timmay'),
		gevent.spawn(worker, 'kyle'),
		gevent.spawn(worker, 'kenny')
	])

if __name__ == '__main__': main()
