# 10.3

class Customer:
    def __init__(self, name, surname, remaining_balance):
        self.name = str(name)
        self.surname = str(surname)
        self.remaining_balance = str(remaining_balance)
    def customer_info(self):
        return 'Клиент: "{0} {1}" Баланс: "{2}" руб'.format(self.name, self.surname, self.remaining_balance)
castum_1 = Customer('Иван', 'Петров', '50')

print(castum_1.customer_info())


input()
