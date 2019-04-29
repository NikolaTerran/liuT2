import random
import re
import operator

#my_randoms = random.sample(xrange(100), 10)
print("please run this with python3")

moby = []

with open("mobydick.txt") as f:
	content = f.readlines()
	word = re.split('; |, |\n|\s|. |: ',''.join(content))
	moby.extend(word)


moby = [x for x in moby if x is not ""]
#print(len(moby))


def word_freq(n):
	filter = [x for x in moby if n.lower() in x or n.upper() in x or n in x]
	#print(filter)
	print("Word " + n + " appeared in Moby Dick", len(filter), "times.")


def group_freq(n):
	list = n.split(" ")
	filter = [x for x in moby for y in list if y.lower() in x or y.upper() in x]
	print("Words " ,n, " appeared in Moby Dick", len(filter), "times.")

def most_freq():
	word = {}
	for x in moby:
		x = x.lower()
		if x not in word:
			word[x] = 1
		else:
			word[x] += 1
	print("The most frequent word in moby dick is:" + max(word.items(), key=operator.itemgetter(1))[0])
	return 0
#group = ['ahab','whale']

word = input("enter a word:")
word_freq(word)
group = input("enter a group of words separated by space:")
print(group)
group_freq(group)
#word_freq("whale")
#group_freq(group)
most_freq()
'''
def q_sort(n):
	ran_list = random.sample(range(n),n)
	print(ran_list)
	result = [y for x in ran_list for y in ran_list]
	print(result)
'''

'''
def p_triple(n):
	result = [(x,y,z) for x in range(1,n)
		    for y in range(x,n)
		    for z in range(y,n)
		    if x * x + y * y == z * z]
	print(result)

p_triple(20)

a = [1,2,3]
b = [2,3,4]

def union(a,b):
	result = [x for x in a] + [x for x in b if x not in a]
	print(result)

union(a,b)

def intersect(a,b):
	result = [x for x in a if x in b]
	print(result)

intersect(a,b)

def set_diff(u,a):
	result = [x for x in u if x not in a]
	print(result)

set_diff(a,b)

def sym_diff(u,a):
	result = [x for x in u if x not in a] + [x for x in a if x not in u]
	print(result)

sym_diff(a,b)

c = ["red","green","blue"]

def cart_pdt(a,b):
	result = [(x,y)for x in a
			for y in b]
	print(result)

cart_pdt(a,c)

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
'''
