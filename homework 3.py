from abc import ABC, abstractmethod

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self._health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level}')

    def rest(self):
        self._health +=1
        pass
        print(f'{self.name} отдыхает')

    @abstractmethod
    def attack(self, enemy):
        pass


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self, enemy):
        self.mana -= 1
        self.strength -= 1
        print(f'{self.name}, Кастует заклинание!!!, Твой остаток маны:{self.mana},Также остаток силы:{self.strength}')
        enemy._health -= 1
        print(f'{enemy.name} потерял(а) 1 очко здоровья, остаток здоровья{enemy._health}')
    def rest(self):
        self.mana += 1
        self._health += 1
        self.strength += 1
        print(f'{self.name} ,Вы отдохнули и восстановили здоровье:{self._health}, И ману:{self.mana},Также силу:{self.strength}')


class Assasin(Hero):
    def __init__(self, name, level, health, strength, secrecy):
        super().__init__(name, level, health, strength)
        self.secrecy = secrecy

    def attack(self, enemy):
        self.secrecy -= 1
        self._health -= 1
        self.strength -= 1
        print(f'{self.name} Наносит удар из-под тишка, Остаток скрытности:{self.secrecy},Также остаток силы:{self.strength}')
        enemy._health -= 1
        print(f'{enemy.name} потерял(а) 1 очко здоровья, остаток здоровья{enemy._health}')

    def rest(self):
        self.secrecy += 1
        self._health += 1
        self.strength += 1
        print(f'{self.name},Вы отдохнули и восстановили здоровье:{self._health},И скрытность:{self.secrecy},Также силу:{self.strength}')

class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self, enemy):
        self.stamina -= 1
        self.strength -= 1
        print(f'{self.name} Наносит удар мечом!!!, Остаток выносливости:{self.stamina},Также остаток силы:{self.strength}')
        enemy._health -= 1
        print(f'{enemy.name} потерял(а) 1 очко здоровья, остаток здоровья{enemy._health}')

    def rest(self):
        self._health += 1
        self.stamina += 1
        self.strength += 1
        print(f'{self.name},Вы отдохнули и восстановили здоровье:{self._health},И выносливость:{self.stamina}, Также силу:{self.strength}')

assasin = Assasin('Assasin', 1, 80, 80, 100)
warrior = Warrior('Warrior', 1, 80, 100, 100)
mage = Mage('Mage', 1, 80, 50, 100)

assasin.greet()
warrior.greet()
mage.greet()

assasin.attack(mage)
mage.attack(warrior)
warrior.attack(assasin)

mage.rest()
warrior.rest()
assasin.rest()