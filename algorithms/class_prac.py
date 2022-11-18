###############################
class C1:
    def setname(self,who):
        self.name=who
###############################    
C1.setname(C1,"joseph")
C1.random="est"

L1=C1()
print(L1.name)  # => prints joseph
print(L1.random)
L2=C1()
print(L2.name)  # => prints joseph
###############################
