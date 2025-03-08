from pprint import pprint


def lcs(str1, str2):  # Longest Common Subsequence - O(mn)
    l1, l2 = len(str1), len(str2)
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


    print()
    cp = [['~'] * (l2 + 2) for _ in range(l1 + 2)]
    for i in range(l1 + 2):
        for j in range(l2 + 2):
            if j == 0 or i == 0:
                cp[i][j] = '-'
            else:
                cp[i][j] = f"{dp[i - 1][j - 1]}"


    for i in range(1, l1 + 1):
        cp[i][0] = str1[i - 1]
    for j in range(1, l2 + 1):
        cp[0][j] = str2[j - 1]
    print()
    pprint(cp)
    print()
    pprint(dp)

    return dp[l1][l2]
