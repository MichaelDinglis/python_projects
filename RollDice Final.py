from random import randint as rd

r=rd(1,7)+rd(1,7)
craps=[7,11]
crLost=[3,2,12]
crnew=[1,4,5,6,8,9,10]
i=0
l=i

pls=[["Michael",False],["Mumteha",False],["Akay",False],["George",False]]
j=len(pls)
h=j+1
print()
e=[]

while(True):
    try:
        l = i + 1
        if r ==craps:
            if l<=j:
                print("The dice was",r)
                global z
                z="Winner is player",i+1
                print(z)
                break
            elif l==h:
                print("No winner")
                break

        elif r in crLost:
            if l<=j:
                print("The dice was",r)
                print("Player",i+1,"Lost")
                pls[i][1]=True
                i+=1
                print(pls)
            elif l == h:
                print("Everyone Lost")
                break

        elif r in crnew:
            craps=r
            print(r, "Is the new winner")
            crnew.clear()
        r = rd(1, 7) + rd(1, 7)


    except IndexError:
        print("No winner")
        break










