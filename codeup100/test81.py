n=ord(input())
n=n-55

for i in range(15):



    print('%X'%n, '*%X'%(i+1), '=%X'%(n*(i+1)), sep='')