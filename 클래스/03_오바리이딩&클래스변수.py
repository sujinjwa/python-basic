# 상속
# : 클래스들에 중복된 코드를 제거하고
#   유지보수를 편하게 하기 위해서 사용

# 클래스 변수
# : 인스턴스들이 모두 공유하는 변수

import random

# 부모 클래스
class Monster:
    max_num = 1000 # 클래스 변수
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1

    def move(self):
        print(f'[{self.name}] 지상에서 이동하기')

# 자식 클래스: 생성자 생략 가능
class Wolf(Monster):
    pass

class Shark(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack) # super() = 부모 클래스의 생성자 불러오기
        self.skills = ('불뿜기', '꼬리치기', '날개치기') # 멤버 변수

    # 메서드 오버라이딩: 부모 클래스에서 정의했던 메서드를 자식 클래스에서 재정의
    def move(self):
        print(f'[{self.name}] 헤엄치기')
    
    def use_random_skill(self):
        print(f'[{self.name}] 스킬 사용 {self.skills[random.randint(0, 2)]}')

class Dragon(Monster):
    def move(self):
        print(f'[{self.name}] 날기')

# 인스턴스 생성
wolf = Wolf('울프', 1500, 200)
wolf.move()
print(wolf.max_num)

shark = Shark('샤크', 3000, 400)
shark.move()
shark.use_random_skill()
print(shark.max_num)

dragon = Dragon('드래곤', 8000, 800)
dragon.move()
print(dragon.max_num)