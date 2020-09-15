class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки with {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки with {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки with {self.title}")


pen = Pen("Ручка")
pen.draw()

pencil = Pencil("Карандаш")
pencil.draw()

handle = Handle("Маркер")
handle.draw()