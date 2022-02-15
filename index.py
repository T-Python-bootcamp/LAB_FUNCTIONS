def format(num):
    for x in reversed(range(1,num+1)):
        print (x,end='')
    print()
    if num>1:
        format(num-1)
format(5)