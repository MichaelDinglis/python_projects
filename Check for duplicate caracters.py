print("Enter a string that its length is multiple of the number 3")
s=str(input())
a=int((len(s))/3)
list=[]
i=0

for f in range (a):
    d=list.append(s[i:i+3])
    i+=3

i=0

for v in range(a):
    g=str(list[i])
    p = g[0]
    h = g[1]
    k = g[2]
    if p==h or p==k or h==k:
        print("There are duplicates on char. set no.",i+1)
    else:
        print("There NO are duplicates on char. set no.",i+1)
    i+=1