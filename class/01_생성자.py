class Monster:
    # 생성자 = 인스턴스 만들 때 호출되는 메서드
    def __init__(self, health, attack, speed):
        # self = 인스턴스(자기 자신)
        self.health = health
        self.attack = attack
        self.speed = speed
    
    def decrease_health(self, num):
        self.health -= num

    def get_health(self):
        return self.health

# 고블린 인스턴스 생성
goblin = Monster(800, 120, 300)
wolf = Monster(1500, 200, 350)

goblin.decrease_health(100)
print(goblin.get_health())