h,w = map(int, input().split())
darr=[]
for i in range(h):
    darr.append([])
    for j in range(w):
        darr[i].append(0)

n= int(input())
for i in range(n):

    l,d,x,y= map(int, input().split())
    for j in range(l):
        if d==0:
            darr[x-1][y-1+j]=1


        else :
            darr[x-1+j][y-1]=1


for i in range(h):
    for j in range(w):

        print(darr[i][j], end=' ')

    print()



