class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
    
    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self, seating_capacity=50):
        super().__init__(seating_capacity)
    
    def fare(self):
        base_fare = super().fare()
        return base_fare + (0.1 * base_fare)

bus = Bus()
print("Total Bus Fare: INR", bus.fare())
