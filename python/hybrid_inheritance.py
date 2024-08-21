class A:
    def add(self,x,y):
        self.x=x
        self.y=y
    print("the add is ",self.x+self.y)
class B(A):
    def sub(self,x,y):
        self.x=x
        self.y=y
    print("the sub is ",self.x-self.y)
class C(B):
    def mul(self,x,y):
        self.x=x
        self.y=y
    print("the mul is ",self.x*self.y)
class D(C):
    def div(self,x,y):
        self.x=x
        self.y=y
    print("the mul is ",self.x/self.y)
a=int(input("en1"))
b=int(input("en2"))
ab=D()
ob.sub(a,b)
ob.add(a,b)
ob.mul(a,b)