n=int(input("enter the length of elements in the list:"))
print("enter the values of list one by one upto length:")
list1=list(map(int,input().split()))
def median_of_list(n,list1):
    list1.sort()
    if n%2==0:
       med=abs(list1[int(n/2)]+list1[(int(n/2)-1)]) 
       return med/2
    else:
        med=round(n/2)
        return list1[med]
def mode(n,list1):
    return max(list1,key=list1.count)
mean=sum(list1)/n
median=median_of_list(n,list1)
print(f"the mean:{mean:.1f}\nthe median:{median:.1f}\nthe mode:{mode(n,list1)}")
