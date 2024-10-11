class 회원가입:
    def __init__(self,이름,나이,연락처):
        self.이름=이름
        self.나이=나이
        self.연락처=연락처
    def indo(self):
        print('가입하신 계정의 이름은',self.이름,'이며,나이는',self.나이,'그리고 연락처는',self.연락처,'입니다')

내정보=회원가입('정동승','23세','010-2488-1617')
내정보.indo()

a=input("메시지를 입력하세요")
def check_length_of_message(message):
    Q=len(message)
    if Q <= 20:
        return "요금은 50원 입니다"
    elif Q > 20:
        return "요금은 100원입니다"
print(check_length_of_message(a))