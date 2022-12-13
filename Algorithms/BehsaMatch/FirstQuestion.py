import pandas

print("hi")

woods={"1":2,"2":3,"3":2,"4":3,"5":2,"6":1}
print(woods)

wood_radios=woods.keys()
wood_radios=sorted(wood_radios)
number_of_each_wood=woods.values()

result=[]
result.append(max(number_of_each_wood))
while len(wood_radios)>0:
    for item in wood_radios:
        result.append(item)
        woods[item]-=1
    wood_radios=[]
    for key,value in woods.items():
        if value!=0:
            wood_radios.append(key)

print(result)






