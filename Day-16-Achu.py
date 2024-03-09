full=[1,1,2,3,3,5]
empty=[]
for i in full:
    if i not in empty:
        empty.append(i)
print(empty)