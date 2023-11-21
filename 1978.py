# https://www.acmicpc.net/problem/1978

N = int(input())
num = list(map(int, input().split()))
decimal = 0
for i in num:
    for j in range(2, i + 1):
        if i % j == 0:
            if j == i:
                decimal += 1
            break

print(decimal)
