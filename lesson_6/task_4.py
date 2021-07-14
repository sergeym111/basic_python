class Car:
    def __init__(self, c='white', n='VAZ', i_p=False):
        self.color = c
        self.name = n
        self.is_police = i_p
        self.speed = 0

    def go(self, speed=40):
        print(f"Автомобиль {self.name} начал движение")
        self.speed = speed

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, direction='Прямо'):
        if not direction in ['Прямо', 'Налево', 'Направо', 'Обратно']:
            print("Неправильно задано направление движение")
        else:
            print(f"Автомобиль движется {direction}")

    def show_speed(self):
        print(f"Скорость движения {self.speed} км/ч")


class TownCar(Car):
    role = 'Городской'

    def go(self, speed=40):
        print(f"{self.role} автомобиль {self.name} начал движение")
        self.speed = speed

    def show_speed(self):
        print(f"Скорость движения {self.speed} км/ч")
        if self.speed > 60 and self.is_police == False:
            print(f"{self.role} автомобиль {self.name} движется с превышением скорости")
        else:
            print(f"{self.role} автомобиль {self.name} движется с допустимой скоростью")


class WorkCar(Car):
    role = 'Служебный'

    def go(self, speed=40):
        print(f"{self.role} автомобиль {self.name} начал движение")
        self.speed = speed

    def show_speed(self):
        print(f"Скорость движения {self.speed} км/ч")
        if self.speed > 40 and self.is_police == False:
            print(f"{self.role} автомобиль {self.name} движется с превышением скорости")
        else:
            print(f"{self.role} автомобиль {self.name} движется с допустимой скоростью")


class SportCar(Car):
    role = 'Спортивный'

    def go(self, speed=40):
        print(f"{self.role} автомобиль {self.name} начал движение")
        self.speed = speed

    def show_speed(self):
        print(f"{self.role} автомобиль {self.name} движется со скоростью {self.speed}")


car_1 = Car(n='BMW')
car_1.go(70)
car_1.show_speed()

car_2 = TownCar()
car_2.go(70)
car_2.show_speed()

car_3 = SportCar()
car_3.go(150)
car_3.show_speed()

car_4 = WorkCar(n='МАЗ')
car_4.go(60)
car_4.show_speed()
