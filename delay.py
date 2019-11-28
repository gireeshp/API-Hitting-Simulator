# from simulator import Simulator, ControlVariables
from random import randint
import datetime
import threading
from time import sleep
import requests
import json

class Delay:

	def __init__ (self, cv):
		self.cv = cv

	def hit_a_url (self, url, json, headers):
		r = requests.post (url=url, json=json, headers=headers)
		self.cv.output = r.json()

	def start_a_delay (self, num_of_digits, how_many_times, stop):

		worst_case = 10000000
		i = 0
		mul = 10**num_of_digits
		match_count = 0
		# print ("Looking for {} matches of multiples of {} ".format(how_many_times, mul))

		start_time = datetime.datetime.now()

		while not stop():
			i+=1
			r = randint(10000, 99999)
			if r%mul == 0:
				match_count+=1
			
			if (match_count >= how_many_times):
				diff = self.get_the_time_difference(start_time)
				# print ("Got {} matches in {} seconds. Stopping. Bye.".format(how_many_times, diff))
				break

			if i >= worst_case:
				diff = self.get_the_time_difference(start_time)
				# print ("Tried {} times in {} seconds without enough matches. Got only {} matches. Was looking for {}. I quit.".format(worst_case, diff, match_count, how_many_times))
				break
		
		if (stop()):
			print ("Ooops. Somebody stopped me.")


	def get_the_time_difference (self,start_time):
		end_time = datetime.datetime.now()
		delta = end_time - start_time
		return delta.total_seconds()

if __name__ == "__main__":

	json_s = '{"name": "Gireesh", "col2": "val2"}'
	print (json_s)
	print (type(json_s))

	json_d = json.loads(json_s)
	print (json_d)
	print (type(json))

	url = "http://127.0.0.1:8081/delay"

	r = requests.post (url=url, json=None, headers=None)
	print (r.json())

	"""
	# slow_down(4, 500)
	d = delay();
	stop = False

	t = threading.Thread(target=d.start_a_delay, args=(4,500,lambda : stop,))
	t.daemon = True
	t.start()
	print ("Started the thread")

	sleep(2)
	print ("Woke up after 2 seconds. Stopping")
	stop = True
	print ("Stopped..")
	print (t.is_alive())
	t.join()
	print (t.is_alive())
	"""
