# Create a function that takes 1 parameter of type int 
# , then it prints out the result formatted like the 
# following patter (if we give it 5 for example):




def function(num:int):
    for i in range(num):
        for n in range(num,i,-1):
            print(n-i,end=' ')
        print()


function(9)



