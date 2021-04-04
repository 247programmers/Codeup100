dlist=[]

for i in range(10):
    dlist.append([])
    for j in range(10):

        dlist[i].append(0)


for i in range(10):

    darr1=input().split()
    for j in range(10):
        dlist[i][j]=int(darr1[j])
       

nowx=1
nowy=1

dlist[nowx][nowy]=9
while 1:
    if dlist[nowx][nowy+1]==0 or dlist[nowx][nowy+1]==2 :

        if dlist[nowx][nowy+1]==2:
            dlist[nowx][nowy+1]=9
            break
        elif dlist[nowx][nowy+1]==0:
            dlist[nowx][nowy+1]=9

        nowy+=1
        

    elif dlist[nowx+1][nowy]==0 or dlist[nowx+1][nowy]==2:

        if dlist[nowx+1][nowy]==2:
            dlist[nowx+1][nowy]=9
            break

        elif dlist[nowx+1][nowy]==0:
            dlist[nowx+1][nowy]=9

        nowx+=1

    else :
        break

        


for i in range(10):
    for j in range(10):
        print(dlist[i][j],end=' ')

    print()