N = int(input("enter a number to check it is weird or not:"))
if(N % 2 == 1):
        print('Weird')
else:
    if(N in range(2,6)):
        print('Not Weird')
    elif(N in range(6, 21)):
        print('Weird')
    else:
        print('Not Weird')