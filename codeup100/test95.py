n = int(input())      #개수를 입력받아 n에 정수로 저장
 #공백을 기준으로 잘라 a에 순서대로 저장


list1=[]


for i in range(20):
    list1.append([])
    for j in range(20):
        list1[i].append(0)


for i in range(n):

    row,col = map(int,input().split())
    list1[row-1][col-1]=1





for i in range(19):
    for j in range (19):
        print(list1[i][j],end=" ")

    print('')