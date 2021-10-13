l=[9,6,1,4,5,8]
for i in range(len(l)-1):
    min_value=min(l[i:])
    min_index=l.index(min_value)
    l[i],l[min_index]=l[min_index],l[i]
    print(l)
