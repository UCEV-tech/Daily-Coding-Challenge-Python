#the function used to find the quartiles
def quartiles(arr):
    arr.sort()
    def median(arr):
        n=len(arr)
        i=n//2
        if n%2==0:
            return round((arr[i-1]+arr[i])/2)
        else:
            return arr[i]
    n=len(arr)
    i=n//2
    return[median(arr[:i]),
           median(arr),
           median(arr[i:]if n%2==0 else arr[i+1:])
           ]

n=int(input("enter the size of array:"))
print("enter the element of arrayone by one:")
i=0
arr=[]
for i in range(n):
    ele=int(input())
    arr.append(ele)

print("the [Q1,Q2,Q3]are:",quartiles(arr))
    
