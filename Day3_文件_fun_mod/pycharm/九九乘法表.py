# -*-coding:utf-8-*-
for a in range(1, 10):
    for b in range(1, a+1):
        # print('%dx%d=%d'%(b,a,b*a),end=" ")
        print("{0}x{1}={2}".format(b, a, b*a), end=" ")
    print()

# 格式化的两种方法  %d %s
#                foramat()
