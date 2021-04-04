N=int(input())


Sum=0

for i in range(N):
    Sum=Sum+i
    if Sum >= N:
        print(i)
        break