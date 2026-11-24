#     class One:
    
#     def set(self,var):
        
#         self.var=var
        
        
#     def get(self):
        
#         return self.var
        
        
# class Two:
    
#     def __init__(self,var):
        
#         self.o=One()
#         self.o.set(var)
        
#     def show(self):
        
#         print("Number=",self.o.get())
        
# T=Two(100)

# T.show()



# class Student:
#     def name(self):
#         print("name...")
        
# class Academic_Performance(Student):
    
#     def acad_score(self):
#         print("academic score is above 90%")
        
# class ECA(Student):
    
#     def ECA_score(self):
        
#         print("eca score is... 50% above")
        
        
# class Result(Academic_Performance,ECA):
    
#     def Eligibility(self):
        
#         print("Minimum Eligibility to apply")
        
        
#         self.acad_score()
#         self.ECA_score()
        
        
# R=Result()        
# R.Eligibility()        