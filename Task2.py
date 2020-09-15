class Road:

    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width
    def mass_road(self):
        mass = 25
        height = 5
        coverage_tons = self.length * self.width * height * mass / 1000
        print(f'Для покрытия дорожного полотна необходимо {coverage_tons} тонн асфальта')

doroga = Road(20, 5000)
doroga.mass_road()