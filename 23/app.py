import random

def make_HTML_heading(f):
    def inner():
        return '<h1>' + f() + '</h1>'
    return inner

@make_HTML_heading
def greet():
    greetings = ['Hello','Welcome','AYO','Hola','Bonjour','Word up']
    return random.choice(greetings)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
#reet_heading = make_HTML_heading(greet)
def memoize(f):
    memo = {}
    def helper(x):
        fib()
    return helper

print(greet())
print(greet())
print(fib(10))

fib = memoize(fib)
print(fib(40))
#print(greet_heading())
