import threading
from time import sleep
from delay import Delay

class Simulator:
	def __init__ (self, cv):
		"""
		Initiating the Simulator
		"""
		self.cv = cv

	def is_running (self):
		return self.cv.running

	def stop (self):
		self.cv.running = False

	def start_simulator(self, total, parallel, running):
		"""
		Start the simulator by setting running flag to True &
		by invoking run() method
		"""

		# print ("Inside Start. Total {} and a parallel {}".format(self.total, self.parallel))

		# if self.running:
		# 	print ("Similator is running already. Nothing to do.")
		# 	return

		# self.running = running()
		print ("Started")
		self.run(total, parallel, running)

		return

	# def stop(self, total, parallel, running):
	# 	"""
	# 	Stop the simulator by setting running flag to False
	# 	"""
	# 	if not self.running:
	# 		print ("Simulator is not running. Nothing to do.") 
	# 		return

	# 	self.running = False
	# 	print ("Stopped")

	# 	return

	def run(self, total, parallel, running):
		print ("Restarted..")
		i = 1
		started_threads = []

		"""
		Loop until all threads are submitted OR
		simulator is stopped explicitely
		"""
		print ("Inside run. Running Flag: {}. Total: {}".format(running(), total()))

		while running() and i <= total():

			print ("Target: {}. Current: {}.  Parallel: {}. Current: {}".format(total(), i, parallel(), len(started_threads)))

			# Wait for a chance before starting new thread
			self.wait_till_I_get_a_chance(started_threads, parallel)

			# print ("Wait over. Starting new thread")

			# Okay. Good to go. Start a new thread.
			d = Delay()
			t = threading.Thread(target=d.start_a_delay, args=(4,200,lambda : (not running())))
			t.daemon = True
			started_threads.append(t)
			t.start()

			# print ("Started new thread. Current running queue size: {}".format(len(started_threads)))

			# Counter goes up
			i+=1

		if running():
			print ("Submitted all {} jobs.".format(total()))

		print ("Let's wait till the submitted jobs to finish")

		"""
		Now simulator started all the jobs OR got interrupted by user
		If interrupted by the user, threads will be stopped anyway.
		Just wait for all threads to stop gracefully
		"""
		self.wait_till_threads_complete(started_threads)

		print ("All done.")

		self.cv.running = False
		print ("Current running status inside simulator: {}".format(self.is_running()))

		return

	def wait_till_I_get_a_chance(self, started_threads, parallel):
		"""
		Loops inifinitely till the number of theads running is less than
		expected parallel running count
		"""

		while True:
			# print ("Current queue size: {}".format(len(started_threads)))
			if len(started_threads) < parallel():
				# print ("Cool. Under the limit")
				# Okay. Now the parent program can start a new thread
				return
			else:
				# print ("Queue is full. Take a nap")
				sleep(0.25)
				started_threads=self.remove_finished_threads(started_threads)

	def remove_finished_threads(self, started_threads):
		"""
		Check each thread in the list for status 
		and remove those which are finished already
		"""
		for t in started_threads:
			if not t.is_alive():
				started_threads.remove(t)

		return started_threads

	def wait_till_threads_complete(self, started_threads):
		"""
		Wait till all the threads finish
		"""
		if len(started_threads) > 0:
			for t in started_threads:
				t.join()

# if __name__ == "__main__":
# 	s = Simulator()
# 	total = 50
# 	parallel = 3
# 	running = True

# 	t = threading.Thread (target=s.start_simulator, args=(lambda:total, lambda:parallel, lambda:running))
# 	t.start()

# 	print ("Started main thread. Goint to sleep for 2 seconds.")
# 	sleep(2)
# 	parallel = 5
# 	print ("Changed the parallel count to 5. Going to sleep for 5 seconds")
# 	sleep(5)
# 	total = 100
# 	parallel = 20
# 	print ("Changed the total tasks to 100 & parallel to 20. Going to sleep for 30 seconds")
# 	sleep(30)
# 	parallel = 5
# 	print ("Reducing parallel back to 5. Going to sleep for 60 seconds.")
# 	sleep(60)
# 	print ("Going to stop the simulator")
# 	running = False
# 	print ("Now waiting for the thread to finish.")
# 	t.join()
# 	print ("All done")

class ControlVariables():
	total_threads = 50
	parallel_threads = 5
	running = False
