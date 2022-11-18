from os import system
def hello(name='jose'):
    print("the hello func has been executed")

    def greet():
        return "\t this is the greet function in hello"
    
    def welcome():
        return "\t this is the welcome inside hello"

    '''
    print(greet())
    print(welcome())
    print("this is the end of hello")
    '''
    print("returning a function")
    if name == 'jose':
        return greet
    else:
        return welcome



#########################################################################

#hello()
#test=hello
#test()
#del hello
#hello()  # 
#test() # this still runs but hello wont
#########################################################################
my_new_func = hello('jose')
my_new_func
s=my_new_func()
print(type(s))
print(repr(s))

#########################################################################

def cool():
    def super_cool():
        return "I am very cool"
    return super_cool

somefunc=cool()
somefunc
somefunc()
print(somefunc())
#########################################################################

def hello1():
    return 'hi jose!'

def other(some_def_func):
    print("other code runs here")
    print(some_def_func())

other(hello1)
#########################################################################
system('cls')
#system('clear')
def new_decorator(originalfunc):
    
    def wrap_func():

        print("some extra code before the oroginal function")
        originalfunc()
        print("some extra code after original function")

    return wrap_func
#########################################################################

#def func_needs_decorator():
#    print("i want to be decoreted")

#func_needs_decorator()
#decorated_func = new_decorator(func_needs_decorator)
#decorated_func()
#########################################################################
@new_decorator
def func_needs_decorator():
    print("i want to be decoreted")
func_needs_decorator()
