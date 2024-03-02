dict={}
n=int(input("how many items are you going to insert:"))
for i in range(0,n):
    key,value=input().split()
    dict.update({key:value})

while True:
    try:
        name=str(input("enter the item key to find:"))
        numb=dict.get(name)
        if not numb:
            print("Not found")
        else:
            print("{}={}".format(name,numb))
    except EOFError as e:
        break
