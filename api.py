from flask import Flask, request, Response
from simulator import Simulator, ControlVariables
import threading
import json

app = Flask(__name__)

cv = ControlVariables()
s = Simulator(cv)

@app.route("/")
def load_template():
	return app.send_static_file("index.html")

@app.route("/status", methods=['GET'])
def status():
	responseJson = {"message": "Simulator is "+("" if cv.running else "not")+" running.",
					"total_threads": cv.total_threads,
					"parallel_threads": cv.parallel_threads,
					"running": cv.running,
					"current_counter": cv.current_counter,
					"current_parallel": cv.current_parallel,
					"url": cv.url,
					"json": cv.json,
					"headers": cv.headers
					}
	# print (responseJson)

	return Response(json.dumps(responseJson), mimetype="application/json")

@app.route("/start", methods=['GET'])
def start():
	# global total_threads, parallel_threads, running

	# print ("Input received. Total: {}. Parallel: {}".format(total_threads, parallel_threads))
	# print ("Current status: {}".format(cv.running))

	if cv.running:
		print ("Simulator is already running.")
		return Response(json.dumps({"message": "Simulator is already running."}), mimetype="application/json")

	# Get the parameters from user. If not given, default them
	total = request.args.get("total", 50)
	parallel = request.args.get("parallel", 5)
	url = request.args.get("url", "")
	json_s = request.args.get("json", "")
	header_s = request.args.get("headers", "")
	headers = None

	try:
		headers = json.loads(header_s)
		print (headers)
	except:
		pass
	
	# Assign to global variables
	cv.total_threads = int(total)
	cv.parallel_threads = int(parallel)
	cv.url = url
	cv.json = json_s
	cv.headers = headers
	cv.running = True

	print ("URL: {}".format(url))
	print ("Json: {}".format(json))
	print ("Headers: {}".format(headers))
	print ("total: {}. parallel: {}. running: {}".format(cv.total_threads, cv.parallel_threads, cv.running))

	# Start new simulator thread
	t = threading.Thread (target=s.start_simulator, args=(lambda:cv.total_threads, lambda:cv.parallel_threads, lambda:cv.running, url, json, headers))
	t.start()
	return Response(json.dumps({"message": "Started the simulator"}), mimetype="application/json")
	# return "Started the simulator", 200

@app.route("/modify", methods=['GET'])
def modify():
	# global total_threads, parallel_threads, running

	if not cv.running:
		print ("Simulator is not running. Please start it using /start.")
		return Response(json.dumps({"message": "Simulator is not running. Please start it using /start."}), mimetype="application/json")

	# Get the parameters from user. If not given, default them
	total = request.args.get("total", 50)
	parallel = request.args.get("parallel", 5)

	print ("Input received. Total: {}. Parallel: {}".format(total, parallel))

	# Assign to global variables
	cv.total_threads = int(total)
	cv.parallel_threads = int(parallel)

	print ("total: {}. parallel: {}. running: {}".format(cv.total_threads, cv.parallel_threads, cv.running))

	# Simulator will automatically take the modified parameters

	return Response(json.dumps({"message": "Modified the parallel counter"}), mimetype="application/json")

@app.route("/stop", methods=['GET'])
def stop():
	# global total_threads, parallel_threads, running

	if not cv.running:
		print ("Simulator is not running. Please start it using /start.")
		return Response(json.dumps({"message": "Simulator is not running. Please start it using /start."}), mimetype="application/json")

	print ("Stopping..")

	cv.running = False

	print ("total: {}. parallel: {}. running: {}".format(cv.total_threads, cv.parallel_threads, cv.running))

	s.stop() 

	return Response(json.dumps({"message": "Stopped the simulator"}), mimetype="application/json")
