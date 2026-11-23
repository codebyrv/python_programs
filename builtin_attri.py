# dict,doc,name,bases


class A():
    '''This is a class A'''
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def display(self):
        
        print("x=",self.x)
        print("y=",self.y)
        
o1=A(10,20)

o1.display()            


print("object.__dict__ -",o1.__dict__)        
print("object.__doc -",o1.__doc__)        
print("class.__name__ -",A.__name__)        
print("object.__module__ -",o1.__module__)        
print("class.__bases__ -",A.__bases__)        