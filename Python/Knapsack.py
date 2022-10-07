w1=[1,2,3,4,5,6]
v1=[100,20,50,100,12,14]
W=7
n=len(w1)
def knapsack(w,v,W,n):
    if n==0 or W==0:
        return 0
    if w[n-1]<=W:
        return max(v[n-1] + knapsack(w,v,W-w[n-1],n-1),knapsack(w,v,W,n-1))
    elif w[n-1]>W:
        return knapsack(w,v,W,n-1)

x=knapsack(w1,v1,W,n)
print(x)