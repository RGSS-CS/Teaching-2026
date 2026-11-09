from sys import stdin
input = stdin.readline

N = int(input())
K = int(input())

totalSum = N
for i in range(K):
    N *= 10
    totalSum += N

print(totalSum)
