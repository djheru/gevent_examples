import gevent
from gevent import Greenlet
from gevent.queue import Queue


	

class Actor(gevent.Greenlet):
	
	def __init__(self):
		self.inbox = Queue()
		Greenlet.__init__(self)
	
	def receive(self, msg):
		'''
		Define in your subclass
		'''
		raise NotImplemented
	
	def _run(self):
		self.running = True
		while self.running:
			msg = self.inbox.get()
			self.receive(msg)

# sample implementation			
class Pinger(Actor):
	def receive(self, msg):
		print(msg)
		pong.inbox.put('ping')
		gevent.sleep(1)
		
ping = Pinger()

class Ponger(Actor):
	def receive(self, msg):
		print(msg)
		ping.inbox.put('pong')
		gevent.sleep(1)
		
pong = Ponger()
	
def main():
	
	ping.start()
	pong.start()
	
	ping.inbox.put('start')
	gevent.joinall([ping, pong])

if __name__ == '__main__': main()
