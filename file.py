def myFun (num:int):
    for i in range(num + 1, 0, -1):    
        for j in range(0, i - 1):  
            print( (i-1) - j, end=" ")       
        print()
        
myFun(5)