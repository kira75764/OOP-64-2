class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f'Привет!,я {self.name}, мой уровень {self.level}')

    def attack(self, enemy):
        self.strength -= 1
        print(f'{self.name} наносит удар!, остаток {self.strength}')
        enemy.health -= 1
        print(f'{enemy.name} потерял(а) 1 очко здоровья, остаток здоровья{enemy.health}')
    def rest(self):
        if self.health < 100:
            self.health +=1
            print(f'{self.name} отдыхает, нынешнее здоровье {self.health}')


ayana = Hero('Ayana', 1, 100, 100)
misha = Hero('Misha', 2, 100, 100)


misha.attack(ayana)
ayana.rest()
print(ayana.health)