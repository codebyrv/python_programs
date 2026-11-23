class A(object):
    def __init__(self):
        
        print("class A")
        super(A,self).__init__()               
class B(object):
    
    def __init__(self):
        
        print("class B")
              
class Derived(A,B):
    def __init__(self):
        super(Derived,self).__init__()
        
        print("derived class")
        
D=Derived()        