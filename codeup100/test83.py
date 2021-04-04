#틀림!

R,G,B=map(int,input().split())
d=0

for r in range(R):
    for g in range(G):
        for b in range(B):
            print(r,g,b)
            d+=1



print(d)