def solve(numheads, numlegs):
    for i in (range(numheads+1)):
        j = numheads - i
        if i*2 + j*4 == numlegs:
            return '鸡%d只,兔%d只' % (i, j)
    return '没有解决方案'


print(solve(2, 6))
