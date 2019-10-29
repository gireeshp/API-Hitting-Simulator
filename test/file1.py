from variables import VariableClass
from class1 import Worker

if __name__ == "__main__":

	v = VariableClass()
	print ("Inside file1.py. A: {}. F: {}".format(v.getA(), v.getF()))
	v.setA(2)
	v.setF(False)
	print ("Inside file1.py. A: {}. F: {}".format(v.getA(), v.getF()))

	worker = Worker()
	worker.start(v)
	print ("Inside file1.py. A: {}. F: {}".format(v.getA(), v.getF()))

	v.a = 10
	v.f = False
	print ("*Inside file1.py. A: {}. F: {}".format(v.getA(), v.getF()))