import gevent, random
from gevent.queue import Queue

"""
Illustrates the use of a queue

Queues are ordered sets of data that have the usual put / get operations 
but are written in a way such that they can be safely manipulated across Greenlets.
For example if one Greenlet grabs an item off of the queue, the same 
item will not grabbed by another Greenlet executing simultaneously.
"""

tasks = Queue()

def boss():
	for i in xrange(1, 25):
		tasks.put_nowait(i)

def worker(n):
	while not tasks.empty():
		task = tasks.get()
		print('Worker {0} got task {1}'.format(n, task))
		tasktime = random.randint(1, 3)
		gevent.sleep(tasktime)
	print('all tasks finished')

def main():
	gevent.spawn(boss).join()
	
	gevent.joinall([
		gevent.spawn(worker, 'steve'),
		gevent.spawn(worker, 'john'),
		gevent.spawn(worker, 'nancy')		
	])

if __name__ == '__main__': main()
