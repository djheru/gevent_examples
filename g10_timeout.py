import gevent
from gevent import Timeout

'''
Illustrates gevent timeout stuff
'''

seconds = 10
time_to_wait = 5

timeout = Timeout(seconds)
timeout.start()

def wait():
	gevent.sleep(10)
	
class TooLong(Exception): pass


def main():
	try:
		gevent.spawn(wait).join()
	except Timeout:
		print("Timeout")
		
	with Timeout(time_to_wait, TooLong):
		gevent.sleep(10)

if __name__ == '__main__': main()
