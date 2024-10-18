import random
def lotto():
    result=[]
    while len(result)<6:
        n=random.randint(1,45)
        if n not in result:
            result.append(n)
    return result
print(lotto())

class 구구단:
    def __init__(self,num):
        self.num=num
    def output(self):
        print(f'----{self.num}단-----')
        for a in range(1,10):
            print(f' {self.num} X {a} = {self.num*a}')
num=int(input('숫자를 입력하세요'))
계산=구구단(num)
계산.output()