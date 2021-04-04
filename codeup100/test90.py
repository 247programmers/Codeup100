a,m,d ,n =map(int, input().split())


init=a
for i in range (n-1):
    init= init*m +d


print(init)