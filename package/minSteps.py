def minSteps(n):
    if n==1:
        return 0
    res=[i for i in range(n+1)]
    for i in range(3,n+1):
        for j in range(int(i/2),1,-1):
            if(i%j==0):
                res[i] = res[j] + res[i/j]
                break
    return res[n]

minSteps(6)