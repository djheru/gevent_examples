import gevent

'''
Illustrates context switching via yielding
'''

def foo():
	print('running in foo')
	gevent.sleep(0)
	print('Explicit context switched back to foo again')
	
def bar():
	print('explicit context switched to bar')
	gevent.sleep(0)
	print('Implicit context switched back to bar')
	
def main():
	gevent.joinall([
		gevent.spawn(foo),
		gevent.spawn(bar)
	])

if __name__ == '__main__': main()
