inp=list(map(str,input().split()))
inp2=input()
new=[]
for i in inp:
    if(i.startswith(inp2)):
        new.append(i)
print(new)



    
