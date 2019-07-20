"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
Follow up: Do this in O(N) time.
Input Format:
The first line of input contains size of array, which is denoted by N and second line of input contains N space separated integers.
Output Format:
The first and only line of output should print the maximum subarray sum, as described in the description.

code in python 3
"""
def max(n,m):
    return n if n>m else m

if __name__ == '__main__':
    n=int(input())
    l=list(map(int,input().split()))
    c_max=g_max=l[0]
    for i in range(1,n):
        c_max=max(l[i],c_max+l[i])
        if c_max>g_max:
            g_max=c_max

    print(g_max)
