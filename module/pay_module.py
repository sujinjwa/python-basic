# 결제 정보, 관리 모듈
# 버전 나타내는 변수
version = 2.0

# 모듈 만든 사람 출력하는 함수
def printAuthor():
    print('조수진')

# 결제 기능 클래스
class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time
    
    def get_payment_info(self):
        return f'{self.time} {self.id} {self.price}'

# 해당 파일을 직접 실행했을 때만 실행되도록 설정
if __name__ == '__main__':
    print('pay module 실행')

# print(__name__) # __main__