class Car:
    def init(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0
        self.fuel = 70



    def __add_distance(self, killometry):
        self.odometr += killometry
        return self.odometr

    def __subtract_fuel(self, liters):
        self.fuel -= liters

    def drive(self, killometry):
        liters = killometry / 10
        if liters <= self.fuel:
            self.__add_distance(killometry)
            print('Let’s drive!')
        elif self.fuel == 0:
            self.__subtract_fuel(liters)
            print('Nujno bolwe benzi!')

    def __str(self):
        print(f'Car {self.model} {self.year} {self.fuel} {self.odometr}')



car2 = Car('kg','bmwx6', 2239)
print(car2.model)
print(car2.year)
car2.drive(300)

print(car2.fuel)

