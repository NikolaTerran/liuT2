# [x for x in p if x in UC_LETTERS]
# 
print("This program can only run with python 3\n")

def ps_checker():
	passwd = input('type ur passwd\n')
	symbl = ['.','?','!','&','#',',',';',':','-','_','*']
	num_check = [x for x in passwd if x.isdigit()]
	cap_check = [x for x in passwd if x.isupper()]
	low_check = [x for x in passwd if x.islower()]
	symbl_check = [x for x in passwd if x in symbl]

	if not num_check:
		print('u need a number in ur passwd')
		exit()
	if not cap_check:
		print('u need a Cap letter in ur passwd')
		exit()
	if not low_check:
		print('u need a lower case letter in ur passwd')
		exit()
	if not symbl_check:
		print('u need a non-alphanumeric char in ur passwd')
		exit()
	if len(passwd) < 6:
		print("u passwd is weak bro!")
		exit()
	if len(passwd) < 12:
		print("u passwd is ok bro!")
		exit()
	if len(passwd) >= 12:
		print("u passwd is brolic bro!")
		exit()
	return 0

ps_checker()
