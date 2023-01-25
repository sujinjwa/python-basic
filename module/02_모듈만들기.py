import pay_module

# 변수
print(pay_module.version)

# 함수
pay_module.printAuthor()

# 클래스
payment_info = pay_module.Pay('20191234', 4000, 20230125)
print(payment_info.get_payment_info())

# __pyche__ 폴더 자동 생성
# 실행 속도 향상으로 생성되는 파일

print(pay_module.__name__) # pay_module