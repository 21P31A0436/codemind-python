def isHappyNumber(n):    
    digit = sum = 0    
    while(n > 0):    
        digit = n % 10 
        sum = sum + (digit * digit)    
        n = n // 10   
    return sum    
        
n = int(input())    
result = n   
     
while(result != 1 and result != 4):    
    result = isHappyNumber(result)   
     
if(result == 1):    
    print(True)   
else:    
    print(False)