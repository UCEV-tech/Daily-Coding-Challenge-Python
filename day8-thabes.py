#gives the maximum no of 1's in the binary of entered number as sequence like ex:13
#binary number of 13 is 1101base2 here 2 1's are in seq thats the max sequence of 1's
n = int(input("enter a  number").strip())
t=0
r=0
while n!=0:
    if n%2==1:
        t+=1
    elif n%2==0:
        t=0
    r=max(t,r)
    n=int(n/2)
print(r)