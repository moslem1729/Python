n=int(input())

a=5
b=0
c=0
for i in range(n):
    op=input()
    if op=="2":
        c-=1
        b+=1
    else:
        b+=1

print(str(a)+" "+str(b)+" "+str(c))

