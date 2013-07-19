import gevent
from gevent.local import local

'''
Gevent also allows you to specify data which is local to the greenlet context. 
Internally, this is implemented as a global lookup which addresses a private 
namespace keyed by the greenlet's getcurrent() value.
'''
stash = local()
stash.globalstash = 0

def f1():
	stash.f1 = 1
	print(stash.f1, stash.__dict__)
	
def f2():
	stash.f2 = 2
	print(stash.f2, stash.__dict__)
	
	try:
		stash.f1
	except AttributeError as e:
		print('f1 is not local to f2: {0} ({1})'.format(e, stash.__dict__))
	
def main():
	gevent.joinall([
		gevent.spawn(f1),
		gevent.spawn(f2)
	])
	
	print(stash.__dict__)

if __name__ == '__main__': main()
