from flask import Flask

app = Flask(__name__)

a = []

@app.route ("/test1", methods=['GET'])
def test1():
	global a
	print (a)
	a.append(1)
	print (a)
	return "Ok", 200

@app.route ("/test2", methods=['GET'])
def test2():
	global a
	print (a)
	a.append(2)
	print (a)
	return "Ok", 200