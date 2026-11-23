# #multiple inheritance

# class A(object):


#     def __init__(self):
        
#         print("class A")
        
        
                
# class B(object):
    
#     def __init__(self):
        
#         print("class B")
        
        
# class Derived(A,B):
    
#     pass

# D=Derived()
    
    











     
        
        
        
        
        
        
        
        
        

class A(object):


    def __init__(self):
        
        print("class A")
        super(A,self).__init__()
        
        
                
class B(object):
    
    def __init__(self):
        
        print("class B")
        
        
class Derived(A,B):
    
    pass

D=Derived()        