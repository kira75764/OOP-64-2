class Hero:
    def __init__(self, name, health, level, strength):
        self.name = name
        self.health = health
        self.level = level
        self.strength = strength
#ggssd
class mage(Hero):
    def __init__(self, name, health, level, strength, mana):
        super().__init__(name, health, level, strength)
        self.mana = mana

    def attack(self):
     self.mana -=1
     print(f'{self.name}, Кастует заклинание!!!, Твой остаток маны:{self.mana}')


class warrior(Hero):
    def __init__(self, name, health, level, strength, stamina):
        super().__init__(name, health, level, strength)
        self.stamina = stamina

    def attack(self):
        self.stamina -= 1
        print(f'{self.name} Наносит удар мечом!!!, Остаток выносливости:{self.stamina}')


class assasin(Hero):
    def __init__(self, name, health, level, strength, secrecy):
        super().__init__(name, health, level, strength)
        self.secrecy = secrecy

    def attack(self):
        self.secrecy -= 1
        print(f'{self.name} Наносит удар из-под тишка, Остаток скрытности:{self.secrecy}')



player_choice = input("Выберите персонажа: mage, warrior, assassin: ").lower()



if player_choice == "mage":
    player = mage("mage", 10, 1, 10, 10)

elif player_choice == "warrior":
    player = warrior("warrior", 10, 1, 10, 10)

elif player_choice == "assassin":
    player = assasin("assassin", 10, 1, 10, 10)


import random

bot_choice = random.choice(['mage,' 'warrior,' 'assasin'])
print('Бот выбрал:', bot_choice)


if bot_choice == "mage":
    bot = mage("mage", 10, 1, 10, 10)
elif bot_choice == "warrior":
    bot = warrior("warrior", 10, 1, 10, 10)
elif bot_choice == "assasin":
    bot = assasin("assasin", 10, 1, 10, 10)

player.attack()
bot.attack()

if player_choice == bot_choice:
    print('Ничья!!')

elif player_choice == 'warrior' and bot_choice == 'assasin':
    bot.health -=1
    player.stamina -=1
    print('Войн победил!!!')
    print('Здоровье бота:', bot.health)

elif player_choice == 'mage' and bot_choice == 'assasin':
    bot.health -=1
    player.secrecy -=1
    print('Ассасин победил!!!')
    print('Здоровье бота:', bot.health)

elif player_choice == 'mage'and bot_choice == 'warrior':
    bot.health -=1
    player.mana -=1
    print('Маг победил!!')
    print('Здоровье бота:', bot.health)

else:
    player.health -=1
    print('Ты проиграл')
    print('Твое здоровье:', player.health)