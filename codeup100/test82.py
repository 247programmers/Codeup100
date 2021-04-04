N=int(input())

for i in range(N):
    if ((i+1)%10==3) or ((i+1)%10==6) or ((i+1)%10==9) :
        print('X',end=' ')
   
    else :
        print(i+1,end=' ')