lower = int(input ())  
upper = int(input ())  
  
#print ("The Prime Numbers in the range are: ")  
for number in range (lower, upper + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  