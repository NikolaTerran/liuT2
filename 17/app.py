def ls_function(list):
	#x = input("type input")
	result = [x for x in list if int(x) % 22 == 0]
	print(result)
	return 0

this_list = ['88','22','33','44','55','66','00']
list2 = [1,3,7,2,4,0,0,0,1,4,56,17,28,27,37,47]

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
	result = [y for y in range(num + 1) if num % y == 0]
	print(result)
	
ls_function(this_list)

function2(list2)
function3(list2)
function4()
function5()
function6(100)
