a,b,c = map(int, input().split())


count=1
while 1:

    if (count%a)==0 and (count%b)==0 and (count%c)==0 :
        break
    
    count+=1

print(count)