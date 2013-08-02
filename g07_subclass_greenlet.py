import gevent
from gevent import Greenlet

'''
Subclass Greenlet and override the _run method
'''

class MyGreenlet(Greenlet):
	
	def __init__(self, message, n):
		Greenlet.__init__(self)
		self.message = message
		self.n = n
		
	def _run(self):
		print(self.message)
		gevent.sleep(self.n)

def main():			
	g = MyGreenlet('Hi There!', 3)
	g.start()
	g.join()


if __name__ == '__main__': main()
