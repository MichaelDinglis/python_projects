arr=[]
l=0
a=int(input("Type amount of rows:  "))
b=int(input("Enter amount of columns"))

for i in range(0,a):
    arr.append([])

for i in range(0,a):
    for k in range(0,b):
        arr[i].append(k+l)
    l+=k

arr=np.array(arr)      
print(arr)
