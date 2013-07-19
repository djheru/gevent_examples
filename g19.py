import gevent
from gevent.pool import Pool

pool = Pool(2)

def hello_from(n):
	print("Size: {0}".format(len(pool)))

pool.map(hello_from, xrange(3))
