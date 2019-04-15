import random
#my_randoms = random.sample(xrange(100), 10)

def q_sort(n):
	ran_list = random.sample(range(n),n)
	print(ran_list)
	result = [y for x in ran_list for y in ran_list]
	print(result)

q_sort(20)

def p_triple(n):
	x = range(1,n)
	y = range(1,n)
	z = range(1,n)
	x2 = [x1 for x1 in x 
		 for y1 in y 
		 for z1 in z 
		 if x1 * x1 + y1 * y1 == z1 * z1]
	y2 =  [y1 for x1 in x 
	          for y1 in y  
	          for z1 in z 
	          if x1 * x1 + y1 * y1 == z1 * z1]
	z2 = [z1 for x1 in x
	         for y1 in y  
                 for z1 in z 
		 if x1 * x1 + y1 * y1 == z1 * z1]
	#result = [a for a in range(1,n)
	#	    for b in range(a,n)
	#	    for c in range(b,n)
	#	    if a * a + b * b == c * c]                                                                                         

	print(x2)
	print(y2)
	print(z2)
	#print(result)
	
#p_triple(100)


def ls_function(list):
	#x = input("type input")
	result = [x for x in list if int(x) % 22 == 0]
	print(result)
	return 0

def function2(list):
	result = [x for x in list if x % 10 == 7]
	print(result)
	return 0

def function3(list):
	result = [x for x in list if x == 1 or x == 0 or x == 2 or x == 4]
	print(result)
	return 0

def function4():
	result = range(101)
	result = [x for x in result if x != 2 or x != 3 or x != 1 or x != 5 or x != 7 or  x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0]
	print(result)
	return 0

def function5():
	result = range(101)
	result = [x for x in result if ((x % 2 != 0 and x % 3 != 0) and (x % 5 != 0 and x % 7 != 0)) or x == 2 or x == 3 or x == 5 or x == 7]
	result = [x for x in result if x != 1]
	print(result)
	return 0

def function6(num):
	result = [y for y in range(num + 1) if y != 0 and num % y == 0]
	print(result)

