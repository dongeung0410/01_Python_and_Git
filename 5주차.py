# 1번 문제
def add(n1,n2,n3,n4):
    result = sum([n1,n2,n3,n4])
    return result
sum_result=add(1,2,3,4)
print(sum_result)

def multiply(n1,n2,n3,n4):
    result= n1*n2*n3*n4
    return result
multiply_result=multiply(1,2,3,4)
print(multiply_result)

# 2번 문제
def determine(number):
    result=[]
    if number % 2 == 0:
        k=("짝수")
        result.append(k)
    elif number % 2 != 0:
        l=("홀수")
        result.append(l)
    return result[0]
result=determine(5)
print("결과값은",result)

# 3번 문제
def average(list_numbers):
   total=0
   for numbers in list_numbers:
       total += numbers
   average_result= total/ len(list_numbers)
   return average_result

result=average([100,200,300,400,500,1000])
print("평균값은",result)

# 4번 문제
class Game:
    def __init__(self,name,sex,job):
        self.name=name
        self.sex=sex
        self.job=job
    def attack(self):
        print("공격!","(",self.name, "," ,self.sex, ",", self.job, ")",)
my_id=Game("정동승","남자","학생")
my_id.attack()

# 5번 문제
class 부동산:
    def __init__(self,위치,평수,건물의종류,가격,준공년도):
        self.위치=위치
        self.평수=평수
        self.건물의종류=건물의종류
        self.가격=가격
        self.준공년도=준공년도
    def 정보(self):
        print(self.위치,",",self.평수,",",self.건물의종류,",",self.가격,",",self.준공년도)

my_부동산 = 부동산("충주","3000평","학교","1,000,000,000원","2002준공")
my_부동산.정보()