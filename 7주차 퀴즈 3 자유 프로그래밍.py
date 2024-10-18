# 제가 만든 프로그래밍은 할 일을 관리하는 프로그램입니다.
# 항상 과제제출 청소 빨래 등 해야할건 많은데 까먹는 경우가 종종 있기 때문입니다.
# 따라서 실생활에서 사용할수 있는 할 일 관리 프로그래밍을 만들어 보았습니다.
# 가독성을 높이기 위해 한글을 좀 많이 사용하였습니다.

# 할일 클래스는 개별 할 일 항목을 나타낸다.
class 할일:
    def __init__(self, 제목, 마감일, 우선순위):
        self.제목 = 제목
        self.마감일 = 마감일
        self.우선순위 = 우선순위
        self.완료됨 = False  # 할 일이 완료되었는지 상태를 표시

    def 할일_정보_출력(self):
        상태 = "완료" if self.완료됨 else "미완료"
        return f"제목: {self.제목}, 마감일: {self.마감일}, 우선순위: {self.우선순위}, 상태: {상태}"
# 할일 목록 클래스는 여러 할 일 항목을 저장하고 관리하는 역할을 한다.
class 할일목록:
    def __init__(self):
        self.할일들 = []

    def 할일_추가(self, 제목, 마감일, 우선순위):
        새_할일 = 할일(제목, 마감일, 우선순위)
        self.할일들.append(새_할일)
        print(f"할 일 '{제목}'이(가) 추가되었습니다.")

    def 할일_삭제(self, 제목):
        for 할일 in self.할일들:
            if 할일.제목 == 제목:
                self.할일들.remove(할일)
                print(f"할 일 '{제목}'이(가) 삭제되었습니다.")
                return
        print(f"할 일 '{제목}'을 찾을 수 없습니다.")

    def 완료된_할일_삭제(self):
        for 할일 in self.할일들[:]:
            if 할일.완료됨:
                self.할일들.remove(할일)
                print(f"완료된 할 일이 삭제되었습니다.")

    def 할일_목록_출력(self):
        if not self.할일들:
            print("할 일이 없습니다.")
            return
        for 할일 in self.할일들:
            print(할일.할일_정보_출력())
# 사용자가 할 일을 추가하거나 삭제하고,할일을 완료 상태로 변경하며, 할일 목록을 출력하는 함수를 담은 클래스
class 할일관리:
    def __init__(self):
        self.할일목록 = 할일목록()

    def 할일_추가(self, 제목, 마감일, 우선순위):
        self.할일목록.할일_추가(제목, 마감일, 우선순위)

    def 할일_삭제(self, 제목):
        self.할일목록.할일_삭제(제목)

    def 할일_완료_변경(self, 제목):
        for 할일 in self.할일목록.할일들:
            if 할일.제목 == 제목:
                할일.완료됨 = True  # 할 일을 완료로 변경하기 위해
                print(f"할 일 '{제목}'이(가) 완료로 처리되었습니다.")
                break
        self.할일목록.완료된_할일_삭제()

    def 할일_목록_출력(self):
        print("할 일 목록:")
        self.할일목록.할일_목록_출력()

    def 할일_입력(self):
        제목 = input("할 일의 제목을 입력하세요: ")
        마감일 = input("할 일의 마감일을 입력하세요 (예: 2024-10-18): ")
        우선순위 = input("할 일의 우선순위를 입력하세요 (high/medium/low): ")
        self.할일_추가(제목, 마감일, 우선순위)

    def 할일_완료_변경_입력(self):
        제목 = input("완료 처리할 할 일의 제목을 입력하세요: ")
        self.할일_완료_변경(제목)

    # 사용자가 할 일을 계속 추가할지 여부를 묻는 함수로 input함수를 사용했을때 한글로
    # 예 아니오 하는게 흐름상 맞지만 한글이 입력이 안되서 영어로 입력하는걸로 만들었습니다. 또한 strip() loxer()부분은 인터넷의 도움을 받았습니다.
    def 할일_추가_계속(self):
        while True:
            self.할일_입력()  # 할 일 입력
            계속 = input("할 일을 더 추가하시겠습니까? (yes/no): ").strip().lower()
            if 계속 == 'yes':
                continue  # 'yes' 입력 시 계속 추가
            elif 계속 == 'no':
                break  # 'no' 입력 시 루프 종료
            else:
                print("잘못된 입력입니다. 'yes' 또는 'no'를 입력해주세요.")

# 할 일 관리 시스템 객체 생성
관리 = 할일관리()

# 할 일을 사용자로부터 입력받아 추가
관리.할일_추가_계속()

# 할 일 목록 출력
관리.할일_목록_출력()

# 사용자가 할 일을 완료 처리하도록 입력받고 완료 상태로 변경
관리.할일_완료_변경_입력()

# 할 일 목록 출력
관리.할일_목록_출력()
