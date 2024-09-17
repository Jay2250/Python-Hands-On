class calculator:
    def add(self,*args):
         print(sum(args))

c1 = calculator()
c1.add(20,60)

class calculator1:
    def add1(*args):
         print(sum(args))

calculator1.add1(20,30)