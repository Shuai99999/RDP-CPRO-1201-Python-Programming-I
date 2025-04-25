class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


Tesla = Vehicle(320, 650)
print(Tesla.max_speed, Tesla.mileage)
