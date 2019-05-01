print("repeat")
def repeat(x):
    def subfx(y):
        print(x * y)
    return subfx

r1 = repeat("hello")
r1(2)
r2 = repeat("goodbye")
r2(2)
repeat("cool")(3)


print("make counter")
def make_counter():
    def subfx():
        #nonlocal x
        subfx.x += 1
        print(subfx.x)
    subfx.x = 0
    return subfx


ctr1 = make_counter()

ctr1()
ctr1()

ctr2 = make_counter()

ctr2()

ctr1()

ctr2()

print("accessor")

def accessor(x):
    print(x.x)

accessor(ctr1)
accessor(ctr2)
