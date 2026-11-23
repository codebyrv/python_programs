lower=int(input("enter the lower limit:\n"))
upper=int(input("enter the upper limit:\n"))


for num in range(lower,upper+1):
    
    if num>1:
        
        for i in range(2,num+1):
            if num%i==0:
                
                break
            
        else:
                
                print(num)
                