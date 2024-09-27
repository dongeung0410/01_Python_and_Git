# 1번 문제
from msvcrt import kbhit

a=input("문자열을 입력하세요")
if a =="안녕하세요":
    print("반갑습니다")
else:
    print("인사를 먼저하세요")

# 2번 문제
number=int(input("값을 입력하세요:"))
if number + 100 >= 150:
    print(number+100)
else:
    print("값이 부족합니다")

# 3번 문제
result=[]
numbers=[100,200,300]
for a in numbers:
    n=a+(a*0.1)
    result.append(n)
print(result)

# 4번 문제
results=[]
numbers2=[3,100,23,33,72,94]
for q in numbers2:
    if q % 3 == 0:
        results.append(q)
print(results)

# 5번문제
w = 1
while w <= 1000:
    print(w)
    w=w+1

# 6번 문제
e=1
r=[]
while e <= 100:
    if e % 2 != 0:
        r.append(e)
    e += 1
print("홀수의 합:", sum(r))
