# def my_function (number:int):
#     num = 6
#     for  mynumber in range(number,0,-1):
#         for  i in range (mynumber,0,-1):
#            num += f"{i}" 
#            print(num("num"))
#            num
# my_function(5)
# rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
# for i in range(rows):
#     # nested loop
#     for j in range(i):
#         # display number
#         print(i, end=' ')
#     # new line after each row
#     print('')

# rows = 8
# num = rows
# # reverse for loop
# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print(num, end=' ')
#     print("\r")


# def myFunction(n:int):
   
#     for i in range( 0, -1):
#      for j in range(0, i):
#          print(j)      
 
#     myFunction(4)



# final solve

def my_number(num:int):
    res =""
    for nember in range(num, 0, -1):
        for i in range(nember, 0 ,-1):   
            res += f"{i} "
        print(res)
        res= "" 
my_number (9)  