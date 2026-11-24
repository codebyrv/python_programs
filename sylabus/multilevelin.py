class A:
    
    def __init__(self):
        print("A's Constructer")
        
    def displayA(A):
        
        print("class A")
        

class B(A):
    
    def __init__(self):
        print("B's Constructer")
    
    def displayB(B):
    
        print("class B")
    
    
class C(B):
    
    def __init__(self):
        
        print("B's Constructer")
        
    def displayC(C):
    
        print("C's Constructer")
    
    
c1=C

c1.displayA()
c1.displayB()
c1.displayC()


    
    
    
    
    
    
    