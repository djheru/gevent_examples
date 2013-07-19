import gevent

def win():
	return "you win!"

def fail():
	raise Exception("wee-woo")

def main():
	winner = gevent.spawn(win)
	loser = gevent.spawn(fail)
	
	print(winner.started)
	print(loser.started)
	
	# exceptions that are raised in vegas stay in vegas
	try:
		gevent.joinall([winner, loser])
	except Exception as e:
		print("I never get called")
	
	print(winner.value)
	print(loser.value)
	
	print(winner.ready())
	print(loser.ready())
	
	print(winner.successful())
	print(loser.successful())
	
	print(loser.exception)
	
	

if __name__ == '__main__': main()
