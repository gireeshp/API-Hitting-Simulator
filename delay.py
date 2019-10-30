from random import randint
import datetime
import threading
from time import sleep

class Delay:

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
				diff = self.get_the_time_difference(start_time)
				match_count+=1
				# print ("Got match {} in attempt {} ({} seconds). Random number was: {}".format(match_count, i, diff, r))
			
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

	flag = False
	print (not flag)

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
