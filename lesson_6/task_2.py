class Road:
    def __init__(self, l, w, t):
        self._length = l
        self._width = w
        self.thickness = t
        self.mass_1_sq_m = 25
    def mass_calculate(self):
        self.mass = self._length * self._width * self.mass_1_sq_m * self.thickness
        print(f'Масса асфальта {self.mass/1000} тонн')


road_1 = Road(1000, 10, 20)
road_1.mass_calculate()
