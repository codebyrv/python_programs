# from base class to two derived class and then that two create another one class


class Student:
    def name(self):
        print("name...")
        
class Academic_Performance(Student):
    
    def acad_score(self):
        print("academic score is above 90%")
        
class ECA(Student):
    
    def ECA_score(self):
        
        print("eca score is... 50% above")
        
        
class Result(Academic_Performance,ECA):
    
    def Eligibility(self):
        
        print("Minimum Eligibility to apply")
        
        
        self.acad_score()
        self.ECA_score()
        
        
R=Result()        
R.Eligibility()        