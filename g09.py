import gevent
import signal

def run_forever():
	print("I'm busy, come back later!")
	gevent.sleep(1000)
	
def main():
	gevent.signal(signal.SIGQUIT, gevent.shutdown)
	thread = gevent.spawn(run_forever)
	thread.join()

if __name__ == '__main__': main()
