#weighted mean calculation
import math
import random
import re
def weightedMean(X, W):
    list1=[]
    for i in range(0,len(X)):
        list1.append(X[i]*W[i])
    weightmean=sum(list1)/sum(W)
    print("the weighted mean is:",round(weightmean))    
        
if __name__ == '__main__':
    n = int(input("enter the no of element to be inserted:").strip())

    vals = list(map(int, input("enter the values upto n:").rstrip().split()))

    weights = list(map(int, input("enter the weights of each corresponding values:").rstrip().split()))

    weightedMean(vals, weights)
