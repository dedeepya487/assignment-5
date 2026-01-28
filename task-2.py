list=[1,2,3,4,5,6,7,8,9,10]
print(f"origu=inal list:{list}")
l1=[]
for i in range(5):
    l1.append(list[i])
print(f"first 5 elements:{l1}")
l1.sort(reverse=True)
print(f"reversed list: {l1}")