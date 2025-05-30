class BMW:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("250 km/h")

class Ferrari:
    def fuel_type(self):
        print("Petrol + Hybrid")

    def max_speed(self):
        print("340 km/h")

def car_info(car):
    car.fuel_type()
    car.max_speed()

b = BMW()
f = Ferrari()

car_info(b)
car_info(f)
