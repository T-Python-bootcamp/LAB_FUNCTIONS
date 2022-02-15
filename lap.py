

def number_format(num):
    num_range = range(1, num+1)
    while num:
        # global num_range
        for n in num_range:
            if(n <= num):
                print(n)
            else:
                num = num - 1
                break


number_format(5)
