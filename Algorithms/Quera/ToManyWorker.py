workers={}
count=int(input())
for i in range(count):
    name_and_family=input()
    name,family=name_and_family.split()
    if name in workers:
        workers[name]+=1
    else:
        workers[name]=1
max=0
for value in workers.values():
    if value>max:
        max=value
print(max)
