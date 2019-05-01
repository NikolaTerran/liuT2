def make_counter():
    x = 0
    def subfx():
        nonlocal x
        x += 1
        print(x)
    return subfx

ctr1 = make_counter()

ctr1()
ctr1()

ctr2 = make_counter()

ctr2()

ctr1()

ctr2()
    
