import time, gevent
from gevent import select

'''
Illustrates how gevent implicitly yields blocking operations inside greenlets
'''

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)

def gr1():
	# busy wait for one second, but we don't want to wait...
	print('Started Polling: ', tic())
	select.select([], [], [], 2)
	print('Ended polling: ', tic())
	
def gr2():	
	# busy wait for one second, but we don't want to wait...
	print('Started Polling: ', tic())
	select.select([], [], [], 2)
	print('Ended polling: ', tic())
	
def gr3():
	print('doing some stuff while the greenlets poll, at: ', tic())
	gevent.sleep(1)
	
def main():
	gevent.joinall([
		gevent.spawn(gr1),
		gevent.spawn(gr2),
		gevent.spawn(gr3)
	])

if __name__ == '__main__': main()
