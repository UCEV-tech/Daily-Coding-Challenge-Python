import math
import os
import random
import re
import sys
''' this function compares the two list or array'''
def compareTriplets(a, b):
    A=0
    B=0
    for i in range(0,len(a)):
        if a[i]>b[i]:
            A+=1
        elif a[i]<b[i]:
            B+=1
    return [A,B]
if __name__ == '__main__':

    a = list(map(int, input("enter element for alice:").rstrip().split()))

    b = list(map(int, input("enter welement for bob:").rstrip().split()))
    print("the first score represents alice and the second represents bob:[alice,bob]")
    result = compareTriplets(a, b)
    print(result)
