
def numbers(num: int):
    res = ""
    for n in range(num,0,-1):
        for x in range(n,0,-1):
            res += f"{x} "
        print(res)
        res=""
    
numbers(5)