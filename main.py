def solve(n, a):
    res = []
    if n == 1:
        res.append(0)
        return res
    if a[0] >= a[1]:
        res.append(0)
    if n != 1:
        for i in range(1, n-1):
            if a[i] >= a[i-1] and a[i] >= a[i+1]:
                res.append(i)
            
    if a[n-1] >= a[n-2]:
        res.append(n-1)
    return res


n = int(input())
a = [int(x) for x in input().split()]

for i in solve(n, a):
    print(i, end=' ')