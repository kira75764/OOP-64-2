rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def conver_to_kgs(self):
        if self.currency not in rates:
            raise ValueError('Неизвестная валюта')
        return self.amount * rates[self.currency]

    def __str__(self):
        return f'{self.amount} {self.currency}'

    def __add__(self, other):
        if not isinstance(other, Money):
            return "ошибка"

        total = self.conver_to_kgs() + other.conver_to_kgs()
        return Money(total, self.currency)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return 'ошибка'

        total = self.conver_to_kgs() - other.conver_to_kgs()
        return Money(total, self.currency)

    def __mul__(self, number):
        if not isinstance(number, (int, float)):
            return 'ошибка'

        return Money(self.amount * number, self.currency)


    def __truediv__(self, number):
        if not isinstance(number, (int, float)):
            return "ошибка"
        return Money(self.amount / number, self.currency)

money1 = Money(100, 'USD')
money2 = Money(5000, 'KGS')

print(money1)
print(money2)

print(money1 + money2)
print(money1 - money2)

print(money1 * 2)
print(money1 / 2)
