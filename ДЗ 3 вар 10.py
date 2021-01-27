class Car:
    # __id = 0
    # __marka = ''
    # __model = ''
    # __god_vypuska = 0
    # __color = ''
    # __price = 0
    # __reg_number = ''

    def __init__(self, id0, marka0, model0, god_vypuska0, color0, price0, reg_number0):
        self.__id = id0
        self.__marka = marka0
        self.__model = model0
        self.__god_vypuska = god_vypuska0
        self.__color = color0
        self.__price = price0
        self.__reg_number = reg_number0

    def get_id(self):
        return self.__id

    def get_marka(self):
        return self.__marka

    def get_model(self):
        return self.__model

    def get_god_vypuska(self):
        return self.__god_vypuska

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def get_reg_number(self):
        return self.__reg_number

def spiski(i):
    print('id:'  + str(cars[i].get_id()))
    print('Марка: ' + str(cars[i].get_marka()))
    print('Модель: ' + str(cars[i].get_model()))
    print('Год выпуска: ' + str(cars[i].get_god_vypuska()))
    print('Цвет: '+ str(cars[i].get_color()))
    print('Цена: ' + str(cars[i].get_price()))
    print('Регистрационный номер: ' + str(cars[i].get_reg_number()))



cars = [Car(1, 'Shkoda','Rapid', 1995, 'Blue', 12000, 'c987hh'),
          Car(2, 'Opel','Corsa', 2000, 'Black', 15000, 'g678kk'),
          Car(3, 'Volkswagen', 'Polo', 1993, 'Grey', 10000, 'f787ff'),
          Car(4, 'BMW', 'X5', 2005, 'Red', 35000, 'h007ry'),
          Car(5, 'Volvo', 'XC90',2010, 'Yelow', 48000, 'f767ko'),
          Car(6, 'Mersedec','Benz', 1999, 'Pink', 13000, 'h342fd'),
          Car(7, 'Mersedec', 'C150', 1994, 'Black', 13500, 'h372fl'),
          Car(8, 'Opel','Corsa', 2006, 'Red', 11000, 'g458yu')]

c=0
marka=0
c = str(input('а) Ведите марку автомобиля: \n'))
i = 0
while i < len(cars):
    if cars[i].get_marka() == c:
        spiski(i)
    i+=1

current_year = 2021
sroc_expl = int(input('б) Введите срок эксплуатации: \n'))
i = 0
while i < len(cars):
    if current_year - cars[i].get_god_vypuska() > sroc_expl:
        spiski(i)
    i += 1
