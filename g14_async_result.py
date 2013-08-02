import gevent
from gevent.event import AsyncResult
a = AsyncResult()

'''
Illustrates the use of AsyncResult, which is a deferred
'''

def setter():
	"""
	After 3 seconds set the result of a
	"""
	gevent.sleep(3)
	a.set({'msg':'Hello!'})
	
def waiter():
	"""
	After 3 seconds the get call will unblock after the setter
	sets a value on the AsyncResult
	"""
	print a.get()

def main():
	gevent.joinall([
		gevent.spawn(setter),
		gevent.spawn(waiter),
		gevent.spawn(waiter),
		gevent.spawn(waiter)
	])

if __name__ == '__main__': main()
