import time

def echo(i):
	time.sleep(0.01)
	return i

def main():
	
	# non deterministic process pool
	from multiprocessing.pool import Pool	
	p = Pool(10)	
	run1 = [a for a in p.imap_unordered(echo, xrange(10))]
	run2 = [a for a in p.imap_unordered(echo, xrange(10))]
	run3 = [a for a in p.imap_unordered(echo, xrange(10))]
	run4 = [a for a in p.imap_unordered(echo, xrange(10))]	
	print(run1, run2, run3, run4)	
	print(run1 == run2 == run3 == run4)
	
	
	# deterministic gevent pool
	from gevent.pool import Pool	
	p = Pool(10)	
	run1 = [a for a in p.imap_unordered(echo, xrange(10))]
	run2 = [a for a in p.imap_unordered(echo, xrange(10))]
	run3 = [a for a in p.imap_unordered(echo, xrange(10))]
	run4 = [a for a in p.imap_unordered(echo, xrange(10))]		
	print(run1, run2, run3, run4)	
	print(run1 == run2 == run3 == run4)

if __name__ == '__main__': main()
