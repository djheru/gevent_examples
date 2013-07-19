from gevent import sleep
from gevent.pool import Pool
from gevent.coros import BoundedSemaphore

'''
A bounded semaphore checks to make sure its current value doesn’t exceed its initial value. 
If it does, ValueError is raised. In most situations semaphores are used to guard resources with limited capacity.
number of release() calls - (number of acquire() calls + the value kwarg in the constructor)
'''

sem = BoundedSemaphore(2)

def worker1(n):
	sem.acquire()
	print("Worker: {0} acquired semaphore".format(n))
	sleep(1)
	sem.release()
	print('Worker {0} released semaphore'.format(n))
	
def worker2(n):
	# contextually
	with sem:
		print("Worker: {0} acquired semaphore".format(n))
		sleep(1)
	print('Worker {0} released semaphore'.format(n))
		
def main():
	pool = Pool()
	pool.map(worker1, xrange(0, 3))
	pool.map(worker2, xrange(3, 6))

if __name__ == '__main__': main()
