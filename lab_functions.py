def func(num:int):
    List = list(range(1,num+1))
    List.reverse()
    while List:
        items = ""
        for item in List:
            items += f"{item} "
        print(items)
        List.pop(0)

func(5)