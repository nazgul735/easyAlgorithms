import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    x=len(arr)
    neg=0
    pos=0
    zer=0
    for i in arr:
        if i==0:
            zer=zer+1
        elif i<0:
            neg=neg+1
        else:
            pos=pos+1


    neg=float(int(neg))
    pos=float(pos)
    zer=float(zer)
    print(round(pos/x, 6))
    print(round(neg/x, 6))
    print(round(zer/x, 6))

def timeConversion(s):
    if "AM" in s:
        if s[:2]=="12":
            s="".join(str(int(s[:2])-12)+"0"+str(s[2:len(s)-2]))
        else:
            s=s[:-2]
    elif "PM" in s:
        if s[:2]=="12":
            s=s[:-2]
        else:
            s="".join(str(int(s[:2])+12)+str(s[2:len(s)-2]))

    return s

def median(arr):
    mid=len(arr)//2
    if len(arr)%2==0:
        med = (arr[mid]+arr[mid-1])/2
        return med
    else:
        return arr[round(mid,0)]


def lonelyinteger(a):
    dict={}
    for i in a:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    for k, v in dict.items():
        if v==1:
            return k

def absSquareMatrx(arr):
    r_sum=0
    l_sum=0
    for i in range(len(arr)):
        l_sum=l_sum+arr[i][i]
        r_sum=r_sum+arr[i][(len(arr)-1)-i]
    print(abs(l_sum - r_sum))

def countUnique(arr):
    list=[0 for i in range(max(arr)+1)]
    for i in arr:
        list[i]=list[i]+1
    return list


# not done
def maxMatrix(mat): 
    min=[]
    max=mat[0][0]
    first=mat[0][0]
    for i in range(len(mat)):
        for j in i:
            if mat[j]>max:
                max=mat[j]
                min=[i,i.index(j)]
                
    mat[0][0]=max
    mat[min[0]][min[1]]=first

    return mat

def maxSubarray(arr):
    maxi=currentMax=arr[0]
    for i in arr[1:]:
        currentMax=max(currentMax+i,currentMax)
        maxi=max(currentMax, maxi)
    return maxi

def param(s):
    st=0
    for i in s:
        if i == "(":
            st=st+1
        elif i==")":
            st=st-1
        if st<0:
            return False
    return True



def sol(s):
    state=0
    par="()"
    for i in s:
        if i not in par:
            continue
        if i =="(":
            state=state+1
        elif i==")":
            state=state-1
            if state<0:
                return False
    if state==0:
        return True
    return False
        

        


        
        



    


            
    
            
            


