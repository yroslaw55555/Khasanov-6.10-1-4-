# 10.3

class Volunteer:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def get_info(self):
        print(f'{self.name}, г. {self.city}')


class StatusVol(Volunteer):
    def __init__(self, name, city, status):
        super().__init__(name, city)
        self.status = status

    def get_info(self):
        print(f'{self.name}, г. {self.city}, статус "{self.status}"')


vasiliy_pupkin = Volunteer('Василий Пупкин', 'Казань')
ivan_petrov = StatusVol('Иван Петров', 'Москва', 'Наставник')

people = [vasiliy_pupkin, ivan_petrov]

for person in people:
    person.get_info()


input()
