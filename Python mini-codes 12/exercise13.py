class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


school_bus = Bus("School Bus", 180, 1200)

print(school_bus.name)
print(school_bus.max_speed)
print(school_bus.mileage)
