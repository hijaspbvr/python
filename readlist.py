list=input("Enter Numbers:")
colors=list.split(" ")
print(colors)
result=[]
for i in list:
    if i>100:
        result.append('over')
    else:
        result.append(i)
print(result)
