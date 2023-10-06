class parent():
    def add1(self,a,b):
        self.a=a
        self.b=b
class child(parent):
    def add(self):
        print("sum=",self.a+self.b) 
x=int(input("enter the number"))
y=int(input("enter the number"))                
obj=child()
obj.add1(x,y)
obj.add()       