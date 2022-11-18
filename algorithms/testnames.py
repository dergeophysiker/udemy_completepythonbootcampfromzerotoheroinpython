'''
class C1:
    def __init__(self, name):
        self.name = name
    def setname(self, name):
        self.name = name

C1.setname(C1, 'foo')
print(C1.name)

a = C1('bar')
b = C1('dog')

print(a.name)
print(b.name)
print(C1.name)
'''

'''
def foo():
    print(foo.i)
    foo.i += 1

foo.i = 0
foo()
foo()
foo()
foo.i = 1000
foo()
foo()
'''
class Foo:
    def __init__(self):
        self.i = 0
    def __call__(self):
        print(self.i)
        self.i += 1
foo = Foo()
foo()
foo()
foo()
foo.i = 1000
foo()