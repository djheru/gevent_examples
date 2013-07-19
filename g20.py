from gevent.pool import Pool

'''
Example of a socket server that polls a pool of sockets
'''

class SocketPool(object):
	def __init__(self):
		self.pool = Pool(1000)
		self.pool.start()
		
	def listen(self, socket):
		while True:
			socket.recv()
			
	def add_handler(self, socket):
		if self.pool.full():
			raise Exception('Maximum pool size reached')
		else:
			self.pool.spawn(self.listen, socket)
			
	def shutdown(self):
		self.pool.kill()
