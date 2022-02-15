def less(num):
    
    for nums in reversed(range(num+1)):
        
        for number in reversed(range(1, nums+1)):
            print(number, end=" ")
            
            
        print("\r")
        
print(less(5))