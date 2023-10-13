# map : 첫 번째 인자(함수), 두 번째 인자(반복 가능한 자료형)
# map을 사용하면 list로 다시 한 번 바꿔줘야 한다.

num = map(int, input().split())
result = 0
for i in num:
    result += i**2
print(result % 10)
