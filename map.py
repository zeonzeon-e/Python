# map : 첫 번째 인자(함수), 두 번째 인자(반복 가능한 자료형)
# map을 사용하면 list로 다시 한 번 바꿔줘야 한다.
# 여기서 list가 없어도 되네..

print(type(list(map(int, input().split()))))
