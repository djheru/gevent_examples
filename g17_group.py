import gevent
from gevent.pool import Group

'''
Illustrates the basic usage of Group
'''

def talk(msg):
	for i in xrange(3):
		print(msg)
		
def main():
	g1 = gevent.spawn(talk, 'foo')
	g2 = gevent.spawn(talk, 'bar')
	g3 = gevent.spawn(talk, 'baz')
	
	group = Group()
	group.add(g1)
	group.add(g1)
	group.join()	
	
	group.add(g1)
	group.join()

if __name__ == '__main__': main()
