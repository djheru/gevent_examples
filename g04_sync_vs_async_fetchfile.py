import gevent.monkey
gevent.monkey.patch_socket()

'''
Illustrates synchronous vs asynchronous fetching of a remote file via urllib2
'''

import gevent, urllib2, simplejson as json

def fetch(pid):
	response = urllib2.urlopen('http://json-time.appspot.com/time.json')
	result = response.read()
	json_result = json.loads(result)
	datetime = json_result['datetime']
	
	print('Process: ', pid, datetime)
	return json_result['datetime']

def synchronous():
	for i in range(1, 10):
		fetch(i)
		
def asynchronous():
	threads = []
	for i in range(1, 10):
		threads.append(gevent.spawn(fetch, i))
	gevent.joinall(threads)
	
def main():
	print('Synchronous: ')
	synchronous()
	
	print('Asynchronous: ')
	asynchronous()

if __name__ == '__main__': main()
