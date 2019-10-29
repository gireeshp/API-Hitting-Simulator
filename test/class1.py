from variables import VariableClass

class Worker:
	def start (self, v):
		self.v = v
		print ("Inside worker. A: {}. F: {}".format(v.getA(), v.getF()))
		self.v.setA(3)
		self.v.setF(True)
		print ("Inside worker. A: {}. F: {}".format(v.getA(), v.getF()))