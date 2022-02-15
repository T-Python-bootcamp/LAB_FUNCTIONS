

def number_format(num):

    # First solution
    result = ""
    for num in range(num, 0, -1):
        for n in range(num, 0, -1):
            result += f"{n} "
        print(result)
        result = ""

    # Second solution
    # lest = list(range(1, num+1))
    # ....

    # Third solution
    # outer = num
    # while(outer > 0):
    #     inner = outer
    #     rowResult = ''
    #     while(inner > 0):
    #         rowResult += "{} ".format(str(inner))
    #         inner -= 1
    #     print(rowResult)
    #     outer -= 1


number_format(5)
