#permituation of given values in the list1
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
z=int(input("enter the value if z:"))
list1=[[i,j,k]for i in range(x+1)for j in range(y+1)for k in range(z+1)]
print("here the arrangement of xyz",list1)
