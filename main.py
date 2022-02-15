
def shapeMaker(params):
    outer=params
    while(outer>0):
        inner=outer
        rowResult=''
        while(inner>0):
            rowResult+="{} ".format(str(inner))
            inner-=1
        print(rowResult)
        outer-=1
shapeMaker(5)