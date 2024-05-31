def fibo_helper(n, ans):
    # base case
    if n <= 1:
        return n

    if ans[n] != -1:
        return ans[n]

    x = fibo_helper(n - 1, ans)
    y = fibo_helper(n - 2, ans)

    ans[n] = x + y

    return ans[n]

def fibo(n):
    ans = [-1] * (n + 1)
    for i in range(0, n + 1):
        ans[i] = -1
    return fibo_helper(n, ans)

n = 5
print(fibo(n))
