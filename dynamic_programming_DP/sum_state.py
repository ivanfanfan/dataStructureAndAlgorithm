def solve1(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return solve(n - 1) + solve(n - 3) + solve(n - 5)


dp = []

def solve(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = solve(n - 1) + solve(n - 3) + solve(n - 5)
    return dp[n]

#
#    TODO
#    if dp[n] != -1:
#       ~~^^^
#    IndexError: list index out of range

if __name__ == '__main__':
    print(solve1(6))
