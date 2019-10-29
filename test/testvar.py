a = 10

def test1():
	global a
	print (a)
	a = 15
	print (a)

def test2():
	global a
	print (a)
	a = 25
	print (a)

if __name__ == "__main__":
	test1()
	test2()
	test1()
	test2()
