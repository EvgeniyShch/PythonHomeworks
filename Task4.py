from time import sleep

class Car:

    color = "black"

    def __init__(self, name, acceleration=10, is_police=False, speed=0):
        self.name = name
        self.acceleration = acceleration
        self.is_police = is_police
        self.speed = speed

    def go(self):
        print(f"{self.name} начал движение")
        for i in range(101):
            print('\r', f'{self.name} едет со скоростью {round(self.speed, 1)} км/ч', end="", sep="")
            self.speed += self.acceleration / 10
            sleep(0.02)
        for i in range(100):
            print('\r', f'{self.name} едет со скоростью {round(self.speed, 1)} км/ч', end="", sep="")
            self.speed += self.acceleration / 100
            sleep(0.02)
        Car.show_speed(self)


    def stop(self):
        Car.speed = 0
        print('\r', f'{self.name} остановился. Скорость {round(Car.speed, 1)} км/ч', end="", sep="")
        sleep(0.2)
        decision = input(f'\nХотите начать движение? y/n\n')
        if decision.upper() == "Y":
            self.speed = 0
            Car.go(self)
        else:
            print(f'Не хотите, как хотите')

    def turn(self):
        decision = input(f'\nХотите повернуть? y/n\n')
        while True:
            if decision.upper() == "Y":
                turning = input(f'Куда хотите повернуть? R/L\n')
                if turning.upper() == ("R" or "RIGHT"):
                    print(f'{self.name} повернул направо')
                    break
                elif turning.upper() == ("L" or "LEFT"):
                    print(f'{self.name} повернул налево')
                    break
                else:
                    print('\r', 'Команда не распознана, укажите верное направление Right / Left. ', end="", sep="")
                    continue
            else:
                print('Поворот отменен')
                break


    def show_speed(self):
        print('\r', f'{self.name} разогнался до {round(self.speed, 1)} км/ч', end="", sep="")
        sleep(1)

class TownCar(Car):

    def __init__(self, name, acceleration=7):
        super().__init__(name, acceleration)

    def show_speed(self):
        if self.speed > 60:
            print('\r',
                  f'Ваша скорость {round(self.speed, 1)} км/ч превышает допустимый лимит для {self.name} 60 км/ч, сбавьте скорость!', sep="",
                  end="")
            decision = input(f'\nХотите продолжить движение на скорости 60 км/ч? y/n\n')
            if decision.upper() == "Y":
                self.speed = 60
                self.show_speed()
            else:
                self.stop()
        else:
            print(f'{self.name} сбавил скорость до {round(self.speed, 1)} км/ч')

class SportCar(Car):

    def __init__(self, name, acceleration=30):
        super().__init__(name, acceleration)

class WorkCar(Car):

    def __init__(self, name, acceleration=5):
        super().__init__(name, acceleration)

    def show_speed(self):
        if self.speed > 40:
            print('\r', f'Ваша скорость {round(self.speed, 1)} км/ч превышает допустимый лимит для {self.name} 40 км/ч, сбавьте скорость!', end="", sep="")
            decision = input(f'\nХотите продолжить движение на скорости 40 км/ч? y/n\n')
            if decision.upper() == "Y":
                self.speed = 40
                self.show_speed()
            else:
                self.stop()
        else:
            print(f'{self.name} сбавил скорость до {round(self.speed, 1)} км/ч')



class PoliceCar(Car):

    def __init__(self, name, acceleration=9999, is_police=True):
        super().__init__(name, acceleration, is_police)

gruzovik = WorkCar("Газелька")
gruzovik.go()
gruzovik.show_speed()
gruzovik.turn()
gruzovik.stop()
print()
porshe = SportCar("Porsche-911")
porshe.go()
porshe.show_speed()
porshe.stop()
print()
carsharing = TownCar("Москвич")
carsharing.go()
carsharing.show_speed()
print()
bobik = PoliceCar("УАЗ-469", 1)
bobik.go()
bobik.show_speed()
print()
bobik2 = PoliceCar("УАЗ-3151", 2)
bobik2.go()
bobik2.show_speed()
print()
bobik3 = PoliceCar("Новейший УАЗ-315195 «Хантер»")
bobik3.go()
bobik3.show_speed()