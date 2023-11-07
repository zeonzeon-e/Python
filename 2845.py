# https://www.acmicpc.net/problem/2845

N, M = map(int, input().split())
news = list(map(int, input().split()))
# a = list()
# for i in news:
#     a.append(i - N * M)
#     i = i - (N * M)
#     # print(i - (N * M), end=" ")
# print(*a)
# print(*news)
# for i in news[:-1]:
#     print(str(i - (N * M)).rstrip(), end=" ")
tmp = []

for i in news:
    tmp.append(str(i - (N * M)))

print(" ".join(tmp))
