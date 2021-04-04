    #개수를 입력받아 n에 정수로 저장
 #공백을 기준으로 잘라 a에 순서대로 저장

d=[]

for i in range(19):
    d.append([])

    for j in range(19):
        d[i].append(0)


for i in range(19):


    d[i][0],d[i][1],d[i][2],d[i][3],d[i][4],d[i][5],d[i][6],d[i][7],d[i][8],d[i][9],d[i][10],d[i][11],d[i][12],d[i][13],d[i][14],d[i][15],d[i][16],d[i][17],d[i][18]=map(int,input().split())



n = int(input())  

for i in range(n):

    row, col = map(int,input().split())
    for j in range(19):
        if d[row-1][j]==1:
            d[row-1][j]=0
        else :
            d[row-1][j]=1

    for p in range(19):
        if d[p][col-1]==1:
            d[p][col-1]=0
        else :
            d[p][col-1]=1


for i in range(19):
    for j in range(19):

        print(d[i][j],end=' ')
    print()
        

  

