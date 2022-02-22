def func (num:int):
    for i in range(num):
        for seq in range(num,i,-1):
            print(seq-i ,end=' ')
        print()

func(5)