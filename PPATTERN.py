# Problem: https://www.codechef.com/problems/PPATTERN

# Consider the following 4×4 pattern:

#  1  2  4  7
#  3  5  8 11
#  6  9 12 14
# 10 13 15 16
# You are given an integer N. Print the N×N pattern of the same kind (containing integers 1 through N2).

# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains a single integer N.
# Output
# For each test case, print N lines; each of them should contain N space-separated integers.

# Constraints
# 1≤T≤10
# 1≤N≤100
# Subtasks
# Subtask #1 (100 points): Original constraints

# Example Input
# 1
# 4
# Example Output
# 1 2 4 7
# 3 5 8 11
# 6 9 12 14
# 10 13 15 16

#My Solution
def getPettern(N):
    ar = [[0]*N for _ in range(N)]
    num, i = 1, 0
    while num <= N*N:
        for j in range(i+1):
            if j < N and i - j < N:
                ar[j][i-j] = num
                num += 1
        i += 1
    return ar

for _ in range(int(input())):
    N = int(input())
    ans = getPettern(N)
    for row in ans:
        print(' '.join(map(str, row)))
