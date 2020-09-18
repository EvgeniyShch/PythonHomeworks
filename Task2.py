from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, parametr):
        self.parametr = parametr

    @abstractmethod
    def fabric_consumption(self):
        return f'Расход ткани будет {self.parametr} на метр'


class Coat(Clothes):
    def __init__(self, parametr, width):
        super().__init__(parametr)
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width < 1:
            self.__width = 1
        else:
            self.__width = width

    def fabric_consumption(self):
        return f'Расход ткани на {self.__class__.__name__} будет {self.width * (self.parametr / 6.5 + 0.5):.2f} на метр'


class Jacket(Clothes):

    def __init__(self, parametr, height, color):
        super().__init__(parametr)
        self.height = height
        self.color = color

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 1:
            self.__height = 1
        else:
            self.__height = height

    def fabric_consumption(self):
        return f'Расход ткани на {self.__class__.__name__} будет {self.height * (self.parametr * 2 + 0.3):.2f} на {self.color} метр'


inp_1 = Coat(10, 3)
inp_2 = Jacket(10, -2, "red")
print(inp_1.fabric_consumption())
print(inp_2.fabric_consumption())