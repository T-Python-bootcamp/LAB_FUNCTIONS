def desc(num:int):
    answer = ""
    for n in range(num, 0, -1):
        for x in range(n, 0 ,-1):
            answer += f"{x} "
        print(answer)
        answer = ""
desc(5)